import random
from datetime import date, timedelta
import csv 

# Define resident data
residents = [
    ("Sean O'Sullivan", 78),
    ("Mary Kelly", 82),
    ("Liam O'Connell", 65),
    ("Aisha Murphy", 90),
    ("Patrick Ryan", 84),
    ("Siobhan O'Reilly", 68),
    ("Brid Aherne", 89),
]

# Define mobility options
mobility_options = ["Independent", "Assisted", "Dependent"]

# Define pain level range
pain_level_range = range(0, 11)

# Define mood options
mood_options = ["Excellent", "Good", "Fair", "Poor"]

# Define notes options
notes_options = [
    "Feeling chatty today.",
    "Struggling with some back pain.",
    "Restless night, but overall positive mood.",
    "Low appetite today.",
    "Attended physical therapy session. Making good progress.",
    "Feeling energetic.",
    "Back pain improved. Enjoyed spending time in the garden.",
    "Slept well. Feeling more optimistic.",
    "Appetite slightly improved. Doctor visit scheduled for tomorrow.",
    "Feeling confident.",
    "Had a productive meeting with his financial advisor. Feeling relieved about future plans.",
    "Participated in arts and crafts activity. Reported feeling less pain.",
    "Feeling motivated. Requested assistance with planning a family visit.",
    "Appetite remained low. Doctor advised dietary changes.",
    "Feeling stronger."
]


def generate_daily_data(resident_name, age):
    mobility = random.choice(mobility_options)
    pain_level = random.choice(pain_level_range)
    mood = random.choice(mood_options)
    meals_consumed = random.randint(1, 4)
    medications = random.choice(["Yes", "No"])
    note = random.choice(notes_options)
    return {
        "Resident Name": resident_name,
        "Age": age,
        "Mobility (Independent/Assisted/Dependent)": mobility,
        "Pain Level (0-10)": pain_level,
        "Mood (Excellent/Good/Fair/Poor)": mood,
        "Meals Consumed (Number)": meals_consumed,
        "Medications Administered (Yes/No)": medications,
        "Notes": note,
    }


def generate_week_data(residents):
    data = []
    start_date = date.today() - timedelta(days=6)  # Start a week ago
    for _ in range(7):
        for resident_name, age in residents:
            daily_data = generate_daily_data(resident_name, age)
            daily_data["Date"] = start_date.strftime("%Y-%m-%d")
            data.append(daily_data)
        start_date += timedelta(days=1)  # Increment date for next day
    return data


def write_to_csv(data, filename):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = list(data[0].keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    week_data = generate_week_data(residents)
    write_to_csv(week_data, "nursing_home_data.csv")
    print("Sample data for a week generated and saved to nursing_home_data.csv")
