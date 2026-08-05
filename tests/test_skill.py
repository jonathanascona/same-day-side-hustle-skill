from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from install import install


class SkillTests(unittest.TestCase):
    def test_skill_metadata_name_is_valid(self) -> None:
        content = (ROOT / "side-hustle" / "SKILL.md").read_text(encoding="utf-8")
        marker = chr(45) * 3
        self.assertTrue(content.startswith(marker + "\n"))
        self.assertIn("name: side-hustle\n", content)

    def test_install_creates_claude_code_skill(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            target = Path(temp_dir) / "side-hustle"
            install(target, force=False)
            self.assertTrue((target / "SKILL.md").exists())
            self.assertTrue((target / "framework" / "scoring-model.md").exists())

    def test_web_archive_has_required_layout(self) -> None:
        subprocess.run([sys.executable, str(ROOT / "scripts" / "package_skill.py")], check=True)
        archive_path = ROOT / "dist" / "side-hustle.zip"
        with zipfile.ZipFile(archive_path) as archive:
            names = set(archive.namelist())
            self.assertIn("side-hustle/skill.md", names)
            skill_text = archive.read("side-hustle/skill.md").decode("utf-8")
            self.assertIn("name: side-hustle\n", skill_text)


if __name__ == "__main__":
    unittest.main()
