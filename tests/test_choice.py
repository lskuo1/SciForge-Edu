from src.models.choice import Choice


def test_create_choice():

    c = Choice(

        label="A",

        text_tex="HCl",

        is_correct=True
    )

    assert c.label == "A"

    assert c.text_tex == "HCl"

    assert c.is_correct is True