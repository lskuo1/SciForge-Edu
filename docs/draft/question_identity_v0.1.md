# SciForge-Edu Question Identity Specification v0.1

Status: Draft

Version: 0.1

---

# 1. Purpose

This document defines Question Identity within SciForge-Edu.

Question Identity is used to determine whether two Question objects represent the same logical question.

This specification does not define Question Similarity.

---

# 2. Scope

This specification applies to:

* Question identity generation
* Question object tracking
* Workbench operations
* Repository workflows
* Renderer namespace planning

This specification does not apply to:

* Similarity detection
* Duplicate detection
* Semantic search
* AI-assisted content analysis

---

# 3. Identity vs Similarity

Question Identity and Question Similarity are distinct concepts.

Question Identity answers:

> Are these the same Question object?

Question Similarity answers:

> Are these different questions with similar content?

Two questions may have:

* different identities
* high similarity

Identity generation shall not depend on similarity detection.

---

# 4. Question Identity

Every Question shall possess a stable Question Identifier.

The Question Identifier is intended to represent the logical identity of the question.

Question Identity shall remain stable under:

* question reordering
* exam reordering
* answer balancing
* renderer namespace changes
* repository storage location changes

---

# 5. Identity Fields

The following fields participate in Question Identity generation.

## question_type

Question type is part of Question Identity.

Examples:

* single_choice
* multiple_choice
* short_answer

Different question types shall produce different identities.

---

## stem_tex

Question stem content participates in identity generation.

Changes to the stem shall produce a different identity.

---

## choices

Choice content participates in identity generation.

Changes to choice text shall produce a different identity.

---

## choice correctness

Correctness participates in identity generation.

Example:

Choice A is correct

and

Choice B is correct

shall be treated as different questions.

---

# 6. Non-Identity Fields

The following fields shall not participate in Question Identity generation.

## solution

Solutions may change without changing question identity.

Examples:

* typo corrections
* explanation improvements
* additional derivations

shall not generate a new Question Identity.

---

## source_path

File locations shall not affect Question Identity.

Questions moved between directories shall preserve identity.

---

## label

Human-readable labels shall not affect identity.

---

## metadata

Metadata fields shall not affect identity.

Examples:

* difficulty
* curriculum tags
* author information
* repository information

---

## statistics

Statistical data shall not affect identity.

Examples:

* usage counts
* difficulty estimates
* discrimination indices

---

# 7. Choice Order Rule

Choice order shall not affect Question Identity.

The following sequences:

A B C D

and

C A D B

shall be considered equivalent.

Implementations shall normalize choice objects before identity generation.

Answer balancing operations shall not alter Question Identity.

---

# 8. Deterministic Identity Generation

Question Identity shall be generated from a canonical representation of identity fields.

Identity generation shall be deterministic.

Identical canonical representations shall produce identical Question Identifiers.

Different canonical representations shall produce different Question Identifiers.

The specific hashing algorithm is implementation-defined.

Future versions may use different algorithms without changing this specification.

---

# 9. Renderer Namespace

Question Identity and Renderer Namespace are separate concepts.

Question Identity is stable and persistent.

Renderer Namespace is temporary and generated during rendering.

Examples:

Question Identity:

a8f73c9d...

Renderer Namespace:

q0001

q0002

q0003

Renderer Namespace may change between rendering operations.

Question Identity shall not.

---

# 10. Future Work

Future repository workflows may support:

* semantic similarity search
* duplicate detection
* near-duplicate detection
* AI-assisted content clustering

These features are outside the scope of Question Identity v0.1.

Similarity detection shall not affect Question Identity generation.
