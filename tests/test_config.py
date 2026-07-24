import importlib
import os
import sys
import tempfile
import unittest
from pathlib import Path


class ConfigTests(unittest.TestCase):
    def test_dotenv_values_are_loaded(self):
        project_root = Path(__file__).resolve().parents[1]
        env_path = project_root / ".env"
        original_env = env_path.read_text(encoding="utf-8") if env_path.exists() else None
        original_device_token = os.environ.get("SMARTROOMWARDEN_DEVICE_TOKEN")
        original_google_credentials = os.environ.get("GOOGLE_CREDENTIALS_PATH")

        try:
            with env_path.open("w", encoding="utf-8") as handle:
                handle.write("SMARTROOMWARDEN_DEVICE_TOKEN=from-dotenv\n")
                handle.write("GOOGLE_CREDENTIALS_PATH=./tmp/example-creds.json\n")

            sys.path.insert(0, str(project_root / "src"))
            import config

            config = importlib.reload(config)

            self.assertEqual(config.DEVICE_TOKEN, "from-dotenv")
            self.assertEqual(config.GOOGLE_CREDENTIALS_PATH, (project_root / "tmp/example-creds.json").resolve())
        finally:
            if original_env is None:
                if env_path.exists():
                    env_path.unlink()
            else:
                env_path.write_text(original_env, encoding="utf-8")

            if original_device_token is None:
                os.environ.pop("SMARTROOMWARDEN_DEVICE_TOKEN", None)
            else:
                os.environ["SMARTROOMWARDEN_DEVICE_TOKEN"] = original_device_token

            if original_google_credentials is None:
                os.environ.pop("GOOGLE_CREDENTIALS_PATH", None)
            else:
                os.environ["GOOGLE_CREDENTIALS_PATH"] = original_google_credentials

            sys.modules.pop("config", None)

    def test_simulation_runtime_mode_loads_simulation_profile(self):
        project_root = Path(__file__).resolve().parents[1]
        env_path = project_root / ".env"
        simulation_env_path = project_root / ".env.simulation"
        original_env = env_path.read_text(encoding="utf-8") if env_path.exists() else None
        original_simulation_env = simulation_env_path.read_text(encoding="utf-8") if simulation_env_path.exists() else None
        original_runtime_mode = os.environ.get("SMARTROOMWARDEN_RUNTIME_MODE")
        original_device_token = os.environ.get("SMARTROOMWARDEN_DEVICE_TOKEN")

        try:
            with simulation_env_path.open("w", encoding="utf-8") as handle:
                handle.write("SMARTROOMWARDEN_RUNTIME_MODE=simulation\n")
                handle.write("SMARTROOMWARDEN_DEVICE_TOKEN=from-simulation-profile\n")

            os.environ["SMARTROOMWARDEN_RUNTIME_MODE"] = "simulation"
            sys.path.insert(0, str(project_root / "src"))
            import config

            config = importlib.reload(config)

            self.assertEqual(config.RUNTIME_MODE, "simulation")
            self.assertEqual(config.DEVICE_TOKEN, "from-simulation-profile")
        finally:
            if original_env is None:
                if env_path.exists():
                    env_path.unlink()
            else:
                env_path.write_text(original_env, encoding="utf-8")

            if original_simulation_env is None:
                if simulation_env_path.exists():
                    simulation_env_path.unlink()
            else:
                simulation_env_path.write_text(original_simulation_env, encoding="utf-8")

            if original_runtime_mode is None:
                os.environ.pop("SMARTROOMWARDEN_RUNTIME_MODE", None)
            else:
                os.environ["SMARTROOMWARDEN_RUNTIME_MODE"] = original_runtime_mode

            if original_device_token is None:
                os.environ.pop("SMARTROOMWARDEN_DEVICE_TOKEN", None)
            else:
                os.environ["SMARTROOMWARDEN_DEVICE_TOKEN"] = original_device_token

            sys.modules.pop("config", None)
