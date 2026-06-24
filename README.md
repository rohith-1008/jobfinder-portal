# 🚀 JobFinder Portal

<p align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=25&pause=1000&color=2563EB&center=true&vCenter=true&width=800&lines=Flask+%2B+Snowflake+Job+Search+Portal;REST+API+Integration;Real-Time+Job+Search;Analytics+Dashboard;Built+by+Venkata+Rohith+Koppolu" />

</p>

<p align="center">

![](https://komarev.com/ghpvc/?username=rohith-1008\&color=blue)

</p>

---

## 📌 Project Overview

JobFinder Portal is a full-stack web application that enables users to search for jobs in real-time using a public Jobs API, store search history in Snowflake Cloud Data Warehouse, save favorite jobs, analyze search trends, export data to CSV, and view dashboard analytics through a modern responsive interface.

This project demonstrates real-world integration of Flask, REST APIs, Snowflake Cloud Database, SQL, HTML, CSS, and JavaScript.

---


## ✨ Features

### 🔍 Job Search

* Real-Time Job Search
* Public REST API Integration
* Skill-Based Search
* Location-Based Filtering

### ☁️ Snowflake Integration

* Cloud Data Warehouse
* Search History Storage
* SQL Query Execution
* Data Analytics

### 💾 Saved Jobs

* Save Favorite Jobs
* Prevent Duplicate Saved Jobs
* Quick Access to Applications

### 📊 Dashboard

* Total Jobs Stored
* Total Saved Jobs
* Most Searched Skill
* Total Skills Covered
* Latest Search Activity

### 📈 Analytics

* Search Trend Analysis
* Skill-Wise Search Count
* SQL Aggregation Queries

### 📁 Export Functionality

* Export Search History to CSV
* Downloadable Reports

### 🎨 User Experience

* Dark Mode Support
* Responsive Design
* Modern UI
* Hover Effects
* Mobile Friendly

### 🛡️ Data Integrity

* Duplicate Prevention
* Error Handling
* Secure Configuration using Environment Variables

---

## 🛠️ Tech Stack

### Backend

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)

![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask)

### Database

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge\&logo=snowflake)

### Frontend

![HTML5](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)

![CSS3](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)

### Tools

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge\&logo=git\&logoColor=white)

![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge\&logo=github)

![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge\&logo=visual-studio-code)

---

## 🏗️ System Architecture

```text
                User
                  │
                  ▼
        Flask Web Application
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
  Remotive API        Snowflake DB
        │                   │
        ▼                   ▼
  Job Listings       Search History
                     Saved Jobs
                     Analytics
                  Dashboard Data
```

---

## 📂 Project Structure

```text
JobFinderPortal/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── results.html
│   ├── history.html
│   ├── saved_jobs.html
│   ├── dashboard.html
│   └── analytics.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .env
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/rohith-1008/jobfinder-portal.git

cd jobfinder-portal
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create:

```text
.env
```

Example:

```env
SNOWFLAKE_USER=YOUR_USER
SNOWFLAKE_PASSWORD=YOUR_PASSWORD
SNOWFLAKE_ACCOUNT=YOUR_ACCOUNT
SNOWFLAKE_WAREHOUSE=JOB_WH
SNOWFLAKE_DATABASE=JOB_DB
SNOWFLAKE_SCHEMA=JOB_SCHEMA
```

### 6️⃣ Run Application

```bash
python app.py
```

### 7️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

## 📊 SQL Features Used

* SELECT
* INSERT
* GROUP BY
* ORDER BY
* COUNT
* DISTINCT
* Aggregate Functions
* Timestamp Operations

---

## 🚀 Future Enhancements

* User Authentication
* Resume Upload Feature
* AI-Based Job Recommendations
* Email Notifications
* Application Tracking System
* Resume Parsing
* Job Matching Score
* Company Reviews
* Interview Preparation Section

---

## 🎯 Learning Outcomes

Through this project I gained hands-on experience with:

* Flask Framework
* REST API Integration
* Snowflake Cloud Data Warehouse
* SQL Querying
* Full Stack Development
* Environment Variables
* Git & GitHub
* Dashboard Development
* Data Analytics
* Responsive Web Design

---

## 👨‍💻 Author

### Venkata Rohith Koppolu

B.Tech – Artificial Intelligence & Machine Learning

### GitHub

https://github.com/rohith-1008

---


<p align="center">

⭐ Thank You For Visiting JobFinder Portal ⭐

</p>
