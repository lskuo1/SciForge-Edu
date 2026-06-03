from pathlib import Path

from src.models.choice import Choice
from src.models.question import Question
from src.renderer.resource_collector import (
    ResourceCollector,
)


def test_collect_same_directory_resource(
    tmp_path: Path,
):

    image = (
        tmp_path
        / "acid.png"
    )

    image.write_bytes(
        b"fake"
    )

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=(
            r"\includegraphics"
            r"{acid.png}"
        ),
        source_path=str(
            tmp_path
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert (
        resources[0].resolved_path
        == image.resolve()
    )

    assert resources[0].exists


def test_collect_subdirectory_resource(
    tmp_path: Path,
):

    images = (
        tmp_path
        / "images"
    )

    images.mkdir()

    image = (
        images
        / "acid.png"
    )

    image.write_bytes(
        b"fake"
    )

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=(
            r"\includegraphics"
            r"{images/acid.png}"
        ),
        source_path=str(
            tmp_path
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert (
        resources[0].resolved_path
        == image.resolve()
    )


def test_collect_parent_directory_resource(
    tmp_path: Path,
):

    questions = (
        tmp_path
        / "questions"
    )

    questions.mkdir()

    shared = (
        tmp_path
        / "shared"
    )

    shared.mkdir()

    image = (
        shared
        / "acid.png"
    )

    image.write_bytes(
        b"fake"
    )

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=(
            r"\includegraphics"
            r"{../shared/acid.png}"
        ),
        source_path=str(
            questions
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert (
        resources[0].resolved_path
        == image.resolve()
    )


def test_missing_resource(
    tmp_path: Path,
):

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=(
            r"\includegraphics"
            r"{missing.png}"
        ),
        source_path=str(
            tmp_path
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert (
        resources[0].exists
        is False
    )


def test_collect_resource_from_choice(
    tmp_path: Path,
):

    image = (
        tmp_path
        / "choice.png"
    )

    image.write_bytes(
        b"fake"
    )

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex="Question",
        choices=[
            Choice(
                text_tex=(
                    r"\includegraphics"
                    r"{choice.png}"
                ),
                is_correct=True,
            )
        ],
        source_path=str(
            tmp_path
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert resources[0].exists


def test_collect_includegraphics_with_options(
    tmp_path: Path,
):

    image = (
        tmp_path
        / "acid.png"
    )

    image.write_bytes(
        b"fake"
    )

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex=(
            r"\includegraphics"
            r"[width=5cm]"
            r"{acid.png}"
        ),
        source_path=str(
            tmp_path
            / "chapter1.tex"
        ),
    )

    collector = (
        ResourceCollector()
    )

    resources = collector.collect(
        question
    )

    assert len(resources) == 1

    assert (
        resources[0].question_uuid
        == "Q1"
    )

    assert resources[0].exists