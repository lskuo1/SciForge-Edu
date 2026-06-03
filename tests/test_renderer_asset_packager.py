from pathlib import Path

import pytest

from src.renderer.asset_packager import (
    AssetPackager,
)
from src.renderer.resource_collector import (
    ResourceReference,
)


def test_copy_single_asset(
    tmp_path: Path,
):

    source = (
        tmp_path
        / "acid.png"
    )

    source.write_bytes(
        b"fake"
    )

    assets_dir = (
        tmp_path
        / "assets"
    )

    resources = [
        ResourceReference(
            question_uuid="Q1",
            original_path="acid.png",
            resolved_path=source,
            exists=True,
        )
    ]

    mapping = (
        AssetPackager()
        .package(
            resources=resources,
            namespace_map={
                "Q1": "q0001"
            },
            assets_dir=assets_dir,
        )
    )

    target = (
        assets_dir
        / "q0001_acid.png"
    )

    assert target.exists()

    assert (
        mapping[source]
        == target
    )


def test_copy_multiple_assets(
    tmp_path: Path,
):

    source1 = (
        tmp_path
        / "acid.png"
    )

    source2 = (
        tmp_path
        / "base.png"
    )

    source1.write_bytes(
        b"acid"
    )

    source2.write_bytes(
        b"base"
    )

    assets_dir = (
        tmp_path
        / "assets"
    )

    resources = [
        ResourceReference(
            question_uuid="Q1",
            original_path="acid.png",
            resolved_path=source1,
            exists=True,
        ),
        ResourceReference(
            question_uuid="Q2",
            original_path="base.png",
            resolved_path=source2,
            exists=True,
        ),
    ]

    mapping = (
        AssetPackager()
        .package(
            resources=resources,
            namespace_map={
                "Q1": "q0001",
                "Q2": "q0002",
            },
            assets_dir=assets_dir,
        )
    )

    assert (
        assets_dir
        / "q0001_acid.png"
    ).exists()

    assert (
        assets_dir
        / "q0002_base.png"
    ).exists()

    assert len(mapping) == 2


def test_filename_collision(
    tmp_path: Path,
):

    dir1 = (
        tmp_path
        / "a"
    )

    dir2 = (
        tmp_path
        / "b"
    )

    dir1.mkdir()

    dir2.mkdir()

    source1 = (
        dir1
        / "acid.png"
    )

    source2 = (
        dir2
        / "acid.png"
    )

    source1.write_bytes(
        b"one"
    )

    source2.write_bytes(
        b"two"
    )

    assets_dir = (
        tmp_path
        / "assets"
    )

    resources = [
        ResourceReference(
            question_uuid="Q1",
            original_path="acid.png",
            resolved_path=source1,
            exists=True,
        ),
        ResourceReference(
            question_uuid="Q2",
            original_path="acid.png",
            resolved_path=source2,
            exists=True,
        ),
    ]

    AssetPackager().package(
        resources=resources,
        namespace_map={
            "Q1": "q0001",
            "Q2": "q0002",
        },
        assets_dir=assets_dir,
    )

    assert (
        assets_dir
        / "q0001_acid.png"
    ).exists()

    assert (
        assets_dir
        / "q0002_acid.png"
    ).exists()


def test_missing_asset_raises(
    tmp_path: Path,
):

    missing = (
        tmp_path
        / "missing.png"
    )

    resources = [
        ResourceReference(
            question_uuid="Q1",
            original_path="missing.png",
            resolved_path=missing,
            exists=False,
        )
    ]

    with pytest.raises(
        FileNotFoundError
    ):

        AssetPackager().package(
            resources=resources,
            namespace_map={
                "Q1": "q0001"
            },
            assets_dir=(
                tmp_path
                / "assets"
            ),
        )


def test_generate_mapping(
    tmp_path: Path,
):

    source = (
        tmp_path
        / "acid.png"
    )

    source.write_bytes(
        b"fake"
    )

    assets_dir = (
        tmp_path
        / "assets"
    )

    mapping = (
        AssetPackager()
        .package(
            resources=[
                ResourceReference(
                    question_uuid="Q1",
                    original_path="acid.png",
                    resolved_path=source,
                    exists=True,
                )
            ],
            namespace_map={
                "Q1": "q0001"
            },
            assets_dir=assets_dir,
        )
    )

    expected = (
        assets_dir
        / "q0001_acid.png"
    )

    assert (
        mapping[source]
        == expected
    )