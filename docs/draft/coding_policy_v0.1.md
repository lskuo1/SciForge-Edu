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