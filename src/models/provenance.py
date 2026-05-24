from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


SourceType = Literal[
    "teacher",
    "ai",
    "publisher",
    "imported",
    "system",
    "edited",
    "template_extractor"
]


class Revision(BaseModel):
    """
    Record modification history.
    """

    timestamp: datetime = Field(
        default_factory=datetime.now
    )

    editor: str

    editor_type: str

    note: str | None = None


class Provenance(BaseModel):
    """
    Track where content originates.
    """

    source_type: SourceType

    source_name: str

    created_by: str

    created_at: datetime = Field(
        default_factory=datetime.now
    )

    based_on: str | None = None

    model_version: str | None = None

    confidence: float | None = Field(
        default=None,
        ge=0,
        le=1
    )

    note: str | None = None

    revision_history: list[Revision] = Field(
        default_factory=list
    )