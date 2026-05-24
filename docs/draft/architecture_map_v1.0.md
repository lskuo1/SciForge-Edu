
# SciForge-Edu Architecture Map
Version: v1.0
Status: Draft

# 1. Purpose

This document defines the global architecture of SciForge-Edu.

Purpose:

- Explain system layers
- Explain dependency relationships
- Guide future developers
- Guide AI-assisted maintenance
- Prevent cross-layer violations

---

# 2. Layer Architecture

SciForge-Edu

├── Import Layer
│
│   Raw PDF
│   Raw Word
│   Old LaTeX
│   Publisher Content
│   Past Exams
│
│       ↓
│
│   Normalizer
│
├── Parser Layer
│
│   Lexer
│   Parser
│   Validator
│   Diagnostic Engine
│
│       ↓
│
│   Question Object
│
├── Repository Layer
│
│   Search
│   Similarity
│   Version
│   Usage Tracking
│   Analysis
│
├── Workspace Layer
│
│   Draft Editing
│   Temporary Modifications
│
├── Exam Layer
│
│   Exam Builder
│   Shuffle
│   Question Selection
│
├── Export Layer
│
│   Template Renderer
│   XeLaTeX Sandbox
│
└── Output
    │
    student.pdf
    teacher.pdf
    analysis_report.pdf

---

# 3. Document Dependency Graph

architecture_map
        ↓

data_model_spec
        ↓

repository_spec
        ↓

parser_grammar_spec
        ↓

gui_workflow_spec

Additional:

template_api_spec
        ↓

sandbox_spec

---

# 4. Runtime Dependency Graph

Raw Question
      ↓

Normalizer
      ↓

Question Object
      ↓

Repository
      ↓

Workspace
      ↓

Exam Builder
      ↓

Template Renderer
      ↓

XeLaTeX Sandbox
      ↓

PDF

---

# 5. Core Source of Truth

Question Object

is the only Source of Truth.

LaTeX:

- import format
- export format

LaTeX is NOT the primary data structure.

---

# 6. Architecture Red Line

Forbidden:

GUI
    → Parser write

Assembler
    → Repository write

AI
    → UUID modify

AI
    → Version history rewrite

Parser
    → Rendering

Repository
    → Question mutation without versioning

---

Allowed:

Parser
    → Question Object

Repository
    → Search

GUI
    → Workspace

Workspace
    → Repository update request

Export Layer
    → Read-only Question access

---

# 7. Modification Policy

If Question Object changes:

Must review:

- repository_spec
- parser_grammar_spec
- GUI workflow
- migration tools

---

If Question Grammar changes:

Must review:

- parser_grammar_spec
- import tools
- migration tools

---

If Repository structure changes:

Must review:

- search
- similarity engine
- workspace
- usage tracking

---

# 8. Recommended Reading Order

1. architecture_map_v1.0.md

2. data_model_spec_v1.0.md

3. repository_spec_v1.0.md

4. parser_grammar_spec_v1.0.md

5. gui_workflow_spec_v1.0.md

---

# 9. Long-Term Principle

Implementation follows architecture.

Architecture does not follow implementation.
