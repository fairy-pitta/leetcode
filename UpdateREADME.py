import os
import re
from datetime import datetime

filename_pattern = re.compile(r"(\d{4})-(.+)\.py")
directory_path = "."
new_entries = []

for file in os.listdir(directory_path):
    if file.endswith('.py') and filename_pattern.match(file):
        match = filename_pattern.match(file)
        problem_no = int(match.group(1))
        problem_name = match.group(2).replace("-", " ")
        url = f"https://leetcode.com/problems/{problem_name.lower().replace(' ', '-')}/"
        hyperlink = f"[{problem_name}]({url})"
        new_entries.append((problem_no, hyperlink))

readme_path = "README.md"

with open(readme_path, 'r') as file:
    lines = file.readlines()

start_index = end_index = None
for index, line in enumerate(lines):
    if "|   Cumulative Problems |" in line:
        start_index = index + 2
    elif start_index is not None and line.strip() == "":
        end_index = index
        break

if start_index is None:
    print("README.md contents:")
    print("\n".join(lines))
    raise ValueError("Could not locate the table in README.md. Please check the table format.")

if end_index is None:
    end_index = len(lines)

table_data = []
existing_problem_nos = []

for line in lines[start_index:end_index]:
    cols = line.strip().split("|")
    if len(cols) > 1 and cols[2].strip().isdigit():
        problem_no = int(cols[2].strip())
        problem_name_link = cols[3].strip()
        date_added = cols[4].strip()
        table_data.append((problem_no, problem_name_link, date_added))
        existing_problem_nos.append(problem_no)

for problem_no, hyperlink in new_entries:
    if problem_no not in existing_problem_nos:
        date_added = datetime.now().strftime('%Y-%m-%d')
        table_data.append((problem_no, hyperlink, date_added))

table_data.sort(key=lambda x: x[0])
updated_table = [
    f"| {i+1} | {item[0]} | {item[1]} | {item[2]} |\n"
    for i, item in enumerate(table_data)
]

lines = lines[:start_index] + updated_table + lines[end_index:]

with open(readme_path, 'w') as file:
    file.writelines(lines)

print("README.md has been updated successfully.")