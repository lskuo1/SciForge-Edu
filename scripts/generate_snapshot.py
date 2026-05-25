"""
generate_snapshot.py

Purpose:
Generate project API snapshots for AI collaboration.

Responsibilities:

- Generate API snapshot
- Save generated snapshot
- Update official snapshot only if changed

Important notes:

- API snapshot is the source of truth for AI context
- Snapshot is automatically updated by pre-commit
- Generated files should not always trigger commits
"""

from pathlib import Path


def generate_snapshot():

    project_root = Path(__file__).resolve().parent.parent

    generated_dir = (
        project_root
        / "docs"
        / ".generated"
    )

    generated_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    generated_file = (
        generated_dir
        / "api_snapshot.md"
    )

    official_file = (
        project_root
        / "docs"
        / "api_snapshot.md"
    )

    content = """# SciForge API Snapshot

Snapshot version: 0.1

Status:
Initial placeholder
"""

    generated_file.write_text(
        content,
        encoding="utf-8"
    )

    old_content = ""

    if official_file.exists():
        old_content = official_file.read_text(
            encoding="utf-8"
        )

    if old_content != content:
        official_file.write_text(
            content,
            encoding="utf-8"
        )


def main():
    generate_snapshot()


if __name__ == "__main__":
    main()