"""
Module Purpose
--------------

Define export artifacts produced by
the Renderer subsystem.

Responsibilities
----------------

- Represent exportable exam artifacts
- Provide a stable contract between
  rendering and export services

Important Notes
---------------

Export bundles must be self-contained.

Generated TeX files should remain
compilable outside SciForge-Edu.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OutputBundle:
    """
    Self-contained exam export bundle.
    """

    export_dir: Path

    assets_dir: Path

    student_tex: Path

    teacher_tex: Path

    answer_table_tex: Path