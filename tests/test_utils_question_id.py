from src.models.choice import Choice
from src.utils.question_id import generate_question_id


def make_choices(entries):
    return [
        Choice(
            text_tex=text,
            is_correct=is_correct,
        )
        for text, is_correct in entries
    ]


def test_same_content_same_id():

    choices = make_choices(
        [
            ("A", True),
            ("B", False),
        ]
    )

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=choices,
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=choices,
    )

    assert id1 == id2


def test_different_stem_different_id():

    choices = make_choices(
        [
            ("A", True),
            ("B", False),
        ]
    )

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question A",
        choices=choices,
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question B",
        choices=choices,
    )

    assert id1 != id2


def test_different_choice_text_different_id():

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("A", True),
                ("B", False),
            ]
        ),
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("X", True),
                ("B", False),
            ]
        ),
    )

    assert id1 != id2


def test_different_correct_answer_different_id():

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("A", True),
                ("B", False),
            ]
        ),
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("A", False),
                ("B", True),
            ]
        ),
    )

    assert id1 != id2


def test_choice_order_does_not_affect_identity():

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("A", True),
                ("B", False),
                ("C", False),
                ("D", False),
            ]
        ),
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question",
        choices=make_choices(
            [
                ("C", False),
                ("A", True),
                ("D", False),
                ("B", False),
            ]
        ),
    )

    assert id1 == id2


def test_whitespace_normalization():

    id1 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question    Text",
        choices=make_choices(
            [
                ("A", True),
                ("B", False),
            ]
        ),
    )

    id2 = generate_question_id(
        question_type="single_choice",
        stem_tex="Question Text",
        choices=make_choices(
            [
                ("A", True),
                ("B", False),
            ]
        ),
    )

    assert id1 == id2