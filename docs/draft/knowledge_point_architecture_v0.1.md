# Knowledge Point Architecture v0.1

## Purpose

Define a curriculum-independent knowledge point architecture for SciForge-Edu.

The architecture should:

- support human communication
- support AI-assisted question generation
- support repository search
- support curriculum mapping
- remain stable across curriculum revisions


## Context

SciForge-Edu questions must be understandable by:

- teachers
- students
- publishers
- AI systems

Current curriculum standards may change over time.

Knowledge concepts are generally more stable than curriculum codes.

Therefore knowledge concepts and curriculum mappings should be modeled separately.


## Decision

### ADR-KP-001

Knowledge Point names are human-facing.

Knowledge Point codes are system-facing.

Human communication takes priority.


### ADR-KP-002

Knowledge Points are curriculum-independent.

Curriculum mappings are a separate layer.


### ADR-KP-003

Question identity and knowledge identity are separate concerns.

Question UUIDs should not encode knowledge semantics.


### ADR-KP-004

Knowledge Point granularity is defined by diagnosability.

A Knowledge Point is the smallest concept unit that can be independently assessed.

Student diagnosability takes priority over textbook structure.


## Knowledge Point Granularity

### Definition

A Knowledge Point is:

> The smallest concept unit that can be independently diagnosed in a learner.

A student should be able to:

- understand it
- misunderstand it
- master it
- fail it

independently of neighboring concepts.


### Good Examples

Knowledge Points:

- 牛頓第一運動定律
- 慣性
- 牛頓第二運動定律
- 牛頓第三運動定律
- 靜摩擦力
- 動摩擦力
- 受力分析

Each can be assessed independently.


### Counter Examples

Not Knowledge Points:

- 力與運動
- 力學
- 摩擦力

These are usually concept groups or chapter-level topics.

They are too broad for reliable diagnosis.


### Diagnostic Test

A candidate concept is a Knowledge Point if the following question is meaningful:

"Can a student understand this concept while misunderstanding another nearby concept?"

If the answer is yes, the concept should likely become its own Knowledge Point.


## Proposed Model

### Knowledge Point

```text
KnowledgePoint
├── code
├── name
├── aliases
├── curriculum_codes
└── description
```

Example:

```text
code:
KP-PHY-MEC-001

name:
牛頓第一運動定律

aliases:
- Newton First Law
- 慣性定律

curriculum_codes:
- Eb-IV-8

description:
若物體所受合力為零，
則保持靜止或等速度直線運動。
```


### Question

```text
Question
└── knowledge_codes
```

Example:

```python
knowledge_codes=[
    "KP-PHY-MEC-001",
    "KP-PHY-MEC-002"
]
```


## Rationale

### Why not use curriculum codes directly?

Curriculum codes may change across curriculum revisions.

Knowledge concepts are expected to remain relatively stable.

The system should preserve knowledge identity even when curriculum mappings change.


### Why not encode knowledge in UUID?

UUIDs represent identity.

Knowledge Points represent meaning.

Mixing the two creates instability when naming or curriculum structures evolve.


## Implications

Future systems may support:

- knowledge-based search
- curriculum-based search
- prerequisite graphs
- misconception tracking
- adaptive assessment
- AI question generation


## Repository Integration

Future Analysis model may include:

```python
knowledge_codes: list[str]
curriculum_codes: list[str]
```

Repository Query v2 may support:

```python
search(
    knowledge_codes=[...]
)
```

and

```python
search(
    curriculum_codes=[...]
)
```


## Open Questions

1. Should Knowledge Points support hierarchical structures?

2. Should prerequisite relationships be modeled explicitly?

3. Should misconceptions become first-class entities?

4. Should curriculum mappings support multiple curriculum versions simultaneously?

5. How should cross-disciplinary Knowledge Points be represented?

6. Should Skill Points be modeled separately from Knowledge Points?
