from src.models.analysis import Analysis


def test_create_analysis():

    a = Analysis(

        difficulty_score=0.7,

        difficulty_level=4,

        subject="Physics",

        chapter="Friction",

        tags=["force","motion"]
    )

    assert a.difficulty_score == 0.7

    assert a.difficulty_level == 4

    assert "force" in a.tags


def test_default_lists():

    a = Analysis()

    assert a.tags == []

    assert a.misconceptions == []