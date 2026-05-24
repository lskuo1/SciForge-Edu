"""
choice.py

Purpose:
Define choice objects for questions.

Responsibilities:

- Store option content
- Store answer correctness

Notes:

Choice labels (A/B/C/D) belong to
presentation layer, not data layer.
"""


from pydantic import BaseModel


class Choice(BaseModel):
    """
    Multiple-choice option.
    """

    text_tex: str

    is_correct: bool = False

    explanation: str | None = None