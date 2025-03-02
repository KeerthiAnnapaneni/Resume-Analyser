
# 📝 Resume Analyzer — Your Ultimate Hiring Assistant


## 📖 Introduction

Resume Analyzer is a powerful and efficient Python-based tool designed to simplify and optimize the resume screening process. By parsing resumes and matching candidate skills against job descriptions, this tool helps identify the best-fit candidates in seconds — saving time and enhancing recruitment decisions.



## ✨ Key Features


**✅ Smart Resume Parsing:** ```Extracts name, email, phone number, and technical skills from the resume.```

**✅ Intelligent Skill Matching:** ```Compares candidate skills with job requirements and calculates a matching score.```

** ✅ Comprehensive Analysis Report:** ``` Provides detailed insights into matched and missing skills.```

**✅ Automated Report Generation:** ```Saves results in a well-structured text report for easy review.```



## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Libraries:** re (Regular Expressions)


## 🗂️ Project Structure


```
Resume_Analyzer/
│── resume_analyzer.py
│── resumes/
│   ├── candidate_resume.txt
│── job_descriptions/
│   ├── job_description.txt
│── resume_analysis_report.txt
```

## 🚀 How to Use


**1️⃣ Prepare Files:** Place resume files in the ```resumes/``` folder and job descriptions in the ```job_descriptions/``` folder.

**2️⃣ Run the Script:** Open terminal and execute:

```
python resume_analyzer.py
```

**3️⃣ Provide Inputs:** Enter file names when prompted.

**4️⃣ View Results:** Check the console for analysis and the resume_analysis_report.txt for a detailed report.


## 📝 Sample Output

```
WELCOME TO THE RESUME ANALYZER!!!
Enter the resume file name: candidate1.txt
Enter the job description file: job_description_file.txt

RESUME DETAILS
keerthi annapaneni
phone: 8309424101
email: keerthi@email.com
skills:python,sql,machine learning
experience: 2 years
education: computers degree in btech

Resume Analysis Report
Score: 33.33%
Matched Skills: python, sql
Missing Skills: html, java, javascript, react


THE REPORT IS SAVED
```

## ⚠️ Error Handling

```
❌ File not found? Displays a clear and professional error message.
❌ Empty or incorrect file format? Ensures graceful failure and informative feedback.
```


## 📄 Report Example

```
Resume Analysis Report
Score: 33.33%
Matched Skills: python, sql
Missing Skills: html, java, javascript, react

```
