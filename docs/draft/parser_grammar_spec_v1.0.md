
# SciForge-Edu Parser Grammar Specification
Version: v1.1
Status: Draft

# 1. Parser Philosophy

Parser does NOT understand LaTeX semantics.

Parser only understands structure.

Parser responsibilities:

✓ Read metadata  
✓ Find question boundaries  
✓ Find choice boundaries  
✓ Find solution boundaries  
✓ Find group boundaries  
✓ Build AST  
✓ Validate structure  

Forbidden:

✗ Rendering  
✗ Shuffle  
✗ AI analysis  
✗ Auto-fix missing fields  
✗ Modify source tex  
✗ Guess user intent  

Core principle:

Parser should fail rather than guess.

---

# 2. Parser Architecture

Input File
    ↓
Lexer
    ↓
Parser
    ↓
Validator
    ↓
Diagnostic Engine
    ↓
Question Object

---

# 3. Supported Input

Supported:

- question.tex
- group_question.tex

Output:

Question Object

---

# 4. Formal Grammar

## Single Question

QuestionFile ::=

    MetadataBlock
    QuestionBlock
    ChoicesBlock
    SolutionBlock?

---

MetadataBlock ::=

    MetadataLine+

MetadataLine ::=

    "%" Identifier ":" Value

Example:

% id: bio_q001
% points: 2

---

QuestionBlock ::=

    "\question"
    TEX_CONTENT

---

ChoicesBlock ::=

    "\begin{choices}"

        Choice+

    "\end{choices}"

Choice ::=

    "\choice" TEX_CONTENT

    |

    "\CorrectChoice" TEX_CONTENT

Constraint:

Exactly one CorrectChoice required.

---

SolutionBlock ::=

    "\begin{solution}"

        TEX_CONTENT

    "\end{solution}"

---

## Group Question

GroupFile ::=

    GroupMetadata
    PassageBlock
    SubQuestion+

PassageBlock ::=

    "\begin{passage}"

        TEX_CONTENT

    "\end{passage}"

SubQuestion ::=

    "\begin{subquestion}"

        QuestionFile

    "\end{subquestion}"

---

# 5. AST Layer

Parser output:

class QuestionAST:

    metadata
    stem
    choices
    solution

Purpose:

Parser ≠ Data Model

Allows future reuse:

- Markdown
- OCR
- HTML
- External imports

---

# 6. Validator Rules

Fatal Errors:

P001 MultipleCorrectChoice

P002 MissingMetadata

P003 MissingQuestion

P004 InvalidPoints

P005 UnclosedEnvironment

P006 InvalidGroupStructure

P007 SubQuestionCountMismatch

---

Warnings:

W001 MissingSolution

W002 UnusedMetadata

W003 LongStemText

---

# 7. Diagnostic System

All errors must produce a Diagnostic object.

class Diagnostic:

    severity:str

    code:str

    file:str

    line:int

    column:int

    message:str

    source_snippet:str

    suggestion:str

    related_info:list[str]

---

Diagnostic severity:

ERROR

WARNING

INFO

---

# 8. Diagnostic Requirements

Every Fatal Error must include:

1. Error location

2. Error cause

3. Source snippet

4. Suggested fix

---

Example:

ERROR [P001]

File:

bio_q001/question.tex

Line:

23

Column:

1

Message:

Expected exactly one CorrectChoice.

Found:

2 CorrectChoice commands.

Source:

22 | \choice A

23 | \CorrectChoice B

24 | \CorrectChoice C

Suggestion:

Change one CorrectChoice to choice.

---

# 9. GUI Integration

GUI should:

- Jump directly to source location
- Highlight problematic region
- Show suggestions
- Filter ERROR/WARNING/INFO

---

# 10. Parser Red Line

Forbidden:

- Automatically insert CorrectChoice
- Generate missing solutions
- Guess metadata
- Modify source files

Required:

System must prioritize actionable repair information over generic error messages.
