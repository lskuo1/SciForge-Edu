"""
generate_exam.py

End-to-end demo:

sample_questions.tex
    ↓
QuestionParser
    ↓
Question objects
    ↓
ExamExport
    ↓
student.tex
teacher.tex
"""

from pathlib import Path
import sys

# --------------------------------------------------
# Make project root importable
# --------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# --------------------------------------------------
# Imports
# --------------------------------------------------

from src.parser.question_parser import QuestionParser
from src.workspace.exam_export import ExamExport

# --------------------------------------------------
# Paths
# --------------------------------------------------

QUESTION_FILE = (
    ROOT
    / "examples"
    / "sample_questions.tex"
)

TEMPLATE_FILE = (
    ROOT
    / "templates"
    / "midterm_base.tex"
)

OUTPUT_DIR = (
    ROOT
    / "build"
)

# --------------------------------------------------
# Main
# --------------------------------------------------


def main() -> None:

    if not QUESTION_FILE.exists():
        raise FileNotFoundError(
            f"Question file not found:\n"
            f"{QUESTION_FILE}"
        )

    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(
            f"Template file not found:\n"
            f"{TEMPLATE_FILE}"
        )

    parser = QuestionParser()

    question_text = QUESTION_FILE.read_text(
        encoding="utf-8"
    )

    questions = parser.parse_questions(
        question_text
    )

    template_text = TEMPLATE_FILE.read_text(
        encoding="utf-8"
    )

    metadata = {
        "school_name": "SciForge Middle School",
        "semester": "114學年度第2學期",
        "exam_title": "第二次段考",
        "grade": "八年級",
        "course": "自然科學",
        "test_range": "第1~4章",
        "year_code": "114-2",
    }

    exporter = ExamExport()

    exporter.export(
        questions=questions,
        template_text=template_text,
        metadata=metadata,
        output_dir=OUTPUT_DIR,
    )

    print()
    print("Export completed.")
    print(f"Output directory:")
    print(OUTPUT_DIR)
    print()

    print("Generated files:")

    for file in OUTPUT_DIR.glob("*.tex"):
        print(f"  - {file.name}")


if __name__ == "__main__":
    main()