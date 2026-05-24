from src.models.version import Version


def test_create_version():

    v = Version(

        version=2,

        author="Teacher",

        change_note="Update wording"
    )

    assert v.version == 2

    assert v.author == "Teacher"


def test_version_must_be_positive():

    try:

        Version(

            version=0,

            author="Teacher",

            change_note="test"
        )

        assert False

    except Exception:

        assert True