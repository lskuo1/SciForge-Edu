
# SciForge-Edu Template API Specification
Version: v1.0
Status: Draft

# 1. Purpose

This document defines template architecture and rendering APIs.

Goals:

- Separate presentation from business logic
- Support built-in and custom templates
- Support extracted templates
- Keep templates stable even if Question Object changes

---

# 2. Template Philosophy

Template = Presentation Layer

Template is NOT:

- business logic
- repository access
- AI service
- file system access

Templates may:

- control layout
- control styles
- control headers/footers
- control teacher/student differences

---

# 3. Template Package Structure

my_template/

├── manifest.json
├── template.tex
├── preview.png
└── assets/

Template package is portable.

---

# 4. Built-in Templates

System templates:

- default_student
- default_teacher
- default_answers

Purpose:

Student:
Formal exam

Teacher:
Detailed solutions

Answers:
Answer tables

---

# 5. Template Sources

Supported:

- Built-in Template
- Imported Template Package
- Extracted Template

Extracted templates require human confirmation.

---

# 6. Render View Model Strategy

Question Object

    ↓

Renderer

    ↓

Render View Model

    ↓

Template

Rule:

Never expose internal Question Objects directly.

---

# 7. Available View Models

class RenderExam:

    title:str
    grade:str
    course:str
    total_score:int

class RenderQuestion:

    number:int
    points:int
    stem:str
    choices:list[str]
    solution:str
    images:list[str]
    question_type:str

class RenderAnswerRow:

    question_number:int
    answer:str
    points:int

---

# 8. Template Syntax

Variables:

[[ exam.title ]]

[[ question.points ]]

[[ question.stem ]]

---

Conditions:

[[ IF teacher_mode ]]

...

[[ ENDIF ]]

---

Loops:

[[ FOR question ]]

...

[[ ENDFOR ]]

---

# 9. Built-in Components

QUESTION_BLOCK

CHOICE_BLOCK

SOLUTION_BLOCK

ANSWER_TABLE

HEADER_BLOCK

FOOTER_BLOCK

---

# 10. Template Validator

Checks:

- missing QUESTION_BLOCK
- invalid variables
- incompatible API version
- unsupported component usage

---

# 11. Export Integration

Output package:

dist/

    student.tex
    teacher.tex
    answers_table.tex

    assets/

All outputs must be independently compilable.

---

# 12. Template Red Line

Forbidden:

- Question mutation
- Repository access
- AI calls
- File system access
- UUID modification

Required:

Use Render View Models only.
