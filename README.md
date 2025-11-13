# 📊 Exploratory Data Analysis on Student Performance Dataset

![Image](https://i.ytimg.com/vi/UM5bxbosgD8/maxresdefault.jpg)

## 🧩 Overview
This project performs an **Exploratory Data Analysis (EDA)** on the **Student Performance Dataset** that tabulates the scores of 1000 high school students from the United States.


The main goal of this analysis is to understand how various factors — such as gender, parental education level, lunch type (as an indicator of the economic status), and test preparation — influence students’ performance in math, reading, and writing exams.  
Through descriptive analysis and visualizations, this project aims to diagnose underlying patterns and extract meaningful insights from the data.

---

## 📂 Dataset Information

**Source:** [Kaggle - Students Performance Dataset](https://www.kaggle.com/code/abdallahwagih/students-performance)

**Description:**  
The dataset contains students’ scores in math, reading, and writing, along with demographic and contextual factors that may influence academic achievement.

| Feature | Description |
|----------|-------------|
| `gender` | Student’s gender |
| `race/ethnicity` | Student’s racial/ethnic group |
| `parental level of education` | Highest education level attained by parent(s) |
| `lunch` | Type of lunch (standard or free/reduced) |
| `test preparation course` | Completion status of test prep course |
| `math score` | Student’s math test score |
| `reading score` | Student’s reading test score |
| `writing score` | Student’s writing test score |

---
**Student’s racial/ethnic group:**

| Group Letter | Meaning (common EEOC use)                                                                     |
| ------------ | --------------------------------------------------------------------------------------------- |
| Group A      | White (Not Hispanic)                                                                          |
| Group B      | Black or African American                                                                     |
| Group C      | Hispanic / Latino                                                                             |
| Group D      | Asian                                                                                         |
| Group E      | Native Hawaiian / Other Pacific Islander / American Indian / Alaskan Native                   |

---

**Highest education level attained by parent(s) (in a descending order)**
1. Master's degree
2. Bachelor's degree
3. Associate's degree
4. Some college
5. High school
6. Some high school

---
## 🧭 Hypotheses

1. Female students get better scores compared to their male classmates.
2. Students' ethnicity does not correlate with their scores.
3. Students whose parent hold higher degrees obtain better scores.
4. students eating standard lunch scored better than those eating a free/reduced price one.
5. Students who took Test preparation course got higher scores.
 
---

## 🧠 Objectives
- Explore the dataset and add an additional column in which every sttudent's total scores is found  
- Identify relationships between demographic variables (gender and race/ethnicity and academic performance.
- Identify relationships between parents'education level and academic performance.
- Identify relationships between taking the test preparation course and academic performance.    
- Analyze correlations among math, reading, and writing scores.  
- Visualize findings using graphs and plots.  
- Extract meaningful insights from the data.

---


## 🏗️ Project Structure

student-performance-eda/
├── README.md
├── data/
│ └── StudentsPerformance.csv
├── notebooks/
│ └── Student.ipynb


---

## 🧰 Tools & Libraries used

- **Python 3.12.10**
- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **jupyter notebook**

---

## 📈 Key Findings

- Female students scored higher in **reading** and **writing**, while males slightly outperformed in **math**.  
- Students who **completed test preparation courses** showed improved performance across all subjects.  
- **Parental education level** correlates positively with students’ scores.  
- **Lunch type** may reflect socioeconomic status, influencing test results.  
- Strong correlations exist among the three subject scores, especially between **reading** and **writing**.

---

## 🧠 Conclusion
This exploratory analysis highlights key demographic and socioeconomic factors influencing students’ academic performance.
The findings could help educators and policymakers design targeted interventions (i.e., test preparation course) to support students’ learning outcomes.

