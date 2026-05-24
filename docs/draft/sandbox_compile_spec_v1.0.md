
# SciForge-Edu Sandbox Compile Specification
Version: v1.0
Status: Draft

# 1. Purpose

This document defines secure compilation behavior for exported LaTeX packages.

Goals:

- Generate independently compilable outputs
- Isolate compilation environments
- Capture useful errors
- Protect system resources
- Support debugging

---

# 2. Sandbox Philosophy

Compilation environment:

may:

- compile generated outputs
- copy required assets
- rewrite paths
- capture logs

Sandbox may NOT:

- modify repository data
- access external systems
- access arbitrary local files
- modify source question files

---

# 3. Compilation Pipeline

Question Object
        ↓

Renderer
        ↓

Export Package

    student.tex
    teacher.tex
    answers_table.tex
    assets/

        ↓

Sandbox Compile

        ↓

PDF

---

# 4. Export Package Rules

Output package structure:

dist/

    exam_name/

        student.tex
        teacher.tex
        answers_table.tex

        assets/

            img_001.png
            fig_023.svg

Rules:

- package must be self-contained
- package must compile independently
- package must not depend on repository paths
- package must not depend on workspace paths

---

# 5. Path Rewrite Rules

Original:

questions/biology/q001/fig1.png

Rewrite:

assets/bio_q001_fig1.png

Purpose:

- avoid filename collisions
- preserve portability

---

# 6. Supported Compiler

Primary:

XeLaTeX

Future possible:

- LuaLaTeX
- PDFLaTeX

Rule:

Generated outputs must preserve XeLaTeX compatibility.

---

# 7. Compile Diagnostics

Capture:

- missing files
- missing packages
- syntax errors
- image problems
- timeout errors

Diagnostic object:

class CompileDiagnostic:

    severity:str

    file:str

    line:int

    message:str

    suggestion:str

---

# 8. GUI Requirements

GUI should:

- display compile progress
- display diagnostics
- jump to source locations
- allow recompilation

---

# 9. Resource Limits

Example:

Compilation timeout:

30 seconds

Memory:

512MB

Maximum image count:

configurable

Purpose:

Prevent runaway compilation.

---

# 10. Sandbox Red Line

Forbidden:

- execute arbitrary shell commands
- access repository directly
- modify original files
- access network resources

Required:

Compilation failures must provide actionable diagnostics.
