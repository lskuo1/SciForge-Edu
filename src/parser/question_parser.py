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
from src.models.choice import Choice
from src.models.question import Question


class QuestionParser:
    """
    Parse Question objects from LaTeX.
    """

    def parse(self, text: str) -> Question:
        question_match = re.search(
            r"\\question\s+(.*)",
            text
        )

        if not question_match:
            raise ValueError("Question not found.")

        stem = question_match.group(1)

        choice_matches = re.findall(
            r"\\choice\s+(.*)",
            text
        )

        choices = [
            Choice(text_tex=c)
            for c in choice_matches
        ]

        return Question(
            uuid="TEMP",
            label="TEMP",
            question_type="single_choice",
            points=0,
            stem_tex=stem,
            choices=choices
        )