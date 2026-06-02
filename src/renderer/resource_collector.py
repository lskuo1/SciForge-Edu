"""
Module Purpose
--------------

Discover external resources referenced by
Question objects.

Responsibilities
----------------

- Scan Question content
- Discover includegraphics resources
- Resolve resource paths
- Report missing resources

Important Notes
---------------

This module does not copy resources.

Packaging belongs to AssetPackager.
"""

from dataclasses import dataclass
from pathlib import Path
import re

from src.models.question import Question


INCLUDEGRAPHICS_PATTERN = re.compile(
    r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}"
)


@dataclass(frozen=True)
class ResourceReference:
    """
    Resolved resource reference.
    """

    original_path: str

    resolved_path: Path

    exists: bool


class ResourceCollector:
    """
    Discover resources referenced by Questions.
    """

    def collect(
        self,
        question: Question,
    ) -> list[ResourceReference]:

        resources: list[ResourceReference] = []

        if not question.source_path:
            return resources

        source_dir = (
            Path(question.source_path)
            .parent
        )

        tex_blocks = [
            question.stem_tex,
        ]

        if question.solution:
            tex_blocks.append(
                question.solution.content_tex
            )

        for choice in question.choices:
            tex_blocks.append(
                choice.text_tex
            )

        for block in tex_blocks:

            for match in (
                INCLUDEGRAPHICS_PATTERN.finditer(
                    block
                )
            ):

                relative_path = (
                    match.group(1).strip()
                )

                resolved = (
                    source_dir
                    .joinpath(relative_path)
                    .resolve()
                )

                resources.append(
                    ResourceReference(
                        original_path=relative_path,
                        resolved_path=resolved,
                        exists=resolved.exists(),
                    )
                )

        return resources