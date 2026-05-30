from pathlib import Path

from src.renderer.output_bundle import (
    OutputBundle,
)


def test_output_bundle() -> None:
    """
    Verify OutputBundle construction.
    """

    bundle = OutputBundle(
        student_tex=Path("student.tex"),
        teacher_tex=Path("teacher.tex"),
        answer_table_tex=Path(
            "answer_table.tex"
        ),
    )

    assert (
        bundle.student_tex
        == Path("student.tex")
    )

    assert (
        bundle.teacher_tex
        == Path("teacher.tex")
    )

    assert (
        bundle.answer_table_tex
        == Path("answer_table.tex")
    )
