import random
from datetime import datetime

# Step 1: Determine the week and day
today = datetime.utcnow()
week_number = today.isocalendar()[1]
weekday_name = today.strftime("%A")

# Step 2: Choose random 2 or 3 commit days for this week
random.seed(week_number)  # Same days every time this week
commit_days = random.sample(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    k=random.choice([2, 3])
)

# Step 3: Exit if today is not a commit day
if weekday_name not in commit_days:
    print(f"Today ({weekday_name}) is not in this week's commit days: {commit_days}")
    exit(0)

# Step 4: Generate a creative commit message
messages = [
    "Added some magic ✨",
    "Bug? What bug? 🐞",
    "Auto update: fueled by caffeine ☕",
    "Life is too short to write bad code 🚀",
    "Bot did a thing! 🤖",
    "Daily dose of code 💉",
    "Tiny tweak, big dreams 💭"
]
commit_msg = f"{random.choice(messages)}"

# Step 5: Save commit message to be used by GitHub Action
with open(".commit-msg", "w") as f:
    f.write(commit_msg)

# Step 6: Modify a target file (create or append to it)
filename = "notes.txt"
with open(filename, "a") as f:
    f.write(f"{today.isoformat()} - {commit_msg}\n")

print(f"Committed to {filename}: {commit_msg}")
