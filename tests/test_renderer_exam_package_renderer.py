from src.models.question import Question
from src.renderer.exam_package_renderer import (
    ExamPackageRenderer,
)


TEMPLATE = r"""
[[ print_answers_config ]]

School:
[[ school_name ]]

Questions:
[[ total_questions ]]

Score:
[[ total_score ]]

[[ questions_content ]]
"""


def test_render_student_tex():

    renderer = (
        ExamPackageRenderer(
            TEMPLATE
        )
    )

    tex = renderer.render_student_tex(
        questions=[
            Question(
                uuid="Q1",
                label="Q1",
                question_type="single_choice",
                points=5,
                stem_tex="Q1",
            )
        ],
        metadata={
            "school_name":
                "SciForge High",
        },
    )

    assert "\\noprintanswers" in tex

    assert "SciForge High" in tex

    assert "Questions:" in tex

    assert "1" in tex


def test_render_teacher_tex():

    renderer = (
        ExamPackageRenderer(
            TEMPLATE
        )
    )

    tex = renderer.render_teacher_tex(
        questions=[
            Question(
                uuid="Q1",
                label="Q1",
                question_type="single_choice",
                points=5,
                stem_tex="Q1",
            )
        ],
        metadata={
            "school_name":
                "SciForge High",
        },
    )

    assert "\\printanswers" in tex

def test_render_without_sections():

    renderer = ExamPackageRenderer(
        TEMPLATE
    )

    tex = renderer.render_student_tex(
        questions=[
            Question(
                uuid="Q1",
                label="Q1",
                question_type="single_choice",
                points=2,
                stem_tex="Q1",
            ),
            Question(
                uuid="Q2",
                label="Q2",
                question_type="single_choice",
                points=2,
                stem_tex="Q2",
            ),
        ],
        metadata={
            "school_name":
                "SciForge High",
        },
    )

    assert "\\section*" not in tex


def test_render_with_sections():

    renderer = ExamPackageRenderer(
        TEMPLATE
    )

    tex = renderer.render_student_tex(
        questions=[
            Question(
                uuid="Q1",
                label="Q1",
                question_type="single_choice",
                points=2,
                stem_tex="Q1",
            ),
            Question(
                uuid="Q2",
                label="Q2",
                question_type="single_choice",
                points=4,
                stem_tex="Q2",
            ),
        ],
        metadata={
            "school_name":
                "SciForge High",
        },
    )

    assert "\\section*" in tex

    assert (
        "每題2分"
        in tex
    )

    assert (
        "每題4分"
        in tex
    )