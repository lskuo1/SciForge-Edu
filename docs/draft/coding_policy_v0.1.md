# SciForge-Edu Coding Policy
Version: v0.1
Status: Draft

# Documentation Rules

All source files should contain:

1. Module purpose
2. Responsibilities
3. Important notes

Example:

"""
usage.py

Purpose:
Track question usage history.

Responsibilities:

- Record exam usage history
- Prevent repeated questions
- Support future analytics
"""

---

All classes should contain:

1. Purpose
2. Important constraints

Example:

class QuestionUsage(BaseModel):
    """
    Track usage history of one question.
    """

---

# Formatting Rules

- Follow PyCharm auto-formatting
- Follow PEP8
- Avoid excessive vertical spacing
- Prefer readability over line minimization
- Use blank lines to separate logical blocks

Example:

Good:

def parse(self, text: str) -> Question:
    question_match = re.search(
        r"\\question\s+(.*)",
        text
    )

    if not question_match:
        raise ValueError("Question not found.")

    stem = question_match.group(1)

Bad:

def parse(
        self,
        text: str
)->Question:



    question_match=re.search(
            r"\\question\s+(.*)",
            text
    )

---

# Test Naming Rules

Pattern:

test_<module_path>_<filename>.py

Examples:

src/parser/question_parser.py
↓

test_parser_question_parser.py


Avoid excessive inline comments.

Prefer explaining:

WHY

instead of:

WHAT

Bad:

i += 1


# add one

Good:

statistics:list[AssessmentStatistics]

# Statistics belong to observed exam
# results rather than intrinsic question
# properties.