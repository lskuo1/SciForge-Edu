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