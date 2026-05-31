from src.models.exam_question_instance import (
    ExamQuestionInstance,
)
from src.models.exam_section import (
    ExamSection,
)
from src.models.question import Question


def test_exam_section_question_count():

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
        instance
    )

    assert section.question_count == 1


def test_exam_section_total_points():

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
        instance1
    )

    section.add_question(
        instance2
    )

    assert section.total_points == 4

def test_exam_section_summary():

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

    assert (
        section.section_summary
        == "每題2分，共4分"
    )