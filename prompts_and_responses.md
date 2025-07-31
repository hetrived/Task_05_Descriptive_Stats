# LLM Prompts & Responses – Netflix Dataset

## ✅ Prompt 1: How many total entries are there in the Netflix dataset?
**ChatGPT Answer:** There are 8807 entries.  
**Correct?** ✅ Yes  
**Validation:** Matches output of `len(df)`  
**Comment:** LLM is accurate for summary queries.

---

## ✅ Prompt 2: Which country has the most titles?
**ChatGPT Answer:** United States  
**Correct?** ✅ Yes  
**Validation:** `df['country'].value_counts().head(1)`  
**Comment:** Accurate and aligned.

---

## ✅ Prompt 3: What is the most common genre on Netflix?
**ChatGPT Answer:** Dramas, International Movies  
**Correct?** ✅ Yes  
**Validation:** `df['listed_in'].value_counts().head(1)`  
**Comment:** Correct. LLM can interpret from summary statistics.

---

## ✅ Prompt 4: How has Netflix's content grown over the years?
**ChatGPT Answer:** Netflix has seen a steady increase in the number of titles, peaking around 2019.  
**Correct?** ✅ Yes (Partial)  
**Validation:** Verified using year_added bar chart  
**Comment:** LLM was able to summarize time trends well.

---

## ❌ Prompt 5: Which genre has the best viewer rating?
**ChatGPT Answer:** Drama  
**Correct?** ❌ No  
**Validation:** The dataset does not contain viewer ratings  
**Comment:** LLM hallucinated based on genre popularity; this field doesn’t exist in the dataset.
