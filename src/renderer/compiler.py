"""
Module Purpose
--------------

Provide basic template rendering services.

Responsibilities
----------------

- Render template text
- Write rendered output files

Important Notes
---------------

This implementation intentionally avoids
third-party template engines.

Future versions may introduce Jinja2.
"""

from pathlib import Path


class ExamCompiler:
    """
    Render template text using Python format().
    """

    def render_template(
        self,
        template_path: Path,
        output_path: Path,
        context: dict[str, object],
    ) -> None:
        """
        Render a template file.
        """

        template_text = template_path.read_text(
            encoding="utf-8",
        )

        rendered = template_text.format(
            **context,
        )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            rendered,
            encoding="utf-8",
        )