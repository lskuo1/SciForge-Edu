from pydantic import BaseModel, Field

from src.models.choice import Choice
from src.models.solution import Solution
from src.models.analysis import Analysis
from src.models.version import Version


class AssessmentStatistics(BaseModel):

    exam_id: str

    correct_rate: float | None = None

    difficulty_index: float | None = None

    discrimination_index: float | None = None

    sample_size: int | None = None


class Question(BaseModel):
    """
    Core Question Object.
    """

    uuid: str

    label: str

    question_type: str

    points: int = Field(
        ge=0
    )

    stem_tex: str

    choices: list[Choice] = Field(
        default_factory=list
    )

    solution: Solution | None = None

    analysis: Analysis | None = None

    statistics: list[AssessmentStatistics] = Field(
        default_factory=list
    )

    current_version: int = 1

    history: list[Version] = Field(
        default_factory=list
    )

    extra: dict = Field(
        default_factory=dict
    )