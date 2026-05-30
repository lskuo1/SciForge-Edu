# Renderer Architecture v0.1

Status:

Draft

## Purpose

Define the responsibilities and boundaries of the Renderer subsystem.

The Renderer subsystem transforms parsed exam content into standalone LaTeX documents and PDF outputs.

Renderer is a production subsystem.

Renderer is not responsible for question parsing, repository management, or educational analysis.

---

## Responsibilities

Renderer is responsible for:

* Template loading
* Template rendering
* Exam document generation
* Answer sheet generation
* Teacher version generation
* PDF compilation
* Output artifact management
* Figure synchronization

Examples:

* student.tex
* teacher.tex
* answer_table.tex
* PDF outputs

---

## Non-Responsibilities

Renderer must not perform:

* Question parsing
* Repository indexing
* Knowledge Point analysis
* Curriculum mapping
* Question import workflows
* Educational diagnostics

These concerns belong to other subsystems.

---

## Current Scope

Renderer v0.1 supports:

* LaTeX rendering
* XeLaTeX compilation
* Output bundle generation

Renderer currently assumes:

* Questions are already parsed.
* Data structures are already validated.

---

## Future Expansion

Potential future components:

```text
renderer/

├── compiler.py
├── template_manager.py
├── output_bundle.py
├── pdf_service.py
└── asset_manager.py
```

Future features:

* Multiple templates
* A/B exam generation
* Question group rendering
* Print layout optimization

---

## Design Principle

Renderer should focus on output generation only.

Input preparation belongs to upstream subsystems.

Renderer consumes structured data and produces publication-ready artifacts.
