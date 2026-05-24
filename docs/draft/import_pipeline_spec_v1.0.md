
# SciForge-Edu Import Pipeline Specification
Version: v1.0
Status: Draft

# 1. Purpose

This document defines the import pipeline for converting external content into Question Objects.

Goals:

- Reuse existing educational assets
- Standardize imported content
- Preserve provenance
- Support human review
- Prevent repository pollution

---

# 2. Supported Sources

Supported inputs:

- PDF
- DOCX
- Existing LaTeX
- Plain text
- CSV
- Publisher content
- Past exam collections
- Raw question files

---

# 3. Import Philosophy

Import Tool:

may:

- detect
- analyze
- normalize
- suggest

Import Tool may NOT:

- silently modify repository
- silently create versions
- silently overwrite teacher content

Human makes final decisions.

---

# 4. Import Pipeline

Raw Content
        ↓

Importer
        ↓

Normalizer
        ↓

Question Candidate
        ↓

AI Analysis (optional)
        ↓

Similarity Check
        ↓

Human Review
        ↓

Repository Update

---

# 5. Raw Question Object

class RawQuestion:

    source:str

    raw_text:str

    raw_answer:str

    raw_solution:str

    attachments:list

---

# 6. Normalization

Normalizer responsibilities:

- identify question boundaries
- identify choices
- identify answers
- identify solutions
- identify images
- identify metadata

Normalizer does NOT:

- invent answers
- invent missing content
- overwrite content

---

# 7. AI Analysis (Optional)

May suggest:

- subject
- chapter
- difficulty
- tags
- misconceptions

Must include:

- confidence score
- provenance

---

# 8. Similarity Integration

Purpose:

Prevent duplicate questions.

Rules:

- suggestions only
- never auto merge

GUI example:

Possible duplicate:

Q-a72f (95%)

□ Treat as new question
□ Create new version
□ Use existing question
□ Temporary use only

---

# 9. Human Review Workflow

Display:

- detected metadata
- AI suggestions
- similarity results
- provenance
- warnings/errors

Teacher decides:

□ Accept
□ Modify
□ Reject
□ Temporary use only

---

# 10. Provenance Requirements

Imported content must preserve:

- source
- import date
- importer
- model information
- revisions

---

# 11. Import Red Line

Forbidden:

- automatic repository insertion
- automatic answer generation
- automatic version creation
- silent content modification

Required:

System may suggest.

Human must decide.
