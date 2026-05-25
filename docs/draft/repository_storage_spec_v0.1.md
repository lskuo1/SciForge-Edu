# Repository Storage Specification
Version: v0.1
Status: Draft

# 1. Goals

Repository storage should:

- support fast search
- support version tracking
- support resource files
- support future migration
- avoid filename conflicts

---

# 2. Repository Structure

repository/

    index/

        repository_index.json

    questions/

        Q-a72f/

            question.json

            usage.json

            resources/

                fig1.png
                fig2.svg

        Q-b234/

            question.json

            usage.json

            resources/

---

# 3. Question Storage

Question content is stored in:

question.json

Example:

{
    "uuid":"Q-a72f",
    "question_type":"single_choice",
    "stem_tex":"Which is acid?",
    ...
}

Rules:

- one question per folder
- folder name = question UUID
- UUID never changes

---

# 4. Usage Storage

Question usage history:

usage.json

Example:

{
    "uuid":"Q-a72f",

    "used_in":[

        {
            "exam_id":"114_midterm",

            "exam_date":"2026-05-25"
        }

    ]
}

---

# 5. Repository Index

RepositoryIndex entries stored in:

repository/index/repository_index.json

Purpose:

- fast search
- avoid loading complete questions

---

# 6. Resources

Question resources:

resources/

Examples:

- images
- diagrams
- tables
- future media files

Rules:

- avoid filename conflicts
- resources belong to question folder

---

# 7. Future Extensions

Possible future additions:

- statistics.json
- ai_analysis.json
- cache/
- migration tools