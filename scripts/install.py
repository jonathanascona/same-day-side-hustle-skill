from __future__ import annotations

import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "side-hustle"
DEFAULT_TARGET = Path.home() / ".claude" / "skills" / "side-hustle"


def install(target: Path, force: bool) -> Path:
    if not (SOURCE / "SKILL.md").exists():
        raise FileNotFoundError(f"Skill source not found: {SOURCE}")

    if target.exists() and any(target.iterdir()) and not force:
        raise FileExistsError(
            f"Target is not empty: {target}. Run again with --force to replace it."
        )

    if target.exists() and force:
        shutil.rmtree(target)

    shutil.copytree(SOURCE, target)
    return target


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Install the side-hustle skill")
    parser.add_argument(
        "--target",
        type=Path,
        default=DEFAULT_TARGET,
        help=f"Install destination. Default: {DEFAULT_TARGET}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing nonempty installation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target = install(args.target.expanduser().resolve(), args.force)
    print(f"Installed side-hustle to {target}")
    print("Open Claude Code and run /skills, then invoke /side-hustle.")


if __name__ == "__main__":
    main()
