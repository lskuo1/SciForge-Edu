from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.exam_section import (
    ExamSection,
)
from src.models.question import Question
from src.renderer.section_renderer import (
    SectionRenderer,
)


def test_section_renderer_generates_summary():

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

    section = ExamSection(
        title="Section A",
        points_per_question=2,
    )

    section.add_question(
        instance1,
    )

    section.add_question(
        instance2,
    )

    renderer = SectionRenderer()

    latex = renderer.render(
        section,
    )

    assert (
        "\\section*" in latex
    )

    assert (
        "每題2分，共4分"
        in latex
    )