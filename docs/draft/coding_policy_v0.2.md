# SciForge-Edu Coding Policy
Version: v0.2
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
- Keep short expressions on one line when readable

Bad:

project_root = (
    Path(__file__)
    .resolve()
    .parent
    .parent
)

Good:

project_root = Path(__file__).resolve().parent.parent


- Avoid unnecessary line wrapping

Bad:

snapshot_is_current = (
    generate_snapshot()
)

Good:

snapshot_is_current = generate_snapshot()


- Keep chained calls on one line
  when readability is acceptable


- Avoid decorative spacing

Bad:

def main():


    x = 1


    y = 2

Good:

def main():
    x = 1
    y = 2


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

Prefer explaining WHY instead of WHAT.

Bad:

i += 1

# add one

Good:

statistics:list[AssessmentStatistics]

# Statistics belong to observed exam
# results rather than intrinsic question
# properties.

---

# Snapshot Rules

Purpose:

API snapshots maintain consistent project context
between developers and AI systems.

Rules:

- Snapshots are treated as system metadata
- Snapshot updates are automatic
- Snapshot files should always reflect current project state
- Snapshot updates do not require manual decisions

Commit behavior:

When snapshot content changes during commit:

1. Update docs/api_snapshot.md
2. Stage docs/api_snapshot.md automatically
3. Append:

   [snapshot updated]

4. Continue commit

Notes:

Snapshot files are not treated as user-authored content.
