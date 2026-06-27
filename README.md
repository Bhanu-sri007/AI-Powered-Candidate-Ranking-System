# AI-Powered Candidate Ranking System

## Overview

The AI-Powered Candidate Ranking System is an intelligent recruitment assistant designed to help recruiters identify the most suitable candidates from large candidate datasets.

Traditional recruitment processes rely heavily on manual resume screening and keyword-based filtering, which are time-consuming and often fail to identify the best candidates. This project uses multiple evaluation factors such as skills, experience, career history, recruiter engagement signals, and recruitability metrics to generate a reliable candidate ranking.

The system processes candidate profiles, calculates suitability scores, classifies candidates, and generates a ranked shortlist that recruiters can trust.


# Problem Statement

Recruiters often need to evaluate thousands of candidate profiles for a single role. Manual screening is slow, inconsistent, and prone to bias.

Challenges include:

* Large volume of candidate profiles
* Difficulty identifying relevant experience
* Lack of insight into candidate engagement
* Time-consuming shortlisting process
* Inconsistent hiring decisions

This project aims to automate and improve the candidate selection process using AI-driven ranking techniques.


# Solution

The system analyzes candidate data and evaluates:

* Current Job Title
* Years of Experience
* Technical Skills
* Career History
* Behavioral Signals
* Recruitability Metrics

Based on these factors, candidates are scored, ranked, categorized, and shortlisted for recruiters.


# Key Features

## Candidate Ranking

Ranks candidates according to overall suitability for the target role.

## Skill Matching

Identifies candidates with relevant AI, Machine Learning, Retrieval, Ranking, and Search-related skills.

## Experience Analysis

Evaluates professional experience and assigns scores based on role requirements.

## Career History Analysis

Analyzes project descriptions and previous work experience to identify production-level expertise.

## Behavioral Signal Analysis

Uses recruiter engagement indicators such as:

* Recruiter Response Rate
* Interview Completion Rate
* Open-to-Work Status
* GitHub Activity

## Recruitability Score

Measures the likelihood of successful recruiter engagement.

## Confidence Score

Provides confidence levels for AI recommendations.

## Match Classification

Candidates are categorized as:

* Strong Match
* Potential Match
* Weak Match
* Not Recommended

## Candidate Comparison

Compares top candidates using detailed score breakdowns.

## Missing Skills Analysis

Highlights important skills missing from candidate profiles.

## Backup Candidate Pool

Provides additional qualified candidates as fallback options.

## AI Recruiter Recommendation

Generates final hiring recommendations based on candidate performance.

## CSV Submission Generator

Exports ranked candidates into a submission-ready CSV file.


# System Architecture

Recruiter Requirement

↓

Candidate Dataset (100,000 Profiles)

↓

Feature Extraction Layer

* Skills
* Experience
* Career History
* Behavioral Signals

↓

Scoring Engine

* Title Score
* Experience Score
* Skill Score
* Career Score
* Behavioral Score
* Recruitability Score
* Penalty Score

↓

Ranking Engine

↓

Candidate Classification

↓

Top Candidate Selection

↓

Candidate Comparison

↓

Missing Skills Analysis

↓

AI Recruiter Recommendation

↓

submission.csv


# Technologies Used

* Python
* JSON
* CSV
* Data Processing
* Information Retrieval Concepts
* Machine Learning Concepts



# Sample Output

## Recruiter Dashboard

```text
Total Candidates: 100000
Strong Matches: 27
Potential Matches: 140
Weak Matches: 257
Not Recommended: 99576
```

## Best Candidate

```text
Candidate ID: CAND_0088025
Final Score: 119
Status: Strong Match
Confidence: 100%
```

## Score Breakdown

```text
Title Score: 24
Experience Score: 12
Skill Score: 18
Career Score: 25
Behavior Score: 25
Recruitability Score: 15
Penalty Score: 0
```

---

# Project Workflow

1. Load candidate dataset
2. Extract profile information
3. Analyze skills and experience
4. Evaluate career history
5. Calculate behavioral signals
6. Compute recruitability score
7. Generate final score
8. Classify candidates
9. Rank candidates
10. Generate recruiter insights
11. Export ranked shortlist

---

# How to Run

### Step 1: Clone or Download the Project

Download the project files or clone the repository.

### Step 2: Open the Project Folder

```bash
cd redrob-hackathon
```

### Step 3: Run the Ranking Engine

```bash
python src/ranker.py
```

### Step 4: View Output

Generated output file:

```text
output/submission.csv
```



# Future Enhancements

* Resume Parsing
* NLP-Based Job Description Understanding
* LLM-Based Candidate Evaluation
* Skill Gap Recommendations
* Candidate Improvement Roadmaps
* Interview Readiness Prediction
* Real-Time Recruiter Dashboard
* Web Application Deployment


# Business Impact

* Reduces recruiter screening effort
* Improves hiring efficiency
* Enhances candidate quality
* Provides explainable AI recommendations
* Supports large-scale recruitment processes

---

# Author

**Bhanusri Dunaboina**

Final Year B.Tech Computer Science and Engineering Student

Java Full Stack Developer | AI & Machine Learning Enthusiast
