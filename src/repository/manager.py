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

import json
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

        question_dir = (

                self.repository_root
                / "questions"
                / question.uuid
        )

        question_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        question_file = (
                question_dir
                / "question.json"
        )

        with open(
                question_file,
                "w",
                encoding="utf-8"
        ) as f:
            json.dump(

                question.model_dump(),

                f,

                ensure_ascii=False,

                indent=4,

                default=str
            )

    def load_question(
            self,
            uuid: str
    ) -> Question:

        """
        Load question from repository.
        """

        raise NotImplementedError()