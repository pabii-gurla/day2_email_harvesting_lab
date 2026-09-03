import re
from pathlib import Path

def harvest_emails(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html = file.read()

    pattern = r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}'
    emails = set(re.findall(pattern, html))

    return emails

file_path = Path(__file__).parent / "test_page.html"
found_emails = harvest_emails(file_path)

print("Emails found:")

for email in found_emails:
    print(email) 