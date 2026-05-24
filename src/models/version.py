"""
version.py

Purpose:
Track question version history.

Responsibilities:

- Record version number
- Record modification time
- Preserve change descriptions

Notes:

Question UUID remains unchanged across versions.
"""


from datetime import datetime
from pydantic import BaseModel, Field


class Version(BaseModel):
    """
    Question version information.
    """

    version: int = Field(
        ge=1
    )

    timestamp: datetime = Field(
        default_factory=datetime.now
    )

    author: str

    change_note: str