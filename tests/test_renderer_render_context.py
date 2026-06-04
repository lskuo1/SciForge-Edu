from pathlib import Path

from src.models.question import Question
from src.renderer.render_context import (
    RenderContext,
)
from src.renderer.resource_collector import (
    ResourceReference,
)


def make_question(
    uuid: str,
):

    return Question(
        uuid=uuid,
        label=uuid,
        question_type="single_choice",
        points=1,
        stem_tex="Question",
    )


def test_create_render_context():

    question = make_question(
        "Q1"
    )

    context = RenderContext(
        questions=[question],
        namespace_map={
            "Q1": "q0001"
        },
    )

    assert len(
        context.questions
    ) == 1

    assert (
        context.namespace_map[
            "Q1"
        ]
        == "q0001"
    )


def test_default_resource_references():

    context = RenderContext(
        questions=[],
        namespace_map={},
    )

    assert (
        context.resource_references
        == []
    )


def test_default_asset_mapping():

    context = RenderContext(
        questions=[],
        namespace_map={},
    )

    assert (
        context.asset_mapping
        == {}
    )


def test_store_resource_references():

    resource = (
        ResourceReference(
            question_uuid="Q1",
            original_path="acid.png",
            resolved_path=Path(
                "/tmp/acid.png"
            ),
            exists=True,
        )
    )

    context = RenderContext(
        questions=[],
        namespace_map={},
        resource_references=[
            resource
        ],
    )

    assert len(
        context.resource_references
    ) == 1

    assert (
        context
        .resource_references[0]
        .question_uuid
        == "Q1"
    )


def test_store_asset_mapping():

    context = RenderContext(
        questions=[],
        namespace_map={},
        asset_mapping={
            Path(
                "/tmp/source.png"
            ): Path(
                "/tmp/assets/q0001_source.png"
            )
        },
    )

    assert len(
        context.asset_mapping
    ) == 1