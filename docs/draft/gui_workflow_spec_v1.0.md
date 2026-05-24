
# SciForge-Edu GUI Workflow Specification
Version: v1.0
Status: Draft

# 1. Purpose

This document defines teacher workflows and GUI behavior.

GUI does NOT define architecture.

GUI follows architecture.

---

# 2. Startup Screen

System startup options:

□ New Exam

□ Open Existing Exam

□ Continue Unfinished Workspace

□ Repository Manager

□ Import Tool

Purpose:

- avoid forced empty projects
- support long-term exam editing
- support repository maintenance

---

# 3. New Exam Workflow

Create exam:

Required metadata:

- Semester
- Exam name
- Subject
- Grade
- Test range
- Total score

Reason:

These values affect:

- Repository filtering
- AI analysis
- Search
- Export

---

# 4. Question Sources

Supported:

□ Import external questions

□ Repository search

□ Create new question

All imported questions first enter:

Question Pool

Question Pool is independent.

Questions do NOT immediately enter exam.

Purpose:

- filtering
- preview
- batch editing

---

# 5. Workspace Layer

Workflow:

Repository Question

Q-a72f v2

        ↓

Copy

        ↓

Workspace Copy

W-a72f

All modifications apply only to:

Workspace Copy

NOT:

Repository Question

---

# 6. Editing Modes

Supported modes:

□ Metadata View

□ Question Editing

□ Preview Mode

□ Advanced Source View

Definitions:

Metadata View:

- points
- labels
- analysis

Question Editing:

- question content
- choices
- images

Preview Mode:

Shows actual exam appearance

Advanced Source View:

Allows direct LaTeX editing

---

# 7. Version Update Policy

Workspace edits do NOT automatically update repository.

Teacher chooses:

□ Use only in current exam

□ Save back as repository version

If saved:

Q-a72f

v2
↓
v3

System requires:

Change note:

_________________

---

# 8. Workspace Persistence

Workspace automatically saves.

Structure:

workspace/

    1141_midterm/

        workspace.json

Purpose:

- resume unfinished work
- avoid data loss
- support repeated editing

---

# 9. Export Workflow

Generate options:

☑ student.tex

☑ teacher.tex

☑ answers_table.tex

☑ student.pdf

☑ teacher.pdf

☑ analysis_report.pdf

Primary deliverables:

- student.tex
- teacher.tex
- answers_table.tex

PDF outputs are secondary.

---

# 10. GUI Red Line

Forbidden:

- GUI directly modifies repository files

- GUI modifies UUID

- GUI bypasses workspace

- GUI writes directly to parser

Required:

- GUI edits workspace only

- GUI shows repository versions

- GUI provides restore capability

- GUI supports reopening unfinished work
