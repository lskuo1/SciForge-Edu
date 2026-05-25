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