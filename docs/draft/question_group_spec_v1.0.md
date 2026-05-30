# Question Group Specification v1.0

Status:

Draft

## Purpose

Define the standard representation of question groups.

A QuestionGroup represents a shared stimulus that is referenced by multiple questions.

Typical examples include:

* Reading comprehension
* Experimental descriptions
* Data analysis tasks
* Shared diagrams
* Shared tables
* Literacy-oriented assessment items

---

## Design Principles

### Principle 1

QuestionGroup is a container.

QuestionGroup contains:

* Shared material
* Shared figures
* Shared tables
* Multiple Question objects

### Principle 2

QuestionGroup is not a Question.

QuestionGroup and Question are different object types.

### Principle 3

Questions remain independently assessable.

Each child Question must be answerable and scorable independently.

### Principle 4

Shared content appears exactly once.

Shared content must not be duplicated into each child Question.

---

## Standard LaTeX Format

```latex
\begin{questiongroup}

\groupstem{

閱讀下列文章後回答問題：

......

}

\begin{questions}

\question ...

\begin{choices}
...
\end{choices}

\question ...

\begin{choices}
...
\end{choices}

\end{questions}

\end{questiongroup}
```

---

## Boxed Group Stem

QuestionGroup may optionally request boxed rendering.

Example:

```latex
\begin{questiongroup}[boxed]

\groupstem{

......

}

...

\end{questiongroup}
```

Meaning:

* group stem
* figures
* tables

should be rendered as a single visual block.

---

## Shared Figures

Shared figures belong inside groupstem.

Example:

```latex
\groupstem{

觀察下圖：

\includegraphics{assets/experiment01.png}

}
```

Shared figures must not be duplicated across child questions.

---

## Shared Tables

Shared tables belong inside groupstem.

Example:

```latex
\groupstem{

\begin{tabular}{...}
...
\end{tabular}

}
```

Shared tables must not be duplicated across child questions.

---

## Child Questions

Each child question follows the standard Question specification.

Example:

```latex
\question ...

\begin{choices}
...
\CorrectChoice ...
...
\end{choices}

\begin{solution}
...
\end{solution}
```

---

## Renderer Requirements

Renderer shall:

1. Render groupstem once.

2. Render child questions immediately after groupstem.

3. Preserve ordering.

4. If boxed option is enabled,
   render groupstem as a single visual block.

5. Child questions shall remain independently numbered.

Example:

閱讀材料

(共用文章)

21.
22.
23.

---

## GUI Requirements

QuestionGroup is the smallest drag-and-drop unit.

Moving a QuestionGroup moves all child questions.

QuestionGroup may be collapsed or expanded.

---

## AI Validation Rules

Rule 1

If multiple questions reference the same article,
table, diagram, or experiment description,

AI should recommend conversion to QuestionGroup.

Rule 2

Shared material must appear in groupstem.

Rule 3

Identical paragraphs must not be copied into each child question.

Rule 4

QuestionGroup must contain at least one Question.

Rule 5

QuestionGroup may not contain another QuestionGroup.

Nested QuestionGroup is prohibited in v1.x.

---

## Future Metadata

Reserved fields:

* group_uuid
* group_source
* knowledge_points
* curriculum_codes

These fields are optional and not required in v1.0.

---

## Migration Guidance

When converting legacy exams:

Before:

Article

Q1

Q2

Q3

After:

QuestionGroup
├── groupstem
├── Q1
├── Q2
└── Q3

This representation is preferred for repository storage, AI processing, rendering, and educational analysis.
