"""
Module Purpose
--------------

Render Question objects into LaTeX.

Responsibilities
----------------

- Render individual questions
- Render collections of questions
- Render exam sections

Important Notes
---------------

This module does not render full
exam templates.

Template composition belongs to
higher-level renderer services.
"""

from src.models.exam_section import (
    ExamSection,
)
from src.models.question import Question
from src.renderer.section_renderer import (
    SectionRenderer,
)


class ExamRenderer:
    """
    Render Question objects into LaTeX.
    """

    def render_question(
        self,
        question: Question,
    ) -> str:
        """
        Render a single Question.
        """

        lines: list[str] = []

        lines.append(
            f"\\question {question.stem_tex}"
        )

        if question.choices:

            lines.append("")
            lines.append(
                "\\begin{choices}"
            )

            for choice in question.choices:

                command = (
                    "\\CorrectChoice"
                    if choice.is_correct
                    else "\\choice"
                )

                lines.append(
                    f"{command} "
                    f"{choice.text_tex}"
                )

            lines.append(
                "\\end{choices}"
            )

        if question.solution:

            lines.append("")
            lines.append(
                "\\begin{solution}"
            )

            lines.append(
                question.solution.content_tex
            )

            lines.append(
                "\\end{solution}"
            )

        return "\n".join(lines)

    def render_questions(
        self,
        questions: list[Question],
    ) -> str:
        """
        Render multiple questions.
        """

        return "\n\n".join(
            self.render_question(q)
            for q in questions
        )

    def render_section(
        self,
        section: ExamSection,
    ) -> str:
        """
        Render an ExamSection.
        """

        section_renderer = (
            SectionRenderer()
        )

        lines = [
            section_renderer.render(
                section
            )
        ]

        for instance in (
            section.question_instances
        ):

            lines.append(
                self.render_question(
                    instance.question
                )
            )

        return "\n\n".join(
            lines
        )

    def render_sections(
        self,
        sections: list[ExamSection],
    ) -> str:
        """
        Render multiple sections.
        """

        return "\n\n".join(
            self.render_section(
                section
            )
            for section in sections
        )