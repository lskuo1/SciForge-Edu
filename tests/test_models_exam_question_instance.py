from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.question import Question


def create_question(
    points: int,
) -> Question:

    return Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=points,
        stem_tex="Example",
    )


def test_use_default_points():

    question = create_question(
        points=2,
    )

    instance = (
        ExamQuestionInstance(
            question=question,
        )
    )

    assert (
        instance.effective_points
        == 2
    )


def test_override_points():

    question = create_question(
        points=2,
    )

    instance = (
        ExamQuestionInstance(
            question=question,
            assigned_points=5,
        )
    )

    assert (
        instance.effective_points
        == 5
    )


def test_question_not_modified():

    question = create_question(
        points=2,
    )

    instance = (
        ExamQuestionInstance(
            question=question,
            assigned_points=7,
        )
    )

    assert (
        instance.effective_points
        == 7
    )

    assert (
        question.points
        == 2
    )
