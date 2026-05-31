"""
Module Purpose
--------------

Exam-specific question instance.

Responsibilities
----------------

Represent a Question used within
a specific examination.

This layer owns exam composition
settings and must not modify the
source Question object.
"""

from dataclasses import dataclass

from src.models.question import Question


@dataclass(slots=True)
class ExamQuestionInstance:
    """
    Question instance inside an exam.
    """

    question: Question

    assigned_points: int | None = None

    display_order: int = 0

    included: bool = True

    paper_version: str = "A"

    @property
    def effective_points(self) -> int:
        """
        Effective score used during
        rendering.
        """

        if self.assigned_points is not None:
            return self.assigned_points

        return self.question.points