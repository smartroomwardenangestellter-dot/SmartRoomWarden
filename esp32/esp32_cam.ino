#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <WiFiClientSecure.h>
#include "secrets.h" // defines WIFI_SSID, WIFI_PASSWORD, DEVICE_TOKEN - copy secrets.h.example, never commit secrets.h

// =========================
// PI SERVER
// =========================

const char* PI_BASE_URL = "https://192.168.188.91:5000";

const char* STATUS_ENDPOINT = "/status";
const char* UPLOAD_ENDPOINT = "/upload";

// Deep Sleep 5 Minuten
const uint64_t SLEEP_US = 5ULL * 60ULL * 1000000ULL;


// =========================
// CAMERA PINS
// AI THINKER ESP32-CAM
// =========================

#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5

#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22


void deepSleep() {

  Serial.println("Deep Sleep...");

  esp_sleep_enable_timer_wakeup(SLEEP_US);

  esp_deep_sleep_start();
}


bool connectWiFi() {

  WiFi.mode(WIFI_STA);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  Serial.print("Verbinde WLAN");

  unsigned long start = millis();

  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");

    if (millis() - start > 20000) {

      Serial.println("\nWLAN Fehler");

      return false;
    }
  }

  Serial.println("\nWLAN verbunden");

  Serial.println(WiFi.localIP());

  return true;
}


bool initCamera() {

  camera_config_t config;

  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;

  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;

  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;

  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;

  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;

  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;

  config.frame_size = FRAMESIZE_QVGA;
  config.jpeg_quality = 15;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);

  if (err != ESP_OK) {

    Serial.println("Kamera Fehler");

    return false;
  }

  return true;
}


bool checkStatus() {

  WiFiClientSecure client; // Hier "Secure" nutzen!
  // Accepted risk (not a bug): the Pi runs Flask with ssl_context="adhoc", which regenerates
  // a self-signed cert on every server restart, so there is no stable cert/public key to pin.
  // setInsecure() skips verification. Threat model: LAN-only, WPA2-protected network - accepted
  // for now. Real fix would require the Pi to serve a persistent, generated-once certificate
  // whose fingerprint this firmware can pin against.
  client.setInsecure();
  HTTPClient http;

  String url = String(PI_BASE_URL) + STATUS_ENDPOINT;

  http.begin(url);

  http.addHeader("X-Device-Token", DEVICE_TOKEN);

  int httpCode = http.GET();

  if (httpCode <= 0) {

    Serial.println("Status Fehler");

    http.end();

    return false;
  }

  String response = http.getString();

  response.trim();

  response.toLowerCase();

  http.end();

  Serial.println(response);

  return response == "true";
}


bool uploadImage(camera_fb_t* fb) {

  HTTPClient http;
  WiFiClientSecure client; // Hier "Secure" nutzen!
  // Accepted risk (not a bug): see checkStatus() above for the full rationale - the Pi's
  // adhoc-generated cert has no stable fingerprint to pin, so this is LAN-only trust.
  client.setInsecure();
  String url = String(PI_BASE_URL) + UPLOAD_ENDPOINT;

  http.begin(url);

  http.addHeader("X-Device-Token", DEVICE_TOKEN);
  http.addHeader("Content-Type", "image/jpeg");

  int httpCode = http.POST(fb->buf, fb->len);

  if (httpCode <= 0) {

    Serial.println("Upload Fehler");

    http.end();

    return false;
  }

  String response = http.getString();

  Serial.println(response);

  http.end();

  return true;
}


void setup() {

  Serial.begin(115200);

  delay(1000);

  if (!connectWiFi()) {
    deepSleep();
  }

  bool meeting = checkStatus();

  if (!meeting) {

    Serial.println("Kein Termin");

    WiFi.disconnect(true);

    deepSleep();
  }

  Serial.println("Termin aktiv");

  if (!initCamera()) {

    WiFi.disconnect(true);

    deepSleep();
  }

  delay(500);

  camera_fb_t* fb = esp_camera_fb_get();

  if (!fb) {

    Serial.println("Bild Fehler");

    esp_camera_deinit();

    WiFi.disconnect(true);

    deepSleep();
  }

  Serial.println("Bild aufgenommen");

  uploadImage(fb);

  esp_camera_fb_return(fb);

  esp_camera_deinit();

  WiFi.disconnect(true);

  deepSleep();
}


void loop() {
}