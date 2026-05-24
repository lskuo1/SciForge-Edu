from src.models.provenance import Provenance


def test_create_provenance():

    p = Provenance(

        source_type="ai",

        source_name="SciForge AI",

        created_by="System",

        confidence=0.95
    )

    assert p.source_type == "ai"

    assert p.confidence == 0.95