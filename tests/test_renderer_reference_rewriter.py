from src.models.choice import Choice
from src.models.question import Question
from src.models.solution import Solution
from src.renderer.reference_rewriter import (
    ReferenceRewriter,
)
from src.models.provenance import Provenance


def make_question(
    stem_tex: str,
    choices=None,
    solution=None,
):

    return Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=stem_tex,
        choices=choices or [],
        solution=solution,
    )


def test_rewrite_label():

    question = make_question(
        r"\label{fig:acid}"
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        rewritten.stem_tex
        == r"\label{q0001_fig_acid}"
    )


def test_rewrite_label_and_ref():

    question = make_question(
        (
            r"\label{fig:acid}"
            "\n"
            r"\ref{fig:acid}"
        )
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\label{q0001_fig_acid}"
        in rewritten.stem_tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in rewritten.stem_tex
    )


def test_rewrite_pageref():

    question = make_question(
        (
            r"\label{fig:acid}"
            "\n"
            r"\pageref{fig:acid}"
        )
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\pageref{q0001_fig_acid}"
        in rewritten.stem_tex
    )


def test_rewrite_autoref():

    question = make_question(
        (
            r"\label{fig:acid}"
            "\n"
            r"\autoref{fig:acid}"
        )
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\autoref{q0001_fig_acid}"
        in rewritten.stem_tex
    )


def test_rewrite_eqref():

    question = make_question(
        (
            r"\label{eq:newton}"
            "\n"
            r"\eqref{eq:newton}"
        )
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\eqref{q0001_eq_newton}"
        in rewritten.stem_tex
    )


def test_rewrite_choice_text():

    question = make_question(
        "Question",
        choices=[
            Choice(
                text_tex=(
                    r"\label{fig:acid}"
                    "\n"
                    r"\ref{fig:acid}"
                ),
                is_correct=True,
            )
        ],
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\label{q0001_fig_acid}"
        in rewritten.choices[0].text_tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in rewritten.choices[0].text_tex
    )


def test_rewrite_solution_content():

    provenance = Provenance(
        source_type="teacher",
        source_name="Teacher",
        created_by="Long-Sheng",
    )

    question = make_question(
        "Question",
        solution=Solution(
            content_tex=(
                r"\label{fig:acid}"
                "\n"
                r"\ref{fig:acid}"
            ),
            provenance=provenance,
        ),
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\label{q0001_fig_acid}"
        in rewritten.solution.content_tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in rewritten.solution.content_tex
    )


def test_label_normalization():

    question = make_question(
        r"\label{eq:newton}"
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        rewritten.stem_tex
        == r"\label{q0001_eq_newton}"
    )


def test_missing_reference_is_allowed():

    question = make_question(
        r"\ref{missing}"
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        rewritten.stem_tex
        == r"\ref{missing}"
    )


def test_multiple_labels():

    question = make_question(
        (
            r"\label{fig:acid}"
            "\n"
            r"\label{eq:newton}"
            "\n"
            r"\ref{fig:acid}"
            "\n"
            r"\eqref{eq:newton}"
        )
    )

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        r"\label{q0001_fig_acid}"
        in rewritten.stem_tex
    )

    assert (
        r"\label{q0001_eq_newton}"
        in rewritten.stem_tex
    )

    assert (
        r"\ref{q0001_fig_acid}"
        in rewritten.stem_tex
    )

    assert (
        r"\eqref{q0001_eq_newton}"
        in rewritten.stem_tex
    )


def test_original_question_not_modified():

    question = make_question(
        r"\label{fig:acid}"
    )

    original = question.stem_tex

    rewritten = (
        ReferenceRewriter()
        .rewrite(
            question,
            render_id="q0001",
        )
    )

    assert (
        question.stem_tex
        == original
    )

    assert (
        rewritten.stem_tex
        != original
    )