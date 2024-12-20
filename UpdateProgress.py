import re
import requests
from datetime import datetime, timedelta
import pytz  # タイムゾーンライブラリ

API_URL = "https://leetcode-api-faisalshohag.vercel.app/Gxv68WV2yV"
README_FILE = "README.md"
SGT = pytz.timezone("Asia/Singapore")  # シンガポール時間

def fetch_api_data(api_url):
    """Fetch data from the API."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from API. Status code: {response.status_code}")

def get_weekly_counts(submission_calendar):
    """Calculate submissions for each day of the past week."""
    today = datetime.now(SGT)
    week_dates = [(today - timedelta(days=i)).date() for i in range(6, -1, -1)]
    weekly_counts = {date: 0 for date in week_dates}

    # Count submissions from the submission calendar
    for timestamp, count in submission_calendar.items():
        submission_date = datetime.fromtimestamp(int(timestamp), SGT).date()
        if submission_date in weekly_counts:
            weekly_counts[submission_date] += count

    return weekly_counts

def format_weekly_submissions_horizontal(weekly_counts):
    """Format weekly submissions as a horizontal Markdown table."""
    week_dates = list(weekly_counts.keys())
    weekdays = [date.strftime("%A") for date in week_dates]  # Dynamic weekdays
    dates = [date.strftime("%m/%d") for date in week_dates]  # Format as MM/DD
    submissions = [weekly_counts[date] for date in week_dates]

    table = "| Day         | " + " | ".join(weekdays) + " |\n"
    table += "|-------------| " + " | ".join(["-" * len(day) for day in weekdays]) + " |\n"
    table += "| Date        | " + " | ".join(dates) + " |\n"
    table += "| Submissions | " + " | ".join(map(str, submissions)) + " |"

    return table

def generate_progress_section(api_data):
    """Generate the progress section as a Markdown string."""
    easy_solved = api_data["easySolved"]
    medium_solved = api_data["mediumSolved"]
    hard_solved = api_data["hardSolved"]
    total_solved = api_data["totalSolved"]
    total_questions = api_data["totalQuestions"]
    ranking = api_data["ranking"]
    contribution_points = api_data["contributionPoint"]
    recent_submissions = format_recent_submissions(api_data["recentSubmissions"])
    
    # Weekly submissions
    weekly_counts = get_weekly_counts(api_data["submissionCalendar"])
    weekly_submissions = format_weekly_submissions_horizontal(weekly_counts)

    return f"""
## Problem Solving Progress 🚀

| Difficulty | Solved | Total | Completion (%) |
|------------|--------|-------|----------------|
| Easy       | {easy_solved}     | {api_data["totalEasy"]}   | {easy_solved / api_data["totalEasy"] * 100:.2f}%          |
| Medium     | {medium_solved}      | {api_data["totalMedium"]}  | {medium_solved / api_data["totalMedium"] * 100:.2f}%          |
| Hard       | {hard_solved}      | {api_data["totalHard"]}   | {hard_solved / api_data["totalHard"] * 100:.2f}%          |

**Total Solved**: {total_solved}/{total_questions} ({total_solved / total_questions * 100:.2f}%)

---

## 📘 Recent Submissions

| Problem                            | Status         | Language  | Timestamp           |
|------------------------------------|----------------|-----------|---------------------|
{recent_submissions}

---

## 📅 Submissions in the Last 7 Days

{weekly_submissions}

---

## 🌟 Rankings and Achievements

- **Global Ranking**: {ranking} 🌍
- **Contribution Points**: {contribution_points}
    """

def update_readme(new_section, readme_file):
    """Update the progress section in README."""
    with open(readme_file, "r") as file:
        content = file.read()

    # Replace the section between markers
    updated_content = re.sub(
        r"<!-- Progress Start -->.*<!-- Progress End -->",
        f"<!-- Progress Start -->{new_section}<!-- Progress End -->",
        content,
        flags=re.DOTALL
    )

    with open(readme_file, "w") as file:
        file.write(updated_content)

def format_recent_submissions(submissions):
    """Format recent submissions as a Markdown table."""
    rows = [
        f"| {sub['title']} | {sub['statusDisplay']} | {sub['lang']} | {datetime.fromtimestamp(int(sub['timestamp']), SGT).strftime('%m/%d %H:%M:%S')} |"
        for sub in submissions
    ]
    return "\n".join(rows)

def main():
    # Fetch API data
    api_data = fetch_api_data(API_URL)
    # Generate new progress section
    new_section = generate_progress_section(api_data)
    # Update README
    update_readme(new_section, README_FILE)
    print("README.md has been updated with new progress stats!")

if __name__ == "__main__":
    main()