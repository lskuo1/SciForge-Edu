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
from src.repository.index import RepositoryIndex


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

        - update repository index
        - create usage file
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
        self.update_index(
            question
        )

    def load_question(
            self,
            uuid: str
    ) -> Question:

        """
        Load question from repository.
        """

        question_file = (

                self.repository_root
                / "questions"
                / uuid
                / "question.json"
        )

        with open(
                question_file,
                "r",
                encoding="utf-8"
        ) as f:
            data = json.load(f)

        return Question(
            **data
        )

    def update_index(
            self,
            question: Question
    ):
        """
        Update repository index.
        """

        index_dir = (

                self.repository_root
                / "index"
        )

        index_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        index_file = (
                index_dir
                / "repository_index.json"
        )

        entries = []

        if index_file.exists():
            with open(
                    index_file,
                    "r",
                    encoding="utf-8"
            ) as f:
                entries = json.load(f)

        index_entry = RepositoryIndex(

            uuid=question.uuid,

            label=question.label,

            question_type=question.question_type,

            source_path=(
                f"questions/{question.uuid}"
            )
        )

        entries = [

            e
            for e in entries
            if e["uuid"] != question.uuid
        ]

        entries.append(
            index_entry.model_dump()
        )

        with open(
                index_file,
                "w",
                encoding="utf-8"
        ) as f:
            json.dump(

                entries,

                f,

                ensure_ascii=False,

                indent=4
            )