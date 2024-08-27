import random
import csv

# Define resident information (adjust as needed)
residents = [
    {"name": "Sarah Murphy", "age": 85, "diagnosis": "Arthritis"},
    {"name": "David Walsh", "age": 72, "diagnosis": "Heart Disease"},
    {"name": "Caoimhe O'Connor", "age": 60, "diagnosis": "Depression"},
    {"name": "Eamon O'Sullivan", "age": 90, "diagnosis": "Dementia"},
    {"name": "Aisha Hassan", "age": 65, "diagnosis": "Diabetes"}
]

# Define data ranges and options
medication_adherence = ["Full", "Partial", "Missed"]
pain_level_range = (0, 10)
mood_options = ["Positive", "Neutral", "Negative"]
activity_levels = ["Independent", "Assisted", "Dependent"]
nurse_note_templates = [
    "Assisted {resident} with {activity}. {comment}",
    "{resident} participated in {activity} session. {comment}",
]
carer_note_templates = [
    "Spent time talking with {resident} about {topic}.",
    "Helped {resident} with {activity}.",
]

# Function to generate random data for a resident
def generate_resident_data(resident):
  medication = random.choice(medication_adherence)
  pain_level = random.randint(*pain_level_range)
  mood = random.choice(mood_options)
  activity_level = random.choice(activity_levels)
  
  # Randomly choose and customize nurse & carer notes
  nurse_note_template = random.choice(nurse_note_templates)
  carer_note_template = random.choice(carer_note_templates)
  activity = random.choice(["exercises", "breakfast", "therapy", "music therapy"])
  topic = "upcoming surgery" if resident["diagnosis"] == "Heart Disease" else "family visit"
  comment = f"They seemed {mood.lower()}."
  nurse_note = nurse_note_template.format(resident=resident["name"], activity=activity, comment=comment)
  carer_note = carer_note_template.format(resident=resident["name"], activity=activity, topic=topic)
  
  return [medication, pain_level, mood, activity_level, nurse_note, carer_note]

# Generate data for a week
data = []
for day in range(17, 21):  # March 17th to 20th
  date = f"2024-03-{day:02d}"
  for resident in residents:
    resident_data = [date, resident["name"], resident["age"], resident["diagnosis"]] + generate_resident_data(resident)
    data.append(resident_data)

# Save data to CSV file
with open("nursing_home_data.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow([
      "Date",
      "Resident Name",
      "Age",
      "Diagnosis",
      "Medication Adherence",
      "Pain Level (0-10)",
      "Mood",
      "Activity Level (Independent/Assisted/Dependent)",
      "Nurse Notes",
      "Carer Notes"
  ])
  writer.writerows(data)

print("Data generated and saved to nursing_home_data.csv")
