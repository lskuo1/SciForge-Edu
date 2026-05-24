
# SciForge-Edu Provenance Specification
Version: v1.0
Status: Draft

# 1. Purpose

This document defines provenance tracking rules.

Goals:
- Preserve content origin
- Preserve attribution
- Preserve revision history
- Support AI-assisted workflows
- Support human accountability

# 2. Human Authority Principle

System may:
- suggest
- analyze
- prepare

Human must:
- review
- approve
- decide

# 3. Provenance Philosophy

System must answer:

Who created this?
Who modified this?
When?
Based on what?
Why did it change?

# 4. Provenance Object

class Provenance:

    source_type:str
    source_name:str
    created_by:str
    created_at:datetime
    based_on:str
    model_version:str
    confidence:float
    note:str
    revision_history:list

# 5. Revision Object

class Revision:

    timestamp:datetime
    editor:str
    editor_type:str
    note:str

# 6. Supported Source Types

teacher
ai
publisher
imported
system
edited
template_extractor

# 7. Provenance Lifecycle

Create
↓
Generate
↓
Human Review
↓
Edit
↓
Version Update

# 8. Integration Points

Question
Solution
QuestionAnalysis
Template Extraction
Import Pipeline
Repository
Workspace

# 9. GUI Requirements

Display:
- Content source
- Creator
- Creation time
- Last editor
- Revision history

# 10. Red Line

Forbidden:
- remove AI attribution
- overwrite revision history
- hide creator information
- silently overwrite teacher content

Required:
Generated content must preserve provenance.
