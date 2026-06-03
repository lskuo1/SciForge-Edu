"""
Module Purpose
--------------

Rewrite LaTeX labels and references
using renderer namespaces.

Responsibilities
----------------

- Rewrite labels
- Rewrite refs
- Rewrite pagerefs
- Rewrite autoref
- Rewrite eqref

Important Notes
---------------

This module operates on Question objects.

The original Question object shall not
be modified.
"""

from __future__ import annotations

import re

from src.models.choice import Choice
from src.models.question import Question
from src.models.solution import Solution


LABEL_PATTERN = re.compile(
    r"\\label\{([^}]*)\}"
)

REFERENCE_PATTERNS = [
    "ref",
    "pageref",
    "autoref",
    "eqref",
]


class ReferenceRewriter:
    """
    Rewrite LaTeX references using a
    render namespace.
    """

    def rewrite(
        self,
        question: Question,
        render_id: str,
    ) -> Question:

        label_map = self._build_label_map(
            question=question,
            render_id=render_id,
        )

        stem_tex = self._rewrite_tex(
            question.stem_tex,
            label_map,
        )

        choices = [
            Choice(
                text_tex=self._rewrite_tex(
                    choice.text_tex,
                    label_map,
                ),
                is_correct=choice.is_correct,
                explanation=choice.explanation,
            )
            for choice in question.choices
        ]

        solution = None

        if question.solution:

            solution = Solution(
                content_tex=self._rewrite_tex(
                    question.solution.content_tex,
                    label_map,
                ),
                provenance=question.solution.provenance,
                is_verified=question.solution.is_verified,
            )

        return question.model_copy(
            update={
                "stem_tex": stem_tex,
                "choices": choices,
                "solution": solution,
            }
        )

    def _build_label_map(
        self,
        question: Question,
        render_id: str,
    ) -> dict[str, str]:

        label_map: dict[
            str,
            str,
        ] = {}

        for block in self._iter_tex_blocks(
            question
        ):

            for match in (
                LABEL_PATTERN.finditer(
                    block
                )
            ):

                original = (
                    match.group(1)
                    .strip()
                )

                normalized = (
                    original.replace(
                        ":",
                        "_",
                    )
                )

                rewritten = (
                    f"{render_id}_"
                    f"{normalized}"
                )

                label_map[
                    original
                ] = rewritten

        return label_map

    def _iter_tex_blocks(
        self,
        question: Question,
    ):

        yield question.stem_tex

        for choice in question.choices:
            yield choice.text_tex

        if question.solution:
            yield (
                question.solution
                .content_tex
            )

    def _rewrite_tex(
        self,
        tex: str,
        label_map: dict[
            str,
            str,
        ],
    ) -> str:

        for (
            original,
            rewritten,
        ) in label_map.items():

            tex = tex.replace(
                rf"\label{{{original}}}",
                rf"\label{{{rewritten}}}",
            )

            for command in (
                REFERENCE_PATTERNS
            ):

                tex = tex.replace(
                    rf"\{command}{{{original}}}",
                    rf"\{command}{{{rewritten}}}",
                )

        return tex