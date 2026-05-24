from src.models.choice import Choice
from src.models.question import Question


def test_create_question():

    q = Question(

        uuid="Q-a72f",

        label="Q1",

        question_type="single_choice",

        points=2,

        stem_tex="Which is acid?",

        choices=[

            Choice(
                text_tex="HCl",
                is_correct=True
            ),

            Choice(
                text_tex="NaOH"
            )
        ]
    )

    assert q.uuid == "Q-a72f"

    assert len(q.choices) == 2

    assert q.points == 2


def test_default_fields():

    q = Question(

        uuid="Q-test",

        label="Q2",

        question_type="single_choice",

        points=1,

        stem_tex="test"
    )

    assert q.choices == []

    assert q.history == []

    assert q.statistics == []