from pydantic import BaseModel


class Choice(BaseModel):
    """
    Multiple-choice option.
    """

    text_tex: str

    is_correct: bool = False

    explanation: str | None = None