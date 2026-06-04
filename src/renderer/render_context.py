"""
Module Purpose
--------------

Shared renderer state passed
between renderer pipeline stages.

Responsibilities
----------------

- Store Questions
- Store namespace maps
- Store resource references
- Store asset mappings

Important Notes
---------------

RenderContext exists only for
a single render operation.
"""

from pathlib import Path

from pydantic import BaseModel
from pydantic import Field

from src.models.question import Question
from src.renderer.resource_collector import (
    ResourceReference,
)


class RenderContext(
    BaseModel
):
    """
    Shared renderer state.
    """

    questions: list[
        Question
    ]

    namespace_map: dict[
        str,
        str,
    ]

    resource_references: list[
        ResourceReference
    ] = Field(
        default_factory=list
    )

    asset_mapping: dict[
        Path,
        Path,
    ] = Field(
        default_factory=dict
    )

    model_config = {
        "arbitrary_types_allowed": True
    }