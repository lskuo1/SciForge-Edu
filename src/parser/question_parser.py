"""
question_parser.py

Purpose:
Parse LaTeX question content.

Responsibilities:

- Parse question stem
- Support future choice parsing
- Support future solution parsing

Notes:

Current implementation only parses
simple \\question syntax.
"""

import re

from src.models.question import Question


class QuestionParser:
    """
    Parse Question objects from LaTeX.
    """

    def parse(
            self,
            text: str
    ) -> Question:

        match = re.search(

            r"\\question\s+(.*)",

            text
        )

        if not match:

            raise ValueError(
                "Question not found."
            )

        stem = match.group(1)

        return Question(

            uuid="TEMP",

            label="TEMP",

            question_type="unknown",

            points=0,

            stem_tex=stem
        )