from src.parser.question_parser import (
    QuestionParser,
)


def test_parse_multiple_questions():
    parser = QuestionParser()

    text = r"""
\question First question

\begin{choices}
\choice A
\CorrectChoice B
\choice C
\end{choices}

\question Second question

\begin{choices}
\CorrectChoice X
\choice Y
\end{choices}
"""

    questions = parser.parse_questions(
        text
    )

    assert len(questions) == 2


def test_parse_correct_choice():
    parser = QuestionParser()

    text = r"""
\question Example

\begin{choices}
\choice A
\CorrectChoice B
\choice C
\end{choices}
"""

    question = parser.parse(text)

    correct_count = sum(
        choice.is_correct
        for choice in question.choices
    )

    assert correct_count == 1


def test_parse_missing_solution():
    parser = QuestionParser()

    text = r"""
\question Example

\begin{choices}
\choice A
\CorrectChoice B
\end{choices}
"""

    question = parser.parse(text)

    assert question.solution is None


def test_parse_multiple_correct_choices():
    parser = QuestionParser()

    text = r"""
\question Example

\begin{choices}
\CorrectChoice A
\CorrectChoice B
\choice C
\end{choices}
"""

    question = parser.parse(text)

    correct_count = sum(
        choice.is_correct
        for choice in question.choices
    )

    assert correct_count == 2