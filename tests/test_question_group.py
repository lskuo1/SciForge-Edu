from src.models.choice import Choice
from src.models.question import Question
from src.models.question_group import (
    QuestionGroup,
)


def test_question_group_creation() -> None:
    """
    Verify QuestionGroup construction.
    """

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=2,
        stem_tex="Example",
        choices=[
            Choice(
                text_tex="A"
            )
        ],
    )

    group = QuestionGroup(
        group_stem_tex="Shared material",
        boxed_stem=True,
        questions=[
            question
        ],
    )

    assert (
        group.group_stem_tex
        == "Shared material"
    )

    assert group.boxed_stem is True

    assert len(group.questions) == 1