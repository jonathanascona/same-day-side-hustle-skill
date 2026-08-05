from __future__ import annotations

from pathlib import Path
import shutil
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "side-hustle"
DIST = ROOT / "dist"
CLAUDE_ARCHIVE = DIST / "side-hustle.zip"
CLAUDE_CODE_ARCHIVE = DIST / "side-hustle-claude-code.zip"


def write_archive(source: Path, archive_path: Path, web_format: bool) -> None:
    if archive_path.exists():
        archive_path.unlink()

    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(source)
            if web_format and relative == Path("SKILL.md"):
                relative = Path("skill.md")
            archive.write(path, Path("side-hustle") / relative)


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    write_archive(SOURCE, CLAUDE_ARCHIVE, web_format=True)
    write_archive(SOURCE, CLAUDE_CODE_ARCHIVE, web_format=False)
    print(f"Created {CLAUDE_ARCHIVE}")
    print(f"Created {CLAUDE_CODE_ARCHIVE}")


if __name__ == "__main__":
    main()
