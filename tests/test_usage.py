from src.repository.usage import QuestionUsage


def test_create_usage():

    u = QuestionUsage(

        uuid="Q-a72f"
    )

    assert u.uuid == "Q-a72f"

    assert u.used_in == []