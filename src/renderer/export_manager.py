"""
Module Purpose
--------------

Provide export bundle management.

Responsibilities
----------------

- Create export directories
- Create assets directory
- Construct OutputBundle instances

Important Notes
---------------

This module does not render templates.

This module does not compile PDFs.
"""

from pathlib import Path

from src.renderer.output_bundle import (
    OutputBundle,
)


class ExportManager:
    """
    Manage self-contained export bundles.
    """

    def create_bundle(
        self,
        export_dir: Path,
    ) -> OutputBundle:
        """
        Create export bundle structure.
        """

        export_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        assets_dir = (
            export_dir
            / "assets"
        )

        assets_dir.mkdir(
            exist_ok=True,
        )

        return OutputBundle(
            export_dir=export_dir,
            assets_dir=assets_dir,
            student_tex=(
                export_dir
                / "student.tex"
            ),
            teacher_tex=(
                export_dir
                / "teacher.tex"
            ),
            answer_table_tex=(
                export_dir
                / "answer_table.tex"
            ),
        )