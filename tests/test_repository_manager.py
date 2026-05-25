from src.repository.manager import RepositoryManager


def test_create_repository_manager():

    r = RepositoryManager(

        repository_root="repository"
    )

    assert str(
        r.repository_root
    ) == "repository"