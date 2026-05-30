"""
Module Purpose
--------------

Define renderer output artifacts.

Responsibilities
----------------

- Represent generated output files
- Provide a stable contract between
  rendering and compilation subsystems

Important Notes
---------------

This module does not generate files.

It only defines output artifact structures.
"""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OutputBundle:
    """
    Renderer output artifact paths.
    """

    student_tex: Path

    teacher_tex: Path

    answer_table_tex: Path