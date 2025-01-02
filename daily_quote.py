import subprocess
import requests
from datetime import datetime

# Fetch a random quote
def get_quote():
    try:
        response = requests.get("http://numbersapi.com/random/trivia")
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}" - {data["author"]}'
    except Exception as e:
        print(f"Error fetching quote: {e}")
    return "Stay motivated!"

# Append the quote to the log file
def append_quote_to_log(quote):
    date = datetime.now().strftime("%Y-%m-%d")
    with open("quotes_log.md", "a") as file:
        file.write(f"{date}: {quote}\n")

# Commit the changes
def git_commit():
    subprocess.run(["git", "add", "quotes_log.md"])
    subprocess.run(["git", "commit", "-m", f"Added quote for {datetime.now().strftime('%Y-%m-%d')}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    quote = get_quote()
    append_quote_to_log(quote)
    git_commit()
