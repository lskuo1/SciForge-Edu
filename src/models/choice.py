from pydantic import BaseModel, Field


class Choice(BaseModel):
    """
    Multiple-choice option.
    """

    label: str = Field(
        min_length=1,
        max_length=5
    )

    text_tex: str

    is_correct: bool = False

    explanation: str | None = None