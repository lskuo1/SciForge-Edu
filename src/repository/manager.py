"""
manager.py

Purpose:
Manage repository operations.

Responsibilities:

- Save questions
- Load questions
- Update repository index
- Support future search functions

Notes:

RepositoryManager operates on storage layer.

Storage structure is defined in:

docs/draft/repository_storage_spec_v0.1.md
"""

from pathlib import Path

from src.models.question import Question


class RepositoryManager:
    """
    Repository operation manager.
    """

    def __init__(self, repository_root: str):

        self.repository_root = Path(
            repository_root
        )

    def save_question(
            self,
            question: Question
    ):

        """
        Save question into repository.

        TODO:
        - create question folder
        - serialize question
        - update index
        """

        raise NotImplementedError()

    def load_question(
            self,
            uuid: str
    ) -> Question:

        """
        Load question from repository.
        """

        raise NotImplementedError()