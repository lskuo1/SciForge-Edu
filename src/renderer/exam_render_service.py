"""
Module Purpose
--------------

Integrate RenderPipeline with
ExamPackageRenderer.

Responsibilities
----------------

- Execute preprocessing pipeline
- Render student exams
- Render teacher exams

Important Notes
---------------

This service is the entry point
for rendering complete exams.
"""

from src.models.question import Question

from src.renderer.exam_package_renderer import (
    ExamPackageRenderer,
)
from src.renderer.render_pipeline import (
    RenderPipeline,
)


class ExamRenderService:
    """
    High-level exam rendering service.
    """

    def __init__(
        self,
        template_text: str,
    ):

        self._pipeline = (
            RenderPipeline()
        )

        self._renderer = (
            ExamPackageRenderer(
                template_text
            )
        )

    def render_student_tex(
        self,
        questions: list[Question],
        metadata: dict[str, str],
    ) -> str:

        context = (
            self._pipeline.run(
                questions
            )
        )

        return (
            self._renderer
            .render_student_tex(
                questions=context.questions,
                metadata=metadata,
            )
        )

    def render_teacher_tex(
        self,
        questions: list[Question],
        metadata: dict[str, str],
    ) -> str:

        context = (
            self._pipeline.run(
                questions
            )
        )

        return (
            self._renderer
            .render_teacher_tex(
                questions=context.questions,
                metadata=metadata,
            )
        )