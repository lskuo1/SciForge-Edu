# Exam Composition Specification v1.0

## Purpose

Define how questions are assembled into an examination.

This specification separates:

- Question
- QuestionGroup
- ExamQuestionInstance
- ExamSection
- ExamPaper

to prevent composition logic from leaking into
question repository objects.

---

# Design Principles

## Principle 1

Question objects must remain reusable.

Exam-specific settings must not modify
the source question.

---

## Principle 2

Exam composition is independent from
question storage.

Repository concerns and composition concerns
must remain separated.

---

## Principle 3

Score override must not modify Question.

The original score stored in Question
is treated as a default recommendation.

---

# Question

Represents a reusable source question.

Owns:

- stem
- choices
- solution
- images
- default points

Does NOT own:

- exam order
- assigned score
- section membership

---

# QuestionGroup

Represents shared materials.

Examples:

- reading passages
- experimental data
- figures
- tables

Contains:

- shared stem
- shared assets
- child questions

---

# ExamQuestionInstance

Represents a question used in a specific exam.

Owns:

- question reference
- assigned points
- display order
- paper version

Examples:

Question:
    default_points = 2

Exam instance:
    assigned_points = 4

The source Question remains unchanged.

---

# ExamSection

Represents a section of an exam.

Examples:

Section A
(2 points each)

Section B
(4 points each)

Owns:

- title
- instructions
- layout options
- question instances

---

# ExamPaper

Represents a complete examination.

Owns:

- metadata
- sections
- rendering settings

Examples:

- school name
- semester
- subject
- exam title

---

# Score Override

Question.default_points

is only a recommendation.

ExamQuestionInstance.assigned_points

is the effective score used during rendering.

---

# Section Grouping Modes

## Mode A

Preserve Question Order

Questions remain in user-defined order.

Example:

Q1
Q2
Q3
Q4

---

## Mode B

Group By Assigned Points

Questions with identical assigned scores
are collected into the same section.

Example:

Section A
(2 points each)

Q1
Q3
Q4

Section B
(4 points each)

Q2

---

# Legacy System Compatibility

Legacy system behavior:

- score override supported
- section generation supported
- consecutive score blocks only

Known limitation:

Questions with identical scores are not
globally collected.

SciForge-Edu may optionally support
global score grouping.

---

# Future Extensions

- answer balancing
- A/B paper generation
- knowledge point statistics
- section analytics