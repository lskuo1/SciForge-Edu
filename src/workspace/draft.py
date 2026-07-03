"""
draft.py

Purpose:
Store unfinished exam workspace state.

Responsibilities:

- Save unfinished exam drafts
- Preserve selected questions
- Preserve exam settings
- Support resume workflow

Notes:

WorkspaceDraft is temporary working data.

It is not a finalized Exam.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class WorkspaceDraft(BaseModel):
    """
    Unfinished workspace state.
    """

    draft_id: str

    title: str

    selected_questions: list[str] = Field(
        default_factory=list
    )

    settings: dict = Field(
        default_factory=dict
    )

    last_modified: datetime = Field(
        default_factory=datetime.now
    )