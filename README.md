# Task 05: Descriptive Statistics + LLM Validation (Netflix Dataset)

## 🎯 Objective
This research task evaluates whether Large Language Models (LLMs) like ChatGPT can correctly interpret and answer natural language questions based on structured data.

## 📦 Dataset
Netflix Movies & TV Shows  
- Source: [Kaggle - Netflix Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Rows: 8807 titles
- Columns: Type, Country, Date Added, Genre, Rating, etc.
- File not included in repo per project policy

## 🛠️ Methodology
1. Cleaned and analyzed the dataset using Pandas
2. Extracted descriptive statistics: top genres, top countries, year-wise growth
3. Asked natural language questions to ChatGPT
4. Validated responses using actual Python outputs

## 📂 Files Included
- `data_cleaning_netflix.py` – Python script to clean and summarize the dataset
- `prompts_and_responses.md` – LLM question logs, accuracy checks, and insights
- `content_added_per_year.png` – Bar chart showing content growth

## 💡 Key Learnings
- LLMs excel at summarizing well-structured data
- Complex judgment questions require more prompt engineering
- Hallucination can occur when fields are not present in the dataset

