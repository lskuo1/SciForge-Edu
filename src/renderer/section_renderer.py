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
            f"{section.section_summary}"
            "}\n"
        )