import importlib.util
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock


def load_vision_module():
    project_root = Path(__file__).resolve().parents[1]
    module_path = project_root / "src" / "ki_zeugs" / "vision_mock.py"
    spec = importlib.util.spec_from_file_location("vision_mock", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load module from {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules["vision_mock"] = module
    spec.loader.exec_module(module)
    return module


vision_mock = load_vision_module()


class VisionMockTests(unittest.TestCase):
    def test_check_raum_status_returns_false_for_invalid_image_bytes(self):
        self.assertFalse(vision_mock.check_raum_status(b"not-a-valid-image"))

    def test_check_raum_status_returns_true_when_model_detects_person(self):
        fake_model = Mock(return_value=[SimpleNamespace(boxes=[SimpleNamespace(cls=[0])])])
        vision_mock.get_model = Mock(return_value=fake_model)

        image_bytes = b"\xff\xd8\xff"  # minimal JPEG header bytes, still invalid for decoding but should not matter because we patch decode?

        with unittest.mock.patch("cv2.imdecode", return_value=SimpleNamespace()):
            self.assertTrue(vision_mock.check_raum_status(image_bytes))
