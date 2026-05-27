"""
index.py

Purpose:
Store searchable repository metadata projections.

Responsibilities:

- Support fast repository search
- Store lightweight query metadata
- Avoid loading complete Question objects
- Support future indexing expansion

Notes:

RepositoryIndex is a query projection layer.

RepositoryIndex does not contain
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

    chapter: str | None = None

    tags: list[str] = Field(
        default_factory=list
    )

    difficulty_level: int | None = Field(
        default=None,
        ge=1,
        le=5
    )

    source_path: str

    current_version: int = 1

    usage_count: int = Field(
        default=0,
        ge=0
    )
