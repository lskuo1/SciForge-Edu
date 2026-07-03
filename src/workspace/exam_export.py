"""
Module Purpose
--------------

Export complete exam packages.

Responsibilities
----------------

- Generate student.tex
- Generate teacher.tex
"""

from pathlib import Path

from src.models.question import Question
from src.renderer.exam_render_service import (
    ExamRenderService,
)


class ExamExport:
    """
    Export complete exam files.
    """

    def export(
        self,
        *,
        questions: list[Question],
        template_text: str,
        metadata: dict[str, str],
        output_dir: Path,
    ) -> None:

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        renderer = ExamRenderService(
            template_text
        )

        student_tex = renderer.render_student_tex(
            questions=questions,
            metadata=metadata,
        )

        teacher_tex = renderer.render_teacher_tex(
            questions=questions,
            metadata=metadata,
        )

        (output_dir / "student.tex").write_text(
            student_tex,
            encoding="utf-8",
        )

        (output_dir / "teacher.tex").write_text(
            teacher_tex,
            encoding="utf-8",
        )