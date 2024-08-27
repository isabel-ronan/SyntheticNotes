import random
from datetime import date, timedelta
import csv

# Define resident data (increased to 100)
residents = [("Resident " + str(i), random.randint(65, 95)) for i in range(100)]

# Define mobility options
mobility_options = ["Independent", "Assisted", "Dependent"]

# Define pain level range
pain_level_range = range(0, 11)

# Define mood options
mood_options = ["Excellent", "Good", "Fair", "Poor"]

# Nurse note options (more specific to medical care)
nurse_note_options = [
    "Vitals stable. No immediate concerns.",
    "Monitored blood pressure due to dizziness. Medication adjusted.",
    "Encouraged participation in physical therapy. Slight improvement in gait.",
    "Administered pain medication for discomfort. Scheduled follow-up with doctor.",
    "Patient reported feeling well-rested. Encouraged social interaction with other residents.",
    "Dressing change performed. Wound healing as expected.",
    "Assisted with medication administration. Patient expressed understanding of medication schedule.",
    "Monitored for signs of infection. No concerns noted.",
    "Dietary assessment conducted. Recommended adjustments to meet nutritional needs.",
    "Discussed upcoming family visit. Patient in good spirits."
]

# Carer note options (more focused on daily living and well-being)
carer_note_options = [
    "Enjoyed a chat about the weather during breakfast.",
    "Assisted with morning dressing. Patient in positive mood.",
    "Participated in reminiscing activity. Resident shared stories from their youth.",
    "Offered assistance with reading materials. Patient preferred listening to music.",
    "Encouraged participation in bingo game. Resident had a good laugh with other residents.",
    "Assisted with walking exercise in the garden. Resident enjoyed the fresh air.",
    "Offered help with writing a letter to family. Patient expressed gratitude for support.",
    "Played a game of cards with resident. Enjoyed a pleasant conversation.",
    "Reminded resident about medication schedule. Assisted with taking medications.",
    "Helped resident prepare for bed. Patient expressed feeling comfortable for the night."
]


def generate_daily_data(resident_name, age):
    mobility = random.choice(mobility_options)
    pain_level = random.choice(pain_level_range)
    mood = random.choice(mood_options)
    meals_consumed = random.randint(1, 4)
    medications = random.choice(["Yes", "No"])
    nurse_note = random.choice(nurse_note_options)
    carer_note = random.choice(carer_note_options)
    return {
        "Resident Name": resident_name,
        "Age": age,
        "Mobility (Independent/Assisted/Dependent)": mobility,
        "Pain Level (0-10)": pain_level,
        "Mood (Excellent/Good/Fair/Poor)": mood,
        "Meals Consumed (Number)": meals_consumed,
        "Medications Administered (Yes/No)": medications,
        "Nurse Notes": nurse_note,
        "Carer Notes": carer_note,
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
    print("Sample data for a week with nurse and carer notes generated and saved to nursing_home_data.csv")
