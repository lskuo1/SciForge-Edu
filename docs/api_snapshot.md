# SciForge API Snapshot

## Core Models

### Analysis

```text
├── difficulty_score: float | None
├── difficulty_level: int | None
├── subject: str | None
├── chapter: str | None
├── tags: list
├── misconceptions: list
└── provenance: src.models.provenance.Provenance | None
```

Description:

Question analysis metadata.

### Choice

```text
├── text_tex: str
├── is_correct: bool
└── explanation: str | None
```

Description:

Multiple-choice option.

### Provenance

```text
├── source_type: Literal
├── source_name: str
├── created_by: str
├── created_at: datetime
├── based_on: str | None
├── model_version: str | None
├── confidence: float | None
├── note: str | None
└── revision_history: list
```

Description:

Track where content originates.

### Revision

```text
├── timestamp: datetime
├── editor: str
├── editor_type: str
└── note: str | None
```

Description:

Record modification history.

### AssessmentStatistics

```text
├── exam_id: str
├── correct_rate: float | None
├── difficulty_index: float | None
├── discrimination_index: float | None
└── sample_size: int | None
```

### Question

```text
├── uuid: str
├── label: str
├── question_type: str
├── points: float
├── stem_tex: str
├── choices: list
├── solution: src.models.solution.Solution | None
├── analysis: src.models.analysis.Analysis | None
├── statistics: list
├── source: src.models.source.Source | None
├── current_version: int
├── history: list
└── extra: dict
```

Description:

Core Question Object.

### Solution

```text
├── content_tex: str
├── provenance: Provenance
└── is_verified: bool
```

Description:

Detailed solution/explanation.

### Source

```text
├── file_path: str
└── raw_tex: str
```

Description:

Original source information.

### Version

```text
├── version: int
├── timestamp: datetime
├── author: str
└── change_note: str
```

Description:

Question version information.
