
# SciForge-Edu Repository Specification
Version: v1.0
Status: Draft

# 1. Repository Role

Question Repository is NOT the question itself.

Question Repository = Question Asset Management Layer

Responsibilities:

- Question indexing
- Search
- Version management
- Similarity checking
- Usage tracking
- AI analysis storage
- Import normalization

Repository must be rebuildable.

Question source files remain the primary assets.

---

# 2. Question Sources

Supported sources:

1. GUI New Question
2. External Import
3. Repository Search
4. Publisher Content
5. Past Exam Import

All sources become:

Raw Question
    ↓
Question Object

---

# 3. Import Pipeline

Raw Question
    ↓
Normalizer
    ↓
Question Object
    ↓
Analysis Engine
    ↓
Similarity Check
    ↓
Repository Update

Notes:

- Parser only accepts SciForge question format.
- Import tools may accept PDF, Word, old tex, publisher content, CSV, etc.

---

# 4. Question Lifecycle

Create / Import
        ↓

Question Object
        ↓

Repository
        ↓

Workspace Draft
        ↓

Teacher edits
        ↓

Decision:

□ Save only in current exam

□ Update repository version

        ↓

Exam Builder

---

# 5. Workspace System

Working drafts must NOT immediately modify repository questions.

Structure:

workspace/

    1141_midterm/

        draft.json

Purpose:

- Allow repeated exam editing
- Prevent repository pollution
- Preserve exam history

---

# 6. Repository Index Model

Example:

class QuestionIndex:

    uuid:str

    label:str

    question_type:str

    subject:str

    analysis:dict

    source_path:str

    current_version:int

    usage_count:int

Repository index stores:

- metadata
- search information
- path information

Repository index does NOT store:

- complete question content
- images

---

# 7. Similarity System

Purpose:

Prevent duplicate questions.

Initial version:

Fingerprint-based

Future:

Embedding / AI semantic matching

Rules:

- Similarity only provides suggestions
- Similarity never auto-merges questions

GUI example:

Possible duplicate:

Q-a72f (95%)

Options:

□ Treat as new question

□ Create new version

□ Use current repository question

□ Temporary use only

---

# 8. Version System

Question:

Q-a72f

    v1
    v2
    v3

Repository versions represent meaningful evolution.

Minor exam drafting changes:

Do NOT automatically create repository versions.

---

# 9. Usage Tracking

Example:

QuestionUsage:

{

uuid:"Q-a72f",

used_in:[

{
exam_id:"1141_midterm",
date:"2026-06-15"
},

{
exam_id:"115_mock_3",
date:"2026-10-05"
}

]

}

Purpose:

- avoid repeated exams
- exam statistics
- question popularity
- future analytics

# 9.5 Assessment Statistics

Question may accumulate multiple
assessment records across exams.

Example:

QuestionStatistics:

{

uuid:"Q-a72f",

records:[

{

exam_id:"1141_midterm",

correct_rate:0.62,

difficulty_index:0.38,

discrimination_index:0.48,

sample_size:240

},

{

exam_id:"115_mock_3",

correct_rate:0.84,

difficulty_index:0.16,

discrimination_index:0.31,

sample_size:180

}

]

}

Notes:

- Statistics belong to exam observations
- Statistics are NOT intrinsic question properties
- Multiple statistics records may exist
- Statistics may be imported from OMR systems


---

# 10. Origin Metadata

QuestionOrigin:

source_type

source_name

year

exam_name

question_number

publisher

Examples:

Past exam:

{

source_type:"exam",

source_name:"教育會考",

year:112,

question_number:17

}

Publisher:

{

source_type:"publisher",

source_name:"翰林"

}

Teacher:

{

source_type:"teacher",

source_name:"Teacher"

}

---

# 11. Repository Red Line

Forbidden:

- Directly overwrite old versions
- Delete questions already used by exams
- AI automatically merge questions
- Workspace drafts directly modify repository

Allowed:

- AI add analysis
- AI suggest duplicate questions
- AI update metadata

