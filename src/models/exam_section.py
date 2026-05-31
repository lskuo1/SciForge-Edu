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

    points_per_question: int | float

    question_instances: list[
        ExamQuestionInstance
    ] = field(default_factory=list)

    @staticmethod
    def _format_score(
        score: int | float,
    ) -> str:
        """
        Format score for display.

        Examples
        --------

        2.0 -> "2"

        2.5 -> "2.5"
        """

        if float(score).is_integer():

            return str(
                int(score)
            )

        return str(score)

    @property
    def question_count(self) -> int:
        """
        Number of questions.
        """

        return len(
            self.question_instances
        )

    @property
    def total_points(
        self,
    ) -> int | float:
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

        points = (
            self._format_score(
                self.points_per_question
            )
        )

        total = (
            self._format_score(
                self.total_points
            )
        )

        return (
            f"每題{points}分，"
            f"共{total}分"
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