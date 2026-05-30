from pathlib import Path

from src.renderer.output_bundle import (
    OutputBundle,
)


def test_output_bundle() -> None:
    """
    Verify OutputBundle construction.
    """

    bundle = OutputBundle(
        export_dir=Path("export"),
        assets_dir=Path("export/assets"),
        student_tex=Path("export/student.tex"),
        teacher_tex=Path("export/teacher.tex"),
        answer_table_tex=Path(
            "export/answer_table.tex"
        ),
    )

    assert bundle.export_dir == Path("export")

    assert (
        bundle.assets_dir
        == Path("export/assets")
    )

    assert (
        bundle.student_tex
        == Path("export/student.tex")
    )