"""
Module Purpose
--------------

Render Question objects into LaTeX.

Responsibilities
----------------

- Render individual questions
- Render collections of questions

Important Notes
---------------

This module does not render full
exam templates.

Template composition belongs to
higher-level renderer services.
"""

from src.models.question import Question


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