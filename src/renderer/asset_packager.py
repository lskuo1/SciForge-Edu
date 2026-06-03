"""
Module Purpose
--------------

Package external resources required by
rendered exam documents.

Responsibilities
----------------

- Copy assets
- Rename assets
- Avoid filename collisions
- Generate asset mappings

Important Notes
---------------

This module does not modify LaTeX.

Label and ref rewriting belong to
other renderer components.
"""

from pathlib import Path
import shutil

from src.renderer.resource_collector import (
    ResourceReference,
)


class AssetPackager:
    """
    Package renderer assets into a
    standalone output directory.
    """

    def package(
        self,
        resources: list[ResourceReference],
        namespace_map: dict[str, str],
        assets_dir: Path,
    ) -> dict[Path, Path]:

        assets_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        mapping: dict[
            Path,
            Path,
        ] = {}

        for resource in resources:

            if not resource.exists:

                raise FileNotFoundError(
                    str(
                        resource.resolved_path
                    )
                )

            render_id = namespace_map[
                resource.question_uuid
            ]

            source = (
                resource.resolved_path
            )

            target_name = (
                f"{render_id}_"
                f"{source.name}"
            )

            target = (
                assets_dir
                / target_name
            )

            shutil.copy2(
                source,
                target,
            )

            mapping[
                source
            ] = target

        return mapping
