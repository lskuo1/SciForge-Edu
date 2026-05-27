"""
generate_snapshot.py

Purpose:
Generate and synchronize API snapshots for project context.

Responsibilities:

- Discover project models
- Extract Pydantic model structures
- Generate API snapshot markdown
- Synchronize official snapshot files

Important notes:

- API snapshots represent current project state
- Snapshot files are treated as system metadata
- Snapshot updates are automatic
- Official snapshots are stored in docs/api_snapshot.md
"""

import importlib
import inspect
import pkgutil
import sys
from pathlib import Path

from pydantic import BaseModel


def get_project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def get_snapshot_path() -> Path:
    return get_project_root() / "docs" / "api_snapshot.md"


def get_models_path() -> Path:
    return get_project_root() / "src" / "models"


def discover_model_modules() -> list[str]:
    models_path = get_models_path()

    modules = []

    for module in pkgutil.iter_modules([str(models_path)]):

        if module.name.startswith("_"):
            continue

        modules.append(
            f"src.models.{module.name}"
        )

    return sorted(modules)


def load_module(module_name: str):

    return importlib.import_module(
        module_name
    )


def extract_pydantic_models(
        module
) -> list[type[BaseModel]]:

    models = []

    for _, obj in inspect.getmembers(
            module,
            inspect.isclass
    ):

        if not issubclass(obj, BaseModel):
            continue

        if obj is BaseModel:
            continue

        if obj.__module__ != module.__name__:
            continue

        models.append(obj)

    return models


def format_field_type(annotation) -> str:

    if hasattr(annotation, "__name__"):
        return annotation.__name__

    return str(annotation).replace(
        "typing.",
        ""
    )


def render_model(
        model: type[BaseModel]
) -> str:

    lines = []

    lines.append(
        f"### {model.__name__}"
    )

    lines.append("")
    lines.append("```text")

    fields = list(
        model.model_fields.items()
    )

    for index, (
            field_name,
            field_info
    ) in enumerate(fields):

        branch = "├──"

        if index == len(fields) - 1:
            branch = "└──"

        field_type = format_field_type(
            field_info.annotation
        )

        lines.append(
            (
                f"{branch} "
                f"{field_name}: "
                f"{field_type}"
            )
        )

    lines.append("```")
    lines.append("")

    if model.__doc__:

        lines.append("Description:")
        lines.append("")

        lines.append(
            model.__doc__.strip()
        )

        lines.append("")

    return "\n".join(lines)


def build_snapshot_content() -> str:

    lines = []

    lines.append(
        "# SciForge API Snapshot"
    )

    lines.append("")
    lines.append(
        "## Core Models"
    )

    lines.append("")

    for module_name in discover_model_modules():

        module = load_module(module_name)

        models = extract_pydantic_models(
            module
        )

        if not models:
            continue

        for model in models:

            lines.append(
                render_model(model)
            )

    return "\n".join(lines)


def generate_snapshot() -> bool:
    snapshot_file = get_snapshot_path()

    content = build_snapshot_content()

    old_content = ""

    if snapshot_file.exists():

        old_content = snapshot_file.read_text(
            encoding="utf-8"
        )

    if old_content == content:
        return False

    snapshot_file.write_text(
        content,
        encoding="utf-8"
    )

    return True


def main():
    project_root = get_project_root()

    if str(project_root) not in sys.path:

        sys.path.insert(
            0,
            str(project_root)
        )

    snapshot_updated = generate_snapshot()

    if snapshot_updated:
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()