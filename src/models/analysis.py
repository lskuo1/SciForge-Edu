"""
analysis.py

Purpose:
Store question analysis metadata.

Responsibilities:

- Store estimated difficulty
- Store chapter and tags
- Store misconceptions
- Preserve analysis provenance

Notes:

Analysis contains intrinsic question properties.

Observed exam statistics belong elsewhere.
"""


from pydantic import BaseModel, Field
from src.models.provenance import Provenance

class Analysis(BaseModel):
    """
    Question analysis metadata.
    """

    difficulty_score: float | None = Field(
        default=None,
        ge=0,
        le=1
    )

    difficulty_level: int | None = Field(
        default=None,
        ge=1,
        le=5
    )

    subject: str | None = None

    chapter: str | None = None

    tags: list[str] = Field(
        default_factory=list
    )

    misconceptions: list[str] = Field(
        default_factory=list
    )

    provenance: Provenance | None = None