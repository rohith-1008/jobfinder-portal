from flask import Flask, render_template, request, redirect
import snowflake.connector
import requests
import pandas as pd
import os

from config import SNOWFLAKE_CONFIG

app = Flask(__name__)

# ==========================================
# Snowflake Connection
# ==========================================

def get_connection():

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG["user"],
        password=SNOWFLAKE_CONFIG["password"],
        account=SNOWFLAKE_CONFIG["account"],
        warehouse=SNOWFLAKE_CONFIG["warehouse"],
        database=SNOWFLAKE_CONFIG["database"],
        schema=SNOWFLAKE_CONFIG["schema"]
    )

    return conn


# ==========================================
# Fetch Jobs from API
# ==========================================

def fetch_jobs(skill):

    try:

        url = f"https://remotive.com/api/remote-jobs?search={skill}"

        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        return data.get("jobs", [])

    except requests.exceptions.RequestException:

        return []

    except Exception:

        return []


# ==========================================
# Save Search History
# Duplicate Prevention
# ==========================================

def save_job_history(job, skill):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM JOB_HISTORY
    WHERE JOB_TITLE=%s
    AND COMPANY=%s
    """,
    (
        job["title"],
        job["company_name"]
    ))

    exists = cur.fetchone()[0]

    if exists == 0:

        cur.execute("""
        INSERT INTO JOB_HISTORY
        (
            JOB_TITLE,
            COMPANY,
            LOCATION,
            SKILL_SEARCHED
        )
        VALUES
        (%s,%s,%s,%s)
        """,
        (
            job["title"],
            job["company_name"],
            job["candidate_required_location"],
            skill
        ))

        conn.commit()

    cur.close()
    conn.close()


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Search Jobs
# ==========================================

@app.route("/search", methods=["POST"])
def search():

    skill = request.form["skill"]
    location = request.form["location"]

    jobs = fetch_jobs(skill)

    filtered_jobs = []

    for job in jobs:

        if location == "":

            filtered_jobs.append(job)

        elif location.lower() in \
        job["candidate_required_location"].lower():

            filtered_jobs.append(job)

    for job in filtered_jobs[:10]:

        save_job_history(job, skill)

    return render_template(
        "results.html",
        jobs=filtered_jobs[:10]
    )


# ==========================================
# Search History
# ==========================================

@app.route("/history")
def history():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM JOB_HISTORY
    ORDER BY SEARCH_DATE DESC
    """)

    records = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "history.html",
        records=records
    )


# ==========================================
# Save Job
# ==========================================

@app.route("/save-job", methods=["POST"])
def save_job_route():

    title = request.form["title"]
    company = request.form["company"]
    location = request.form["location"]
    url = request.form["url"]

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT COUNT(*)
    FROM SAVED_JOBS
    WHERE JOB_TITLE=%s
    AND COMPANY=%s
    """,
    (
        title,
        company
    ))

    exists = cur.fetchone()[0]

    if exists == 0:

        cur.execute("""
        INSERT INTO SAVED_JOBS
        (
            JOB_TITLE,
            COMPANY,
            LOCATION,
            JOB_URL
        )
        VALUES
        (%s,%s,%s,%s)
        """,
        (
            title,
            company,
            location,
            url
        ))

        conn.commit()

    cur.close()
    conn.close()

    return redirect("/saved-jobs")


# ==========================================
# Saved Jobs
# ==========================================

@app.route("/saved-jobs")
def saved_jobs():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM SAVED_JOBS
    ORDER BY SAVED_AT DESC
    """)

    jobs = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "saved_jobs.html",
        jobs=jobs
    )


# ==========================================
# Dashboard
# ==========================================

@app.route("/dashboard")
def dashboard():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM JOB_HISTORY"
    )

    total_jobs = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM SAVED_JOBS"
    )

    total_saved_jobs = cur.fetchone()[0]

    cur.execute("""
    SELECT
        SKILL_SEARCHED,
        COUNT(*)
    FROM JOB_HISTORY
    GROUP BY SKILL_SEARCHED
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """)

    top_skill = cur.fetchone()

    cur.execute("""
    SELECT COUNT(
        DISTINCT SKILL_SEARCHED
    )
    FROM JOB_HISTORY
    """)

    total_skills = cur.fetchone()[0]

    cur.execute("""
    SELECT MAX(SEARCH_DATE)
    FROM JOB_HISTORY
    """)

    latest_search = cur.fetchone()[0]

    cur.close()
    conn.close()

    return render_template(
        "dashboard.html",
        total_jobs=total_jobs,
        total_saved_jobs=total_saved_jobs,
        top_skill=top_skill,
        total_skills=total_skills,
        latest_search=latest_search
    )


# ==========================================
# Analytics
# ==========================================

@app.route("/analytics")
def analytics():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT
        SKILL_SEARCHED,
        COUNT(*)
    FROM JOB_HISTORY
    GROUP BY SKILL_SEARCHED
    ORDER BY COUNT(*) DESC
    """)

    analytics_data = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "analytics.html",
        analytics=analytics_data
    )


# ==========================================
# Export CSV
# ==========================================

@app.route("/export")
def export():

    conn = get_connection()

    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM JOB_HISTORY
    """)

    rows = cur.fetchall()

    columns = [col[0] for col in cur.description]

    df = pd.DataFrame(
        rows,
        columns=columns
    )

    csv_path = os.path.join(
        os.getcwd(),
        "job_history.csv"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    cur.close()
    conn.close()

    return f"""
    CSV Exported Successfully ✅

    <br><br>

    File Location:

    <br>

    {csv_path}
    """


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)