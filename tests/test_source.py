from src.models.source import Source


def test_create_source():

    s = Source(

        file_path="questions/q001/question.tex",

        raw_tex=r"\question What is HCl?"
    )

    assert s.file_path == "questions/q001/question.tex"

    assert "HCl" in s.raw_tex