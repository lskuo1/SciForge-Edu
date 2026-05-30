# Current System Audit v0.3

## Purpose

Audit the legacy ExamGenerationSystem v0.6 and
identify:

- implemented capabilities
- absorbed capabilities
- partially absorbed capabilities
- future integration targets

---

# Legacy System Functional Audit

## Overview

Legacy system status:

- production-tested
- used for real school examinations
- supports PDF generation
- supports answer balancing
- supports score grouping
- supports student/teacher paper generation

---

## Capability Matrix

| Capability | Legacy | SciForge | Status |
|------------|---------|----------|---------|
| Question Parsing | ✓ | ✓ | Absorbed |
| Multi-question Parsing | ✓ | ✓ | Absorbed |
| Student Paper | ✓ | ✓ | Absorbed |
| Teacher Paper | ✓ | ✓ | Absorbed |
| Template System | ✓ | Partial | In Progress |
| PDF Compilation | ✓ | ✗ | Not Yet |
| Answer Table | ✓ | ✗ | Not Yet |
| Answer Balancing | ✓ | ✗ | Not Yet |
| Score Override | ✓ | ✗ | Not Yet |
| Score Grouping | ✓ | ✗ | Not Yet |
| Question Reordering | ✓ | ✗ | Not Yet |
| Figure Copying | ✓ | ✗ | Not Yet |
| Question Groups | ✗ | Partial | New Capability |
| Knowledge Points | ✗ | Planned | New Capability |
| Repository System | ✗ | Partial | New Capability |

---

# Legacy GUI Workflow

## Workflow

Teacher:

1. Import questions
2. Reorder questions
3. Override scores
4. Generate sections
5. Balance answers
6. Generate student paper
7. Generate teacher paper
8. Generate answer table
9. Compile PDF

---

# Legacy Composition Model

## Observed Behavior

The legacy system implicitly contains:

- Exam
- Section
- Question Instance

although these concepts are not explicitly modeled.

Example:

Section A
(2 points each)

Q1
Q2
Q3

Section B
(4 points each)

Q4
Q5

Section C
(2 points each)

Q6
Q7

The grouping logic is based on
consecutive score blocks.

---

## Identified Limitation

Questions with identical scores are not
globally collected.

Example:

Q1 2 pts
Q2 2 pts
Q3 4 pts
Q4 2 pts

Current output:

Section 1
Q1
Q2

Section 2
Q3

Section 3
Q4

Desired optional behavior:

Section 1
Q1
Q2
Q4

Section 2
Q3

---

# Proposed SciForge Composition Model

## Question

Represents the source question.

Must remain independent of exam layout.

---

## QuestionGroup

Represents shared stem/data.

Must remain independent of scoring.

---

## ExamQuestionInstance

Represents a question used in a specific exam.

Owns:

- assigned score
- display order
- paper version
- inclusion state

---

## ExamSection

Represents:

- title
- score rule
- layout rule

Contains:

- ExamQuestionInstances

---

## ExamPaper

Represents a complete examination.

Contains:

- metadata
- sections
- rendering configuration

---

# Absorption Strategy

Priority 1

- PDF compilation
- Answer table
- Figure export

Priority 2

- Score override
- Answer balancing
- Question reordering

Priority 3

- Explicit ExamSection model
- Explicit ExamPaper model

Priority 4

- Knowledge point integration