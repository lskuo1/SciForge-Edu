from src.models.question import Question
from src.renderer.namespace_assigner import (
    NamespaceAssigner,
)


def make_question(
    uuid: str,
):

    return Question(
        uuid=uuid,
        label=uuid,
        question_type="single_choice",
        points=1,
        stem_tex="Question",
    )


def test_assign_single_question():

    questions = [
        make_question("Q1")
    ]

    mapping = (
        NamespaceAssigner()
        .assign(questions)
    )

    assert mapping == {
        "Q1": "q0001",
    }


def test_assign_multiple_questions():

    questions = [
        make_question("Q1"),
        make_question("Q2"),
        make_question("Q3"),
    ]

    mapping = (
        NamespaceAssigner()
        .assign(questions)
    )

    assert mapping == {
        "Q1": "q0001",
        "Q2": "q0002",
        "Q3": "q0003",
    }


def test_preserve_input_order():

    questions = [
        make_question("B"),
        make_question("A"),
        make_question("C"),
    ]

    mapping = (
        NamespaceAssigner()
        .assign(questions)
    )

    assert mapping == {
        "B": "q0001",
        "A": "q0002",
        "C": "q0003",
    }


def test_empty_question_list():

    mapping = (
        NamespaceAssigner()
        .assign([])
    )

    assert mapping == {}


def test_namespace_format():

    questions = [
        make_question("Q1"),
        make_question("Q2"),
        make_question("Q3"),
        make_question("Q4"),
        make_question("Q5"),
    ]

    mapping = (
        NamespaceAssigner()
        .assign(questions)
    )

    assert mapping["Q1"] == "q0001"
    assert mapping["Q2"] == "q0002"
    assert mapping["Q3"] == "q0003"
    assert mapping["Q4"] == "q0004"
    assert mapping["Q5"] == "q0005"