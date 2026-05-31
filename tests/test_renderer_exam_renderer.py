from src.models.choice import Choice
from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.exam_section import (
    ExamSection,
)
from src.models.question import Question
from src.renderer.exam_renderer import (
    ExamRenderer,
)


def test_render_question():
    renderer = ExamRenderer()

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=2,
        stem_tex="Which is acid?",
        choices=[
            Choice(
                text_tex="HCl",
                is_correct=True,
            ),
            Choice(
                text_tex="NaOH",
                is_correct=False,
            ),
        ],
    )

    latex = renderer.render_question(
        question
    )

    assert "\\question" in latex

    assert "Which is acid?" in latex

    assert "\\CorrectChoice" in latex


def test_render_questions():
    renderer = ExamRenderer()

    q1 = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=1,
        stem_tex="Q1",
    )

    q2 = Question(
        uuid="Q2",
        label="Q2",
        question_type="single_choice",
        points=1,
        stem_tex="Q2",
    )

    latex = renderer.render_questions(
        [q1, q2]
    )

    assert "Q1" in latex

    assert "Q2" in latex


def test_render_section():
    renderer = ExamRenderer()

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=2,
        stem_tex="Example",
    )

    instance = ExamQuestionInstance(
        question=question,
    )

    section = ExamSection(
        title="Section A",
        points_per_question=2,
    )

    section.add_question(
        instance,
    )

    latex = renderer.render_section(
        section
    )

    assert "\\section*" in latex

    assert "\\question Example" in latex


def test_render_sections():
    renderer = ExamRenderer()

    question = Question(
        uuid="Q1",
        label="Q1",
        question_type="single_choice",
        points=2,
        stem_tex="Example",
    )

    instance1 = ExamQuestionInstance(
        question=question,
    )

    instance2 = ExamQuestionInstance(
        question=question,
    )

    section1 = ExamSection(
        title="A",
        points_per_question=2,
    )

    section2 = ExamSection(
        title="B",
        points_per_question=4,
    )

    section1.add_question(
        instance1,
    )

    section2.add_question(
        instance2,
    )

    latex = renderer.render_sections(
        [
            section1,
            section2,
        ]
    )

    assert (
        latex.count(
            "\\section*"
        )
        == 2
    )