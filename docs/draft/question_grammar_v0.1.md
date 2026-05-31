# SciForge-Edu Question Grammar v0.1

Status: Draft

Version: 0.1

Last Updated: 2026-05

---

# Purpose

This document defines the canonical question grammar used by SciForge-Edu.

The grammar serves as:

* repository storage format
* AI authoring format
* parser input format
* composer input format

The grammar is designed as a LaTeX-compatible DSL.

Future versions may provide:

```
\usepackage{sciforge}
```

to compile the grammar directly.

---

# Design Principles

## Principle 1

Human-readable.

Teachers should be able to read and edit question files directly.

---

## Principle 2

AI-friendly.

Large language models should be able to generate valid question files with minimal prompting.

---

## Principle 3

LaTeX-compatible.

New constructs should resemble standard LaTeX environments whenever possible.

---

## Principle 4

Renderer-independent.

Grammar defines structure and meaning.

Visual appearance is determined by renderers and templates.

---

# Supported Objects

Version 0.1 supports:

* Question
* Choices
* Solution
* QuestionGroup
* GroupStem
* Images
* Tables

---

# Single Question

Example:

```latex
\question

下列何者為鹽酸？

\begin{choices}

\choice NaOH

\CorrectChoice HCl

\choice NaCl

\choice H2O

\end{choices}
```

---

# Choices

A question must contain:

```latex
\begin{choices}
...
\end{choices}
```

---

# Correct Answer

Exactly one:

```latex
\CorrectChoice
```

must appear inside a choices environment.

Valid:

```latex
\choice A

\CorrectChoice B

\choice C

\choice D
```

Invalid:

```latex
\choice A

\choice B

\choice C

\choice D
```

No correct answer specified.

Invalid:

```latex
\CorrectChoice A

\CorrectChoice B
```

Multiple correct answers.

---

# Solution

Optional.

Valid:

```latex
\begin{solution}

詳解內容

\end{solution}
```

Questions may omit the solution environment.

Example:

```latex
\question

...

\begin{choices}
...
\end{choices}
```

is valid.

---

# Question Group

QuestionGroup represents multiple questions sharing a common context.

Example:

```latex
\begin{questiongroup}

\begin{groupstem}

閱讀下列資料後回答問題。

\end{groupstem}

\question
...

\question
...

\end{questiongroup}
```

---

# GroupStem

GroupStem contains shared content.

Typical contents:

* reading passages
* experimental descriptions
* images
* tables
* diagrams
* datasets

Example:

```latex
\begin{groupstem}

閱讀下列實驗資料。

\includegraphics{images/example.png}

\end{groupstem}
```

---

# GroupStem Rendering Hint

Optional rendering hints may be provided.

Example:

```latex
\begin{groupstem}[boxed]

閱讀下列資料。

\end{groupstem}
```

Meaning:

Renderer should visually emphasize the group stem.

The exact appearance is renderer-dependent.

---

# Shared Resources

Shared resources should be placed inside GroupStem.

Examples:

* shared text
* shared images
* shared tables
* shared diagrams
* shared experimental data

Recommended:

```latex
\begin{groupstem}

共享資料

\end{groupstem}
```

instead of placing shared content directly in QuestionGroup.

---

# Images

Example:

```latex
\includegraphics[width=0.5\textwidth]{images/sample.png}
```

Images may appear:

* inside Question
* inside GroupStem

Relative paths are recommended.

---

# Tables

Example:

```latex
\begin{tabular}{cc}

A & B \\

1 & 2

\end{tabular}
```

Tables may appear:

* inside Question
* inside GroupStem

---

# Workbench Scope

Workbench operates on exam instances.

Workbench may modify:

* question selection
* question order
* score assignment
* answer balancing

Workbench does not modify:

* question stem
* choice text
* solution content
* group stem content

---

# Open Questions

The following items are intentionally left undecided in v0.1:

* metadata syntax
* difficulty tags
* source tags
* curriculum tags
* point annotations
* parser requirements for GroupStem
* additional rendering hints

These topics will be addressed in future versions.
