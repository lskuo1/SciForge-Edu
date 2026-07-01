# GF-005-003

## Title

Repository architecture changes require explicit authorization.

---

## Status

Open

---

## Introduced

Sprint 005

---

## Observation

During Sprint 005 governance review activities, an engineering contributor was asked to recommend how repository governance knowledge should be preserved.

The contributor proposed a technically well-reasoned solution that introduced a new repository artifact type together with corresponding modifications to the repository governance architecture.

Although the proposal was technically sound, the task did not authorize repository architecture modifications.

The proposed changes were therefore rejected and rolled back.

---

## Evidence

During Sprint 005 governance review:

- A new repository artifact type was proposed.
- Repository governance documents were modified to integrate the new artifact.
- The requested task did not authorize repository architecture evolution.
- All unauthorized repository modifications were successfully rolled back after Architecture Owner review.

---

## Engineering Impact

This case demonstrates the importance of distinguishing between:

- solving the requested engineering problem; and
- evolving the repository architecture.

Repository architecture should evolve only through explicitly authorized architectural decisions, regardless of the technical quality of a proposed solution.

---

## Recommendation

Repository engineering tasks should clearly distinguish between:

- repository research;
- repository implementation; and
- repository architecture evolution.

If an engineering task reveals that repository architecture should evolve, the proposed architectural changes should be submitted separately through the repository governance workflow rather than implemented as part of the current task.

---

## Resolution

Not yet resolved.

Future repository governance guidance may explicitly define how architecture evolution proposals should be handled when they arise during engineering or governance review activities.