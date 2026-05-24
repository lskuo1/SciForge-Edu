from src.models.provenance import Provenance
from src.models.solution import Solution


def test_create_solution():

    p = Provenance(

        source_type="teacher",

        source_name="Teacher",

        created_by="Long-Sheng"
    )

    s = Solution(

        content_tex="Because $1+1=2$",

        provenance=p
    )

    assert s.content_tex == "Because $1+1=2$"

    assert s.is_verified is False

    assert s.provenance.source_type == "teacher"