"""
Module Purpose
--------------

Exam section model.

Responsibilities
----------------

Group exam question instances
under a common section.

Examples
--------

Section A
(2 points each)

Section B
(4 points each)
"""

from dataclasses import dataclass, field

from src.models.exam_question_instance import (
    ExamQuestionInstance,
)


@dataclass(slots=True)
class ExamSection:
    """
    Section within an exam.
    """

    title: str

    points_per_question: int

    question_instances: list[
        ExamQuestionInstance
    ] = field(default_factory=list)

    @property
    def question_count(self) -> int:
        """
        Number of questions.
        """

        return len(
            self.question_instances
        )

    @property
    def total_points(self) -> int:
        """
        Total section score.
        """

        return (
            self.points_per_question
            * self.question_count
        )

    @property
    def section_summary(self) -> str:
        """
        Human-readable section summary.
        """

        return (
            f"每題{self.points_per_question}分，"
            f"共{self.total_points}分"
        )

    def add_question(
        self,
        instance: ExamQuestionInstance,
    ) -> None:
        """
        Add a question instance.
        """

        self.question_instances.append(
            instance
        )