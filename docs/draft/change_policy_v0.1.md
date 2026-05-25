# Change Policy
Version: v0.1
Status: Draft

Rules:

1. Do not directly modify multiple files at once.

2. Modify one module at a time.

3. Run tests after every change.

4. Commit immediately after a stable state.

5. Prefer adding tests before refactoring.

6. Explain WHY in commit messages.

# Source of Truth Rules

When modifying code:

1. Never assume model fields from memory.

2. Before changing parser, repository,
   renderer, or GUI code:

   Open related model files.

3. Model definitions are the single source
   of truth.

Priority:

models/*.py

↓

specification documents

↓

tests

↓

memory/discussion