import subprocess
import random
from datetime import datetime

# Generate a random word or phrase
def get_quote():
    # Option 1: Random Word
    words = ["Motivation", "Creativity", "Resilience", "Courage", "Inspiration"]
    # Option 2: Random Sentence
    subjects = ["Success", "Happiness", "Creativity", "Motivation", "Courage"]
    verbs = ["comes", "thrives", "depends", "is achieved", "is discovered"]
    objects = [
        "when you believe in yourself",
        "through hard work",
        "by sharing with others",
        "by overcoming challenges",
        "with persistence",
    ]
    # Randomly choose between word or sentence generation
    if random.choice([True, False]):
        return f"Today's focus is on: {random.choice(words)}."
    else:
        return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."

        
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
