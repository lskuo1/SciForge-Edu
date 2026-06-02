"""
question_id.py

Purpose
-------
Generate deterministic Question Identity
for SciForge-Edu Question objects.

Responsibilities
----------------
- normalize identity fields
- build canonical representations
- generate deterministic Question IDs

Identity Rules
--------------
- question_type participates
- stem_tex participates
- choice text participates
- choice correctness participates
- choice order does not participate

Future Work
-----------
Question Similarity Detection is outside
the scope of this module.
"""

from __future__ import annotations

import hashlib

from src.models.choice import Choice


def normalize_text(text: str) -> str:
    """
    Normalize whitespace for identity generation.
    """
    return " ".join(text.split())


def normalize_choices(
    choices: list[Choice],
) -> list[tuple[str, bool]]:
    """
    Normalize and sort Choice objects.

    Choice order shall not affect
    Question Identity.
    """
    normalized = [
        (
            normalize_text(choice.text_tex),
            choice.is_correct,
        )
        for choice in choices
    ]

    normalized.sort()

    return normalized


def build_canonical_representation(
    question_type: str,
    stem_tex: str,
    choices: list[Choice],
) -> str:
    """
    Build the canonical Question representation.
    """

    choice_lines = [
        f"{text}|{is_correct}"
        for text, is_correct
        in normalize_choices(choices)
    ]

    return "\n".join(
        [
            normalize_text(question_type),
            normalize_text(stem_tex),
            *choice_lines,
        ]
    )


def generate_question_id(
    question_type: str,
    stem_tex: str,
    choices: list[Choice],
) -> str:
    """
    Generate a deterministic Question ID.
    """

    canonical = build_canonical_representation(
        question_type=question_type,
        stem_tex=stem_tex,
        choices=choices,
    )

    return hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()[:16]