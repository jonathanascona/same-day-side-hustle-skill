from __future__ import annotations

from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".json", ".toml"}
REQUIRED = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "side-hustle/SKILL.md",
    "side-hustle/framework/scoring-model.md",
    "side-hustle/framework/question-bank.md",
    "side-hustle/references/same-day-launch-rules.md",
    "side-hustle/references/business-models.md",
    "side-hustle/references/build-decision-tree.md",
    "scripts/install.py",
    "scripts/package_skill.py",
)


def text_files() -> list[Path]:
    result = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts or "dist" in path.parts or "__pycache__" in path.parts:
            continue
        if path.name in {"LICENSE", ".gitignore"} or path.suffix in TEXT_SUFFIXES:
            result.append(path)
    return result


def main() -> int:
    errors: list[str] = []

    for relative in REQUIRED:
        if not (ROOT / relative).exists():
            errors.append(f"Missing required path: {relative}")

    skill = ROOT / "side-hustle" / "SKILL.md"
    if skill.exists():
        text = skill.read_text(encoding="utf-8")
        marker = chr(45) * 3
        if not text.startswith(marker + "\n"):
            errors.append("SKILL.md is missing YAML frontmatter")
        if "name: side-hustle\n" not in text:
            errors.append("SKILL.md name must be side-hustle")
        if text.count(marker) != 2:
            errors.append("SKILL.md should contain exactly two metadata delimiters")

    forbidden = {
        "em dash character": chr(0x2014),
        "en dash character": chr(0x2013),
    }
    marker = chr(45) * 3

    for path in text_files():
        text = path.read_text(encoding="utf-8")
        for label, sequence in forbidden.items():
            if sequence in text:
                errors.append(f"{path.relative_to(ROOT)} contains {label}")
        if marker in text and path != skill:
            errors.append(f"{path.relative_to(ROOT)} contains three consecutive hyphens")
        if text and not text.endswith("\n"):
            errors.append(f"{path.relative_to(ROOT)} needs a final newline")

    web_zip = ROOT / "dist" / "side-hustle.zip"
    if web_zip.exists():
        with zipfile.ZipFile(web_zip) as archive:
            names = set(archive.namelist())
            if "side-hustle/skill.md" not in names:
                errors.append("Claude upload ZIP is missing side-hustle/skill.md")
            if any(name.startswith("side-hustle/side-hustle/") for name in names):
                errors.append("Claude upload ZIP has an extra nested folder")

    if errors:
        print("Repository checks failed:")
        for error in errors:
            print(f"  {error}")
        return 1

    print(f"Repository checks passed for {len(text_files())} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
