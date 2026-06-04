"""
Module Purpose
--------------

Execute renderer preprocessing
pipeline stages.

Responsibilities
----------------

- Assign namespaces
- Rewrite references
- Produce RenderContext

Important Notes
---------------

This pipeline does not render LaTeX.

This pipeline prepares data for
later rendering stages.
"""

from src.models.question import Question

from src.renderer.namespace_assigner import (
    NamespaceAssigner,
)
from src.renderer.reference_rewriter import (
    ReferenceRewriter,
)
from src.renderer.render_context import (
    RenderContext,
)


class RenderPipeline:
    """
    Execute renderer preprocessing.
    """

    def run(
        self,
        questions: list[Question],
    ) -> RenderContext:

        namespace_map = (
            NamespaceAssigner()
            .assign(questions)
        )

        rewritten_questions = []

        rewriter = (
            ReferenceRewriter()
        )

        for question in questions:

            render_id = (
                namespace_map[
                    question.uuid
                ]
            )

            rewritten_questions.append(
                rewriter.rewrite(
                    question,
                    render_id,
                )
            )

        return RenderContext(
            questions=rewritten_questions,
            namespace_map=namespace_map,
        )