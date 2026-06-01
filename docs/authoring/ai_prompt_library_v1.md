# SciForge-Edu AI Prompt Library v1

Status: Draft

用途：

本文件提供可直接複製到 ChatGPT、Gemini、Claude、DeepSeek 等 AI 的 Prompt。

目標是快速產生可匯入 SciForge-Edu 的題目。

---

# Prompt 1：產生單元練習題

請產生國中自然科單選題。

主題：
【自行填寫】

例如：

* 力與運動
* 摩擦力
* 酸鹼中和
* 氧化還原
* 生殖系統
* 神經系統

題數：
【自行填寫】

難度：
【基礎／中等／進階】

輸出格式必須如下：

\question

題目內容

\begin{choices}

\choice 選項A

\CorrectChoice 正確答案

\choice 選項C

\choice 選項D

\end{choices}

\begin{solution}

詳解內容

\end{solution}

規則：

1. 每題以 \question 開始。
2. 每題必須有 choices 環境。
3. 恰好一個 \CorrectChoice。
4. 每題四個選項。
5. solution 可省略。
6. 不要輸出 \documentclass。
7. 不要輸出 \begin{document}。
8. 不要輸出任何額外說明。
9. 僅輸出題目內容。
10. 使用繁體中文。

現在開始產生題目。

---

# Prompt 2：產生段考題

請產生適合國中段考的單選題。

年級：
【自行填寫】

科目：
【理化／生物】

範圍：
【自行填寫】

題數：
【自行填寫】

輸出格式：

\question

...

\begin{choices}
...
\end{choices}

規則：

1. 題目難度須符合段考。
2. 題目分布應兼顧記憶、理解與應用。
3. 恰好一個 \CorrectChoice。
4. 不要輸出完整 LaTeX 文件。
5. 僅輸出題目內容。

---

# Prompt 3：產生題組題

請產生一組國中自然科題組題。

主題：
【自行填寫】

輸出格式：

\begin{questiongroup}

\begin{groupstem}[boxed]

題組共同資料

\end{groupstem}

\question

第一題

\begin{choices}
...
\end{choices}

\question

第二題

\begin{choices}
...
\end{choices}

\question

第三題

\begin{choices}
...
\end{choices}

\end{questiongroup}

規則：

1. 所有共同資料必須放在 groupstem。
2. 不可直接在 questiongroup 中放共同敘述。
3. 每題恰好一個 \CorrectChoice。
4. 可加入 solution。
5. 使用繁體中文。
6. 僅輸出題目內容。

---

# Prompt 4：將既有題目轉成 SciForge 格式

請將下列題目轉換成 SciForge-Edu 格式。

要求：

1. 保留所有教學內容。
2. 保留原本正確答案。
3. 不增加新知識。
4. 不修改題意。
5. 使用：

\question

\begin{choices}

\CorrectChoice

\end{choices}

格式。
6. 僅修正格式。

原始內容：

【貼上題目】

---

# Prompt 5：OCR 結果轉 SciForge 格式

以下內容來自 OCR。

請：

1. 修正 OCR 錯字。
2. 重建題目結構。
3. 找出選項。
4. 轉換成 SciForge-Edu 格式。
5. 若無法判斷正確答案，請保留：

% FIXME: correct answer unknown

輸出格式：

\question

\begin{choices}
...
\end{choices}

OCR 內容：

【貼上 OCR 結果】

---

# Prompt 6：補上詳解

請為以下題目補上詳解。

要求：

1. 保留所有題目。
2. 保留所有選項。
3. 保留所有正確答案。
4. 使用國中生能理解的語言。
5. 使用：

\begin{solution}

...

\end{solution}

題目內容：

【貼上題目】

---

# Prompt 7：檢查格式是否合法

請檢查下列內容是否符合 SciForge-Edu 格式。

檢查：

1. 是否有 \question。
2. 是否有 choices 環境。
3. 是否恰好一個 \CorrectChoice。
4. questiongroup 是否正確。
5. groupstem 是否正確。
6. 是否有 LaTeX 語法錯誤。

請輸出：

* 錯誤位置
* 錯誤原因
* 修正建議

不要直接改寫。

題目內容：

【貼上題目】

---

# Prompt 8：修復格式錯誤

請修復下列 SciForge 題目格式。

要求：

1. 保留所有內容。
2. 不改變題意。
3. 不改變正確答案。
4. 修復所有格式錯誤。
5. 輸出合法的 SciForge 題目格式。

題目內容：

【貼上題目】
