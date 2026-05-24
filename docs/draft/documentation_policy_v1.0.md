
# SciForge-Edu Documentation Policy
Version: v1.0
Status: Draft

# 1. Purpose

This document defines documentation rules for SciForge-Edu.

Goals:

- Keep documents consistent
- Prevent incompatible changes
- Guide future developers
- Guide AI-assisted maintenance
- Preserve architecture integrity

---

# 2. Documentation Categories

System Architecture:

- architecture_map_vX.Y.md
- data_model_spec_vX.Y.md
- repository_spec_vX.Y.md
- parser_grammar_spec_vX.Y.md
- gui_workflow_spec_vX.Y.md
- template_api_spec_vX.Y.md

Authoring:

- question_authoring_spec_vX.Y.md
- naming_convention_vX.Y.md
- examples/

---

# 3. File Naming Rules

Format:

document_name_vMajor.Minor.md

Examples:

data_model_spec_v1.0.md

repository_spec_v1.0.md

parser_grammar_spec_v1.0.md

Forbidden:

data_model_new.md

parser_final_v2.md

test.md

---

# 4. Version Rules

Major version:

Increase when:

- Data Model changes
- Grammar changes
- Breaking architecture changes
- Incompatible modifications

Examples:

v1.0 → v2.0

---

Minor version:

Increase when:

- Clarifications
- New examples
- New warnings
- Small compatible additions

Examples:

v1.0 → v1.1

---

# 5. Dependency Rules

Document dependency:

documentation_policy
        ↓

architecture_map
        ↓

data_model_spec
        ↓

repository_spec
        ↓

parser_grammar_spec
        ↓

gui_workflow_spec

Rules:

Lower layers must not redefine upper layers.

---

# 6. Modification Policy

If data_model_spec changes:

Must review:

- repository_spec
- parser_grammar_spec
- gui_workflow_spec
- migration tools

---

If parser grammar changes:

Must review:

- parser_grammar_spec
- import tools
- migration tools

---

If repository changes:

Must review:

- search
- workspace
- similarity engine
- usage tracking

---

# 7. Change Log Requirement

Each document update must record:

- version
- date
- author
- reason
- affected files

Example:

Version: v1.1

Date: 2026-05-24

Author: Teacher

Reason:

Added Diagnostic Engine

Affected:

parser_grammar_spec
gui_workflow_spec

---

# 8. Architecture Red Line

Forbidden:

- Modify lower layers to redefine upper layers
- Skip dependency review
- Create undocumented system layers
- Change UUID semantics

---

# 9. AI Maintenance Rules

AI must:

- Explain impact scope
- Update dependency graph
- Update versions
- Explain change reason

AI must NOT:

- Change architecture silently
- Modify UUID behavior
- Introduce hidden dependencies
- Modify files without recording changes

---

# 10. Recommended Reading Order

1. documentation_policy_v1.0.md

2. architecture_map_v1.0.md

3. data_model_spec_v1.0.md

4. repository_spec_v1.0.md

5. parser_grammar_spec_v1.0.md

6. gui_workflow_spec_v1.0.md

---

# 11. Long-Term Principle

Documentation defines architecture.

Implementation follows documentation.

Implementation must not redefine documentation.
