"""
usage.py

Purpose:
Track how questions are used across exams.

Responsibilities:

- Record exam usage history
- Prevent repeated questions
- Support popularity analysis
- Support future assessment analytics

Notes:

QuestionUsage stores usage metadata only.

It does NOT store question content.
"""


from datetime import date

from pydantic import BaseModel, Field


class UsageRecord(BaseModel):
    """
    Single usage event.
    """

    exam_id: str

    exam_date: date


class QuestionUsage(BaseModel):
    """
    Track usage history of one question.
    """

    uuid: str

    used_in: list[UsageRecord] = Field(
        default_factory=list
    )