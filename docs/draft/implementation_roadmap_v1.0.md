
# SciForge-Edu Implementation Roadmap
Version: v1.0
Status: Draft

# 1. Purpose

This document defines implementation order and development phases.

Goals:

- Prevent architecture violations
- Reduce future refactoring
- Provide implementation guidance
- Support human and AI contributors

---

# 2. Implementation Principle

Core engines first.

GUI later.

AI features last.

Rule:

Implementation follows architecture.

---

# 3. Phase 0 — Governance Layer

Status: Completed

Completed specifications:

- documentation_policy
- architecture_map
- data_model
- provenance
- repository
- parser
- GUI workflow
- template API
- import pipeline

Purpose:

Define system rules.

---

# 4. Phase 1 — Core Data Engine

Implement:

- Question Object
- QuestionVersion
- Provenance
- Repository Object

Output:

Stable internal data structures

Reason:

Everything depends on data models.

---

# 5. Phase 2 — Parser Engine

Implement:

- Lexer
- Parser
- Validator
- Diagnostic Engine

Pipeline:

question.tex

↓

Question Object

---

# 6. Phase 3 — Repository Engine

Implement:

- Question Store
- Search Engine
- Similarity Engine
- Version Tracking

Purpose:

Question lifecycle management

---

# 7. Phase 4 — Workspace Layer

Implement:

- Workspace Copy
- Autosave
- Restore
- Draft Management

Purpose:

Prevent repository pollution

---

# 8. Phase 5 — Renderer Engine

Implement:

- Render View Models
- Template Renderer
- Template Validator

Pipeline:

Question Object

↓

student.tex
teacher.tex
answers_table.tex

---

# 9. Phase 6 — Sandbox Compile

Implement:

- XeLaTeX Sandbox
- Asset Copy
- Path Rewriter
- Compile Error Capture

Pipeline:

.tex

↓

PDF

---

# 10. Phase 7 — Import System

Implement:

- Importer
- Normalizer
- Human Review
- AI Analysis

Purpose:

Reuse existing educational assets

---

# 11. Phase 8 — GUI Layer

Implement:

- Exam Builder
- Repository Manager
- Template Manager
- Import Tool

Rule:

GUI wraps core engines.

GUI must not redefine architecture.

---

# 12. Phase 9 — AI Features

Implement:

- AI Solution Generator
- AI Difficulty Analysis
- AI Tagging
- Template Extractor

Rule:

AI features depend on stable core systems.

---

# 13. Long-Term Principle

Architecture

↓

Core Engine

↓

Workflow

↓

GUI

↓

AI

Never reverse this order.
