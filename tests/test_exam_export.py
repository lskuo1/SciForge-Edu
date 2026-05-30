from pathlib import Path

from src.models.question import Question
from src.workspace.exam_export import (
    ExamExport,
)


def test_export_exam(
    tmp_path: Path,
):

    exporter = ExamExport()

    exporter.export(
        questions=[
            Question(
                uuid="Q1",
                label="Q1",
                question_type="single_choice",
                points=5,
                stem_tex="Example",
            )
        ],
        template_text="""
[[ print_answers_config ]]
[[ questions_content ]]
""",
        metadata={},
        output_dir=tmp_path,
    )

    assert (
        tmp_path
        / "student.tex"
    ).exists()

    assert (
        tmp_path
        / "teacher.tex"
    ).exists()