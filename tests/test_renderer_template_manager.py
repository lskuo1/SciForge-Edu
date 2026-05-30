from pathlib import Path

import pytest

from src.renderer.template_manager import (
    TemplateManager,
)


def test_list_templates(
    tmp_path: Path,
) -> None:
    """
    Verify template discovery.
    """

    (
        tmp_path
        / "midterm"
    ).mkdir()

    (
        tmp_path
        / "quiz"
    ).mkdir()

    manager = TemplateManager(
        templates_root=tmp_path,
    )

    templates = manager.list_templates()

    assert templates == [
        "midterm",
        "quiz",
    ]


def test_get_template_path(
    tmp_path: Path,
) -> None:
    """
    Verify template lookup.
    """

    template_dir = (
        tmp_path
        / "midterm"
    )

    template_dir.mkdir()

    template_file = (
        template_dir
        / "template.tex"
    )

    template_file.write_text(
        "dummy",
        encoding="utf-8",
    )

    manager = TemplateManager(
        templates_root=tmp_path,
    )

    path = manager.get_template_path(
        "midterm"
    )

    assert path == template_file


def test_missing_template(
    tmp_path: Path,
) -> None:
    """
    Verify missing template handling.
    """

    manager = TemplateManager(
        templates_root=tmp_path,
    )

    with pytest.raises(
        FileNotFoundError
    ):
        manager.get_template_path(
            "missing"
        )