"""
index.py

Purpose:
Store repository search entries.

Responsibilities:

- Support fast question search
- Store metadata
- Avoid loading complete questions

Notes:

Repository index does not contain
complete question content.
"""


from pydantic import BaseModel, Field


class RepositoryIndex(BaseModel):
    """
    Repository search/index entry.
    """

    uuid: str

    label: str

    question_type: str

    subject: str | None = None

    tags: list[str] = Field(
        default_factory=list
    )

    source_path: str

    current_version: int = 1

    usage_count: int = Field(
        default=0,
        ge=0
    )