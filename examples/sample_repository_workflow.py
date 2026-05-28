"""
sample_repository_workflow.py

Purpose:
Demonstrate the canonical SciForge-Edu repository workflow.

This example is intentionally written as:

- executable architectural documentation
- repository workflow walkthrough
- AI-readable onboarding artifact

This file demonstrates:

Question
↓
Analysis
↓
RepositoryManager.save_question()
↓
RepositoryIndex projection
↓
search()
↓
load_question()

The goal is not merely to show API syntax.

The goal is to demonstrate:

- repository philosophy
- projection semantics
- metadata architecture
- deterministic workflow behavior
"""


from pathlib import Path
import json
import shutil

from src.models.analysis import Analysis
from src.models.choice import Choice
from src.models.provenance import Provenance
from src.models.question import Question
from src.models.solution import Solution
from src.models.source import Source

from src.repository.manager import RepositoryManager


# ============================================================
# Repository setup
# ============================================================

# This example intentionally uses a local temporary repository.
#
# Repository structure should remain:
#
# - inspectable
# - deterministic
# - human-readable
#
# This reflects the current filesystem-first philosophy.

repository_root = Path(
    "example_repository"
)

if repository_root.exists():
    shutil.rmtree(repository_root)

manager = RepositoryManager(
    repository_root=str(repository_root)
)


# ============================================================
# Analysis metadata
# ============================================================

# Analysis represents intrinsic question properties.
#
# RepositoryIndex later projects searchable metadata
# from Analysis.
#
# RepositoryIndex is intentionally NOT treated
# as a duplicate Question object.

analysis = Analysis(

    subject="physics",

    chapter="Newtonian Mechanics",

    tags=[
        "force",
        "newton",
        "mechanics"
    ],

    difficulty_level=3,

    misconceptions=[
        "force_required_for_motion",
        "mass_confused_with_weight"
    ],

    provenance=Provenance(
        created_by="sample_workflow",
        confidence=0.95
    )
)


# ============================================================
# Multiple choice structure
# ============================================================

choices = [

    Choice(
        key="A",
        content="The object stops immediately."
    ),

    Choice(
        key="B",
        content="The object continues at constant velocity."
    ),

    Choice(
        key="C",
        content="The object accelerates upward."
    ),

    Choice(
        key="D",
        content="The object gains mass."
    )
]


# ============================================================
# Solution structure
# ============================================================

solution = Solution(

    answer="B",

    explanation=(
        "According to Newton's first law, "
        "an object continues at constant velocity "
        "unless acted upon by a net external force."
    )
)


# ============================================================
# Source metadata
# ============================================================

source = Source(

    source_type="textbook",

    source_name="SciForge Physics Prototype"
)


# ============================================================
# Question construction
# ============================================================

# Question remains the primary domain object.
#
# Analysis, Solution, Source, and Choices
# are attached as structured components.

question = Question(

    uuid="physics-newton-001",

    label="Newton First Law Conceptual Question",

    question_type="multiple_choice",

    content=(
        "A hockey puck slides on frictionless ice. "
        "After being struck once, what happens "
        "if no additional force acts on it?"
    ),

    choices=choices,

    solution=solution,

    analysis=analysis,

    source=source
)


# ============================================================
# Repository persistence
# ============================================================

# save_question() performs:
#
# 1. Question persistence
# 2. RepositoryIndex projection update
#
# Projection is intentionally automatic.

manager.save_question(question)

print("\n=== Question Saved ===\n")


# ============================================================
# Inspect generated repository structure
# ============================================================

print("Repository structure:\n")

for path in sorted(repository_root.rglob("*")):

    relative = path.relative_to(repository_root)

    if path.is_dir():
        print(f"[DIR ] {relative}")

    else:
        print(f"[FILE] {relative}")


# ============================================================
# Inspect RepositoryIndex projection
# ============================================================

# RepositoryIndex intentionally stores:
#
# - lightweight metadata
# - searchable projections
#
# rather than complete Question content.

index_file = (
    repository_root
    / "index"
    / "repository_index.json"
)

print("\n=== RepositoryIndex Projection ===\n")

with open(
        index_file,
        "r",
        encoding="utf-8"
) as f:

    index_data = json.load(f)

print(
    json.dumps(
        index_data,
        indent=4,
        ensure_ascii=False
    )
)


# ============================================================
# Structural repository queries
# ============================================================

# Current repository query behavior is:
#
# - deterministic
# - explicit
# - metadata-oriented

print("\n=== Query: subject='physics' ===\n")

physics_results = manager.search(
    subject="physics"
)

for result in physics_results:
    print(result)


print("\n=== Query: tags=['force'] ===\n")

force_results = manager.search(
    tags=["force"]
)

for result in force_results:
    print(result)


print(
    "\n=== Query: "
    "tags=['force', 'newton'] ===\n"
)

combined_results = manager.search(
    tags=["force", "newton"]
)

for result in combined_results:
    print(result)


# ============================================================
# Roundtrip reconstruction
# ============================================================

# load_question() reconstructs the complete
# Question domain object from repository storage.

loaded_question = manager.load_question(
    "physics-newton-001"
)

print("\n=== Roundtrip Reconstruction ===\n")

print(loaded_question)


# ============================================================
# Roundtrip consistency validation
# ============================================================

# The repository workflow should preserve
# deterministic roundtrip semantics.

assert (
    loaded_question.uuid
    ==
    question.uuid
)

assert (
    loaded_question.analysis.subject
    ==
    "physics"
)

assert (
    "force"
    in
    loaded_question.analysis.tags
)

print("\n=== Roundtrip Validation Passed ===\n")


# ============================================================
# Final architectural note
# ============================================================

print(
    "SciForge-Edu repository workflows are "
    "intentionally designed to remain:\n"
)

print("- deterministic")
print("- inspectable")
print("- AI-readable")
print("- projection-oriented")
