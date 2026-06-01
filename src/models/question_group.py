"""
question_group.py

Purpose:
Define QuestionGroup objects.

Responsibilities:

- Store shared group material
- Store child questions
- Preserve group-level metadata

Notes:

QuestionGroup is not a Question.

QuestionGroup acts as a container
for multiple Question objects.
"""

from pydantic import BaseModel, Field

from src.models.question import Question


class QuestionGroup(BaseModel):
    """
    Shared-stimulus question group.
    """

    group_stem_tex: str | None = None

    boxed_stem: bool = False

    questions: list[Question] = Field(
        min_length=1
    )

    extra: dict = Field(
        default_factory=dict
    )