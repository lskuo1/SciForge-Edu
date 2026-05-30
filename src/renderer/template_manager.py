"""
Module Purpose
--------------

Provide template discovery and lookup services
for the Renderer subsystem.

Responsibilities
----------------

- Discover available templates
- Resolve template paths
- Validate template existence

Important Notes
---------------

This module does not perform rendering.

Rendering belongs to compiler.py.
"""

from pathlib import Path


class TemplateManager:
    """
    Manage available exam templates.
    """

    def __init__(
        self,
        templates_root: Path,
    ) -> None:
        """
        Parameters
        ----------
        templates_root:
            Root templates directory.
        """

        self._templates_root = templates_root

    def list_templates(
        self,
    ) -> list[str]:
        """
        Return available template names.
        """

        if not self._templates_root.exists():
            return []

        templates: list[str] = []

        for item in self._templates_root.iterdir():
            if item.is_dir():
                templates.append(item.name)

        templates.sort()

        return templates

    def get_template_path(
        self,
        template_name: str,
    ) -> Path:
        """
        Resolve template.tex path.

        Raises
        ------
        FileNotFoundError
            If template does not exist.
        """

        template_path = (
            self._templates_root
            / template_name
            / "template.tex"
        )

        if not template_path.exists():
            raise FileNotFoundError(
                f"Template not found: {template_name}"
            )

        return template_path