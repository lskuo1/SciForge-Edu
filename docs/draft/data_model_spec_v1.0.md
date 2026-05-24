
# SciForge-Edu Internal Data Model Specification
Version: v1.0
Status: Draft (Architecture Locked)

## 1. Core Philosophy

### Source of Truth
- Question Object = 唯一真理來源
- LaTeX = Import / Export Format

Flow:

question.tex
→ Parser
→ Question Object
→ GUI
→ Assembler
→ student.tex / teacher.tex
→ PDF

Rules:
- GUI 不直接修改 tex
- Parser 不做 rendering
- Assembler 不做 parsing
- Shuffle 不修改 Question Object

---

## 2. Question 與 Exam 分離

Question = 可重複使用之資產

Exam = 題目的排列組合

Question ≠ Exam

---

## 3. Supported Question Types

- single_choice
- group

---

## 4. Choice Object

```python
class Choice:
    text_tex:str
    is_correct:bool
```

---

## 5. QuestionAnalysis

```python
class QuestionAnalysis:
    difficulty:Optional[float]
    chapter:Optional[str]
    tags:list[str]
    competency:list[str]
    misconceptions:list[str]
    extra:dict
```

---

## 6. QuestionVersion

```python
class QuestionVersion:
    version:int
    timestamp:datetime
    author:str
    change_note:str
```

---

## 7. SourceInfo

```python
class SourceInfo:
    file_path:str
    raw_tex:str
```

---

## 8. Question Object

```python
class Question:
    uuid:str
    label:str
    type:QuestionType
    points:int
    stem_tex:str
    choices:list[Choice]
    solution_tex:Optional[str]
    analysis:Optional[QuestionAnalysis]
    source:Optional[SourceInfo]
    current_version:int
    history:list[QuestionVersion]
    extra:dict
```

---

## 9. GroupQuestion

```python
class GroupQuestion:
    uuid:str
    label:str
    passage_tex:str
    subquestions:list[Question]
    total_points:int
```

Capabilities:

- passage 可放圖片
- 子題可 shuffle
- 子題共用圖片
- 題組有總配分

Restrictions:

- 不支援巢狀題組
- passage 不跨頁

---

## 10. Exam Object

```python
class ExamMetadata:
    exam_id:str
    title:str
    semester:str
    school_name:str
    grade:str
    course:str
    test_range:str

class ExamSettings:
    shuffle_questions:bool
    balance_answers:bool
    total_score:int

class ExamQuestionReference:
    uuid:str
    version:int

class Exam:
    metadata:ExamMetadata
    settings:ExamSettings
    questions:list[ExamQuestionReference]
```

---

## 11. Resource Management

Each question is atomic:

bio_q001/
- question.tex
- fig1.png
- fig2.svg

Output:

student.tex
teacher.tex

Images are renamed automatically to avoid conflicts.

---

## 12. Architecture Red Line

Forbidden:

- GUI 直接修改 tex
- Parser 進行 render
- Assembler 進行 parse
- Shuffle 修改 Question Object
- AI 修改 UUID
- AI 修改歷史版本

Allowed:

- AI 新增分析資訊
- AI 新增 metadata
- AI 新增 extra 欄位
