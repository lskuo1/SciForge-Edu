"""
question_parser.py

Purpose:
Parse LaTeX question content.

Responsibilities:

- Parse multiple questions
- Parse legacy choice syntax
- Parse choices environment
- Parse CorrectChoice markers
- Parse legacy solution syntax
- Parse solution environment

Parser Philosophy
-----------------

The parser should be permissive.

Missing optional metadata should not
cause parsing failure.

Validation belongs to diagnostics.

Backward Compatibility
----------------------

The parser supports both:

- Legacy inline syntax
- Environment-based syntax

to facilitate migration of older
question banks.
"""

import re

from src.models.choice import Choice
from src.models.provenance import Provenance
from src.models.question import Question
from src.models.solution import Solution


class QuestionParser:
    """
    Parse Question objects from LaTeX.
    """

    def parse(
        self,
        text: str,
    ) -> Question:
        """
        Legacy API.

        Returns the first parsed question.
        """

        questions = self.parse_questions(
            text
        )

        if not questions:
            raise ValueError(
                "Question not found."
            )

        return questions[0]

    def parse_questions(
        self,
        text: str,
    ) -> list[Question]:
        """
        Parse multiple questions from LaTeX.
        """

        blocks = re.split(
            r"(?=\\question)",
            text,
        )

        blocks = [
            block.strip()
            for block in blocks
            if block.strip()
        ]

        questions: list[Question] = []

        for index, block in enumerate(
            blocks,
            start=1,
        ):
            question_match = re.search(
                r"\\question\s+(.*?)(?="
                r"\\begin\{choices\}"
                r"|\\begin\{solution\}"
                r"|\\choice"
                r"|\\CorrectChoice"
                r"|\\solution"
                r"|$)",
                block,
                re.DOTALL,
            )

            if not question_match:
                continue

            stem = (
                question_match
                .group(1)
                .strip()
            )

            choices = self._extract_choices(
                block
            )

            solution = self._extract_solution(
                block
            )

            question = Question(
                uuid=f"TEMP-{index}",
                label=f"TEMP-{index}",
                question_type="single_choice",
                points=0,
                stem_tex=stem,
                choices=choices,
                solution=solution,
            )

            questions.append(
                question
            )

        return questions

    def _extract_choices(
        self,
        block: str,
    ) -> list[Choice]:
        """
        Parse both legacy and environment-based
        choice formats.
        """

        choices_match = re.search(
            r"\\begin\{choices\}"
            r"(.*?)"
            r"\\end\{choices\}",
            block,
            re.DOTALL,
        )

        if choices_match:
            return self._parse_choices(
                choices_match.group(1)
            )

        legacy_choices = re.findall(
            r"\\choice\s+(.*)",
            block,
        )

        return [
            Choice(
                text_tex=text.strip(),
                is_correct=False,
            )
            for text in legacy_choices
        ]

    def _parse_choices(
        self,
        choices_block: str,
    ) -> list[Choice]:
        """
        Parse choices environment.
        """

        pattern = re.compile(
            r"\\(CorrectChoice|choice)"
            r"\s+(.*?)(?="
            r"\\(?:CorrectChoice|choice)"
            r"|$)",
            re.DOTALL,
        )

        choices: list[Choice] = []

        for match in pattern.finditer(
            choices_block
        ):
            kind = match.group(1)

            text = (
                match.group(2)
                .strip()
            )

            choices.append(
                Choice(
                    text_tex=text,
                    is_correct=(
                        kind
                        == "CorrectChoice"
                    ),
                )
            )

        return choices

    def _extract_solution(
        self,
        block: str,
    ) -> Solution | None:
        """
        Parse both legacy and environment-based
        solution formats.
        """

        solution_match = re.search(
            r"\\begin\{solution\}"
            r"(.*?)"
            r"\\end\{solution\}",
            block,
            re.DOTALL,
        )

        if solution_match:
            return self._create_solution(
                solution_match.group(1)
            )

        legacy_solution_match = re.search(
            r"\\solution\s+(.*)",
            block,
            re.DOTALL,
        )

        if legacy_solution_match:
            return self._create_solution(
                legacy_solution_match.group(1)
            )

        return None

    def _create_solution(
        self,
        content: str,
    ) -> Solution:
        """
        Create Solution object.
        """

        return Solution(
            content_tex=content.strip(),
            provenance=Provenance(
                source_type="system",
                source_name="question_parser",
                created_by="system",
            ),
        )