"""
Module Purpose
--------------

Assign renderer namespaces to
Questions participating in a
render operation.

Responsibilities
----------------

- Generate render namespaces
- Produce namespace maps
- Preserve render ordering

Important Notes
---------------

Render namespaces are temporary.

Render namespaces are not
Question identities.
"""

from src.models.question import Question


class NamespaceAssigner:
    """
    Assign render namespaces
    to Questions.
    """

    def assign(
        self,
        questions: list[Question],
    ) -> dict[str, str]:

        mapping: dict[
            str,
            str,
        ] = {}

        for index, question in enumerate(
            questions,
            start=1,
        ):

            mapping[
                question.uuid
            ] = (
                f"q{index:04d}"
            )

        return mapping