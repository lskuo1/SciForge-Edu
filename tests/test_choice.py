from src.models.choice import Choice


def test_create_choice():

    c = Choice(

        text_tex="HCl",

        is_correct=True
    )

    assert c.text_tex == "HCl"

    assert c.is_correct is True


def test_default_correct_value():

    c = Choice(

        text_tex="NaOH"
    )

    assert c.is_correct is False


def test_optional_explanation():

    c = Choice(

        text_tex="NH3",

        explanation="Weak base"
    )

    assert c.explanation == "Weak base"