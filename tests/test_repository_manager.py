from src.repository.manager import RepositoryManager


def test_create_repository_manager():

    r = RepositoryManager(

        repository_root="repository"
    )

    assert str(
        r.repository_root
    ) == "repository"

from src.models.question import Question

def test_save_question(tmp_path):

    r = RepositoryManager(

        repository_root=tmp_path
    )

    q = Question(

        uuid="Q-a72f",

        label="Q1",

        question_type="single_choice",

        points=2,

        stem_tex="What is HCl?"
    )

    r.save_question(q)

    saved = (

        tmp_path
        / "questions"
        / "Q-a72f"
        / "question.json"
    )

    assert saved.exists()

def test_load_question(tmp_path):

    r = RepositoryManager(
        repository_root=tmp_path
    )

    q = Question(

        uuid="Q-a72f",

        label="Q1",

        question_type="single_choice",

        points=2,

        stem_tex="What is HCl?"
    )

    r.save_question(q)

    loaded = r.load_question(
        "Q-a72f"
    )

    assert loaded.uuid == q.uuid
    assert loaded.stem_tex == q.stem_tex

def test_update_index(tmp_path):

    r = RepositoryManager(
        repository_root=tmp_path
    )

    q = Question(

        uuid="Q-a72f",

        label="Q1",

        question_type="single_choice",

        points=2,

        stem_tex="What is HCl?"
    )

    r.save_question(q)

    index_file = (

        tmp_path
        / "index"
        / "repository_index.json"
    )

    assert index_file.exists()