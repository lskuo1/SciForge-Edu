from src.models.question import Question

from src.renderer.render_pipeline import (
    RenderPipeline,
)


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


def test_pipeline_assigns_namespaces():

    questions = [
        make_question(
            "Q1",
            "Question 1",
        ),
        make_question(
            "Q2",
            "Question 2",
        ),
    ]

    context = (
        RenderPipeline()
        .run(questions)
    )

    assert context.namespace_map == {
        "Q1": "q0001",
        "Q2": "q0002",
    }


def test_pipeline_rewrites_labels():

    questions = [
        make_question(
            "Q1",
            (
                r"\label{fig:acid}"
                "\n"
                r"\ref{fig:acid}"
            ),
        )
    ]

    context = (
        RenderPipeline()
        .run(questions)
    )

    rewritten = (
        context.questions[0]
    )

    assert (
        r"\label{q0001_fig_acid}"
        in rewritten.stem_tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in rewritten.stem_tex
    )


def test_pipeline_returns_context():

    questions = [
        make_question(
            "Q1",
            "Question",
        )
    ]

    context = (
        RenderPipeline()
        .run(questions)
    )

    assert len(
        context.questions
    ) == 1

    assert (
        context.namespace_map[
            "Q1"
        ]
        == "q0001"
    )