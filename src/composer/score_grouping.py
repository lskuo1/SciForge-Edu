"""
Module Purpose
--------------

Group exam question instances
by assigned points.
"""

from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.exam_section import (
    ExamSection,
)


def group_by_points(
    instances: list[ExamQuestionInstance],
) -> list[ExamSection]:
    """
    Group question instances by
    effective points.
    """

    groups: dict[
        int,
        list[ExamQuestionInstance]
    ] = {}

    for instance in instances:

        points = (
            instance.effective_points
        )

        groups.setdefault(
            points,
            [],
        ).append(
            instance
        )

    sections: list[
        ExamSection
    ] = []

    for points in sorted(
        groups.keys()
    ):

        section = ExamSection(
            title=f"{points} Points",
            points_per_question=points,
        )

        section.question_instances.extend(
            groups[points]
        )

        sections.append(
            section
        )

    return sections