from src.parser.question_parser import (
    QuestionParser
)


def test_parse_question():

    parser = QuestionParser()

    q = parser.parse(

        r"\question What is HCl?"
    )

    assert (

        q.stem_tex
        ==
        "What is HCl?"
    )


def test_missing_question():

    parser = QuestionParser()

    try:

        parser.parse(
            "hello"
        )

        assert False

    except ValueError:

        assert True

def test_parse_choices():

    parser = QuestionParser()

    q = parser.parse(

        r"""
        \question Which is acid?

        \choice HCl
        \choice NaOH
        \choice CO2
        """
    )

    assert len(
        q.choices
    ) == 3

    assert (

        q.choices[0].text_tex
        ==
        "HCl"
    )