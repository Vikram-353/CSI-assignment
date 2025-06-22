# 📊 AI Job Market & Salary Trends — Data Visualization Project

This project explores and visualizes the **2025 Global AI Job Market and Salary Trends** dataset. Using powerful tools like **Plotly**, **Seaborn**, and **Matplotlib**, it reveals insights into AI-related roles, compensation, skills, and global job distributions.

---

## 📁 Dataset Overview

- **Rows:** 15,000
- **Columns:** 19
- **Source:** Kaggle (AI Job Dataset)  \
- **Theme:** Global AI jobs, salaries, skills, and employment trends

### 📌 Key Columns:

| Column Name            | Description                                        |
|------------------------|----------------------------------------------------|
| `job_title`            | Role or position name (e.g., AI Scientist, NLP Eng.) |
| `salary_usd`           | Standardized salary in USD                        |
| `salary_currency`      | Original currency of the salary                   |
| `experience_level`     | Entry/Mid/Senior/Executive                        |
| `employment_type`      | FT, PT, Contract, Freelancer                      |
| `company_location`     | Country of the company                            |
| `employee_residence`   | Country of employee                               |
| `remote_ratio`         | 0 (on-site), 50 (hybrid), 100 (fully remote)      |
| `required_skills`      | List of tools/technologies required               |
| `education_required`   | Minimum education (Bachelor, Master, etc.)        |
| `years_experience`     | Required or listed years of experience            |
| `benefits_score`       | Score indicating perks & benefits (0–10)          |

---

## 🎯 Objective

To visually explore:

- Salary distributions by region, experience, and job role
- Demand for technical skills across roles
- Remote work trends and employment types
- Company size and location impact on salary
- Posting and deadline frequency over time

---

## 📈 Visualizations Created

### 📌 Distributions

- Salary (Histogram + KDE + Boxplot)
- Job Description Length & Benefits Score
- Experience Level, Employment Type, Company Size
- Required Skills Frequency

### 🗺️ Categorical Frequency Charts

- Job Title
- Company Location vs Employee Residence
- Salary Currency
- Education Level

### 🔗 Relationship Analysis

- Salary vs Experience Level
- Salary vs Years of Experience
- Company Location ↔ Employee Residence
- Salary Currency ↔ Residence or Company
- Heatmaps & Violinplots for deeper analysis

### 📅 Temporal Trends

- Job Posting Dates by Month
- Application Deadlines over Time

---

## 🛠️ Technologies Used

- 🐼 **Pandas** for data manipulation
- 📊 **Matplotlib & Seaborn** for static plots
- 🧹 **NumPy** for numerical operations

---

## 🧠 Insights Highlight

- High-paying roles include **Head of AI** and **Machine Learning Researchers**
- Most in-demand skills: `Python`
- The **US, India, and Germany** dominate AI job postings
- Majority of jobs are **fully remote (100%)** or **hybrid (50%)**
- Companies prefer candidates with **Master’s or PhD degrees**

---

