# SciForge-Edu API Snapshot Draft v1

## Project Overview

SciForge-Edu

Purpose:

Structured assessment authoring and repository system.

Core domains:

- Question modeling
- Repository management
- Exam workspace workflow
- Import/export pipeline
- Future GUI authoring


---

## Repository Structure

```text
src/
├── diagnostics/
├── gui/
├── importer/
├── models/
├── parser/
├── renderer/
├── repository/
└── workspace/
```


---

## Core Models

### Question

```text
Question
├── uuid: str
├── label: str
├── question_type: str
├── points: int
├── stem_tex: str
├── choices: list[Choice]
├── solution: Solution | None
├── analysis: Analysis | None
├── statistics: list[AssessmentStatistics]
├── source: Source | None
├── current_version: int
├── history: list[Version]
└── extra: dict
```

Responsibilities:

- Store question content
- Connect related models
- Maintain version history

Important notes:

- Question is the core aggregate root
- Question Object is the source of truth
- LaTeX content remains preserved in stem_tex
- Version history is stored inside Question
- Statistics represent observed exam results


### AssessmentStatistics

```text
AssessmentStatistics
├── exam_id: str
├── correct_rate: float | None
├── difficulty_index: float | None
├── discrimination_index: float | None
└── sample_size: int | None
```

Important notes:

- Statistics represent observed performance data
- Statistics are conceptually separate from intrinsic question content


---

## Repository Layer

### RepositoryManager

```text
RepositoryManager
├── save_question()
├── load_question()
├── update_index()
└── search()
```

Responsibilities:

- Persist Question objects
- Maintain repository index
- Support future repository search

Storage structure:

```text
repository_root/
├── questions/
│   └── <uuid>/
│       └── question.json
└── index/
    └── repository_index.json
```

Important notes:

- RepositoryManager operates on storage layer
- Repository structure is filesystem-based
- Repository index is maintained separately from Question storage


---

## Workspace Layer

### WorkspaceDraft

```text
WorkspaceDraft
├── draft_id: str
├── title: str
├── selected_questions: list[str]
├── settings: dict
└── last_modified: datetime
```

Responsibilities:

- Save unfinished exam drafts
- Preserve selected questions
- Preserve exam settings
- Support resume workflow

Important notes:

- WorkspaceDraft represents temporary editing state
- WorkspaceDraft is not finalized Exam data
- WorkspaceDraft supports persistent editing workflow


---

## Parser Layer

### Current Status

```text
parser/
└── question_parser.py
```

Important notes:

- Parser architecture is currently minimal
- Parser expansion is expected in future versions


---

## Documentation Layer

Important specifications currently exist under:

```text
docs/draft/
```

Key specifications:

- repository_spec_v1.1.md
- parser_grammar_spec_v1.0.md
- repository_storage_spec_v0.1.md
- import_pipeline_spec_v1.0.md
- template_api_spec_v1.0.md

Important notes:

- Snapshot should reference specifications selectively
- Snapshot should avoid dumping full documentation content


---

## Architecture Philosophy

Core principles:

- Models represent domain concepts
- Repository layer manages persistence
- Workspace layer manages editing state
- Question is the primary source of truth
- Metadata and statistics remain conceptually separated
- Snapshot files exist to improve AI collaboration context
- Snapshot files are treated as system metadata


---

## Snapshot Generation Direction

Future automatic snapshot generation should prioritize:

1. Core models
2. Repository structure
3. Workspace workflow
4. Public APIs
5. Architecture rules

Automatic snapshot generation should avoid:

- Full repository dumps
- Excessive implementation details
- Large documentation duplication
- Temporary cache data
