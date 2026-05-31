"""
Module Purpose
--------------

Render ExamSection objects
into LaTeX section blocks.
"""

from src.models.exam_section import (
    ExamSection,
)


class SectionRenderer:
    """
    Render ExamSection objects.
    """

    def render(
        self,
        section: ExamSection,
    ) -> str:

        return (
            "\\section*{"
            f"每題{section.points_per_question}分，"
            f"共{section.total_points}分"
            "}\n"
        )