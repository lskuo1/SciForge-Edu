from pathlib import Path

from src.renderer.export_manager import (
    ExportManager,
)


def test_create_bundle(
    tmp_path: Path,
) -> None:
    """
    Verify export bundle creation.
    """

    export_dir = (
        tmp_path
        / "exam_export"
    )

    manager = ExportManager()

    bundle = manager.create_bundle(
        export_dir
    )

    assert export_dir.exists()

    assert (
        export_dir
        / "assets"
    ).exists()

    assert (
        bundle.student_tex
        == export_dir
        / "student.tex"
    )