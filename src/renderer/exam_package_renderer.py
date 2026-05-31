"""
Module Purpose
--------------

Render complete exam packages using
legacy templates.

Responsibilities
----------------

- Build student.tex
- Build teacher.tex
- Inject rendered questions
"""

from src.composer.score_grouping import (
    group_by_points,
)
from src.models.question import Question
from src.renderer.exam_renderer import (
    ExamRenderer,
)


class ExamPackageRenderer:
    """
    Build complete exam documents.
    """

    def __init__(
        self,
        template_text: str,
    ) -> None:
        self._template = template_text

        self._question_renderer = (
            ExamRenderer()
        )

    def render_student_tex(
        self,
        questions: list[Question],
        metadata: dict[str, str],
    ) -> str:

        return self._render(
            questions=questions,
            metadata=metadata,
            print_answers=False,
        )

    def render_teacher_tex(
        self,
        questions: list[Question],
        metadata: dict[str, str],
    ) -> str:

        return self._render(
            questions=questions,
            metadata=metadata,
            print_answers=True,
        )

    def _render(
        self,
        questions: list[Question],
        metadata: dict[str, str],
        print_answers: bool,
    ) -> str:

        unique_points = {
            q.points
            for q in questions
        }

        if len(unique_points) <= 1:

            content = (
                self._question_renderer
                .render_questions(
                    questions
                )
            )

        else:

            from src.models.exam_question_instance import (
                ExamQuestionInstance,
            )

            instances = [
                ExamQuestionInstance(
                    question=q,
                )
                for q in questions
            ]

            sections = (
                group_by_points(
                    instances
                )
            )

            content = (
                self._question_renderer
                .render_sections(
                    sections
                )
            )

        result = self._template

        for key, value in metadata.items():

            result = result.replace(
                f"[[ {key} ]]",
                str(value),
            )

        result = result.replace(
            "[[ questions_content ]]",
            content,
        )

        result = result.replace(
            "[[ total_questions ]]",
            str(len(questions)),
        )

        total_score = sum(
            q.points
            for q in questions
        )

        result = result.replace(
            "[[ total_score ]]",
            str(total_score),
        )

        result = result.replace(
            "[[ print_answers_config ]]",
            (
                "\\printanswers"
                if print_answers
                else "\\noprintanswers"
            ),
        )

        return result