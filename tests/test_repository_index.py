from src.repository.index import RepositoryIndex


def test_create_repository_index():

    r = RepositoryIndex(

        uuid="Q-a72f",

        label="Q1",

        question_type="single_choice",

        subject="Physics",

        tags=["force"],

        source_path="repository/q_a72f.json"
    )

    assert r.uuid == "Q-a72f"

    assert r.current_version == 1


def test_default_values():

    r = RepositoryIndex(

        uuid="Q-test",

        label="Q2",

        question_type="single_choice",

        source_path="repository/test.json"
    )

    assert r.tags == []

    assert r.usage_count == 0