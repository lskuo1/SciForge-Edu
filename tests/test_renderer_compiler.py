"""
Tests for renderer.compiler.
"""

from pathlib import Path

from src.renderer.compiler import ExamCompiler


def test_render_template(
    tmp_path: Path,
) -> None:
    """
    Verify template rendering using Python format().
    """

    template_path = (
        tmp_path / "template.tex"
    )

    output_path = (
        tmp_path / "output.tex"
    )

    template_path.write_text(
        "Hello {name}",
        encoding="utf-8",
    )

    compiler = ExamCompiler()

    compiler.render_template(
        template_path=template_path,
        output_path=output_path,
        context={
            "name": "SciForge",
        },
    )

    assert output_path.exists()

    rendered = output_path.read_text(
        encoding="utf-8",
    )

    assert rendered == "Hello SciForge"