# ADR-DOC-001

Title:

Documentation Must Be AI-Transferable

## Status

Accepted

## Context

SciForge-Edu is intended to support long-term development across:

- multiple human contributors
- multiple AI systems
- multiple future AI generations

Project documentation must remain understandable even when read by an AI that has no prior project context or access to previous conversations.

## Decision

Documentation should not rely solely on concise rules or slogans.

Important architectural decisions should include:

- Purpose
- Context
- Decision
- Rationale
- Examples
- Counter Examples
- Implications
- Open Questions

whenever practical.

## Rationale

A future AI may not have access to:

- historical conversations
- architectural discussions
- original design motivations

The documentation itself must preserve architectural intent.

## Good Example

Rule:

Knowledge Points are curriculum-independent.

Rationale:

Curriculum standards may change across curriculum revisions.

Knowledge concepts remain relatively stable.

Example:

Knowledge Point: Newton First Law

114 Curriculum: Eb-IV-8

Future Curriculum: Eb-IV-11

Knowledge Point remains unchanged.

Counter Example:

Renaming a Knowledge Point identifier solely because a curriculum code changed.

## Bad Example

Knowledge Points are curriculum-independent.

(No rationale.)

(No examples.)

(No counter examples.)

## Implications

Future AI systems should be able to reconstruct architectural intent without requiring access to prior conversations.

Architectural reasoning should be portable across AI systems.

## Documentation Template

Future architectural documents should prefer the following structure:

1. Purpose
2. Context
3. Decision
4. Rationale
5. Examples
6. Counter Examples
7. Implications
8. Open Questions

## Consequences

Documentation quality is prioritized over brevity when architectural intent may otherwise be lost.

Human readability and AI transferability are both first-class requirements.
