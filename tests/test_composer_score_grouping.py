from src.composer.score_grouping import (
    group_by_points,
)
from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.question import Question


def create_instance(
    assigned_points: int,
) -> ExamQuestionInstance:

    question = Question(
        uuid="Q",
        label="Q",
        question_type="single_choice",
        points=1,
        stem_tex="Example",
    )

    return ExamQuestionInstance(
        question=question,
        assigned_points=assigned_points,
    )


def test_group_by_points():

    instances = [
        create_instance(2),
        create_instance(2),
        create_instance(4),
        create_instance(2),
    ]

    sections = group_by_points(
        instances
    )

    assert len(
        sections
    ) == 2

    assert (
        sections[0]
        .points_per_question
        == 2
    )

    assert (
        sections[0]
        .question_count
        == 3
    )

    assert (
        sections[1]
        .points_per_question
        == 4
    )

    assert (
        sections[1]
        .question_count
        == 1
    )