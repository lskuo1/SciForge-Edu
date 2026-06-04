from src.models.question import Question

from src.renderer.exam_render_service import (
    ExamRenderService,
)


TEMPLATE = r"""
[[ print_answers_config ]]

[[ questions_content ]]
"""


def make_question(
    uuid: str,
    stem_tex: str,
):

    return Question(
        uuid=uuid,
        label=uuid,
        question_type="single_choice",
        points=1,
        stem_tex=stem_tex,
    )


def test_student_render_uses_pipeline():

    service = ExamRenderService(
        TEMPLATE
    )

    tex = service.render_student_tex(
        questions=[
            make_question(
                "Q1",
                (
                    r"\label{fig:acid}"
                    "\n"
                    r"\ref{fig:acid}"
                ),
            )
        ],
        metadata={},
    )

    assert (
        r"\label{q0001_fig_acid}"
        in tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in tex
    )

    assert (
        "\\noprintanswers"
        in tex
    )


def test_teacher_render_uses_pipeline():

    service = ExamRenderService(
        TEMPLATE
    )

    tex = service.render_teacher_tex(
        questions=[
            make_question(
                "Q1",
                (
                    r"\label{fig:acid}"
                    "\n"
                    r"\ref{fig:acid}"
                ),
            )
        ],
        metadata={},
    )

    assert (
        r"\label{q0001_fig_acid}"
        in tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in tex
    )

    assert (
        "\\printanswers"
        in tex
    )


def test_multiple_questions():

    service = ExamRenderService(
        TEMPLATE
    )

    tex = service.render_student_tex(
        questions=[
            make_question(
                "Q1",
                r"\label{fig:a}",
            ),
            make_question(
                "Q2",
                r"\label{fig:b}",
            ),
        ],
        metadata={},
    )

    assert (
        r"\label{q0001_fig_a}"
        in tex
    )

    assert (
        r"\label{q0002_fig_b}"
        in tex
    )