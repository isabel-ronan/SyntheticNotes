import random

# Sample data with limited details to protect privacy
resident_data = [
    {"Resident ID": "RES" + str(1000 + i),
     "Date of Assessment": "2024-03-08",
     "Age": random.randint(65, 90),
     "Gender": random.choice(["Male", "Female"]),
     "Marital Status": random.choice(["Married", "Widowed", "Single", "Divorced"]),
     "Length of Stay (days)": random.randint(30, 270),
     "Primary Diagnosis": random.choice(["Heart Failure", "Osteoporosis", "Alzheimer's Disease",
                                         "Hip Fracture", "Diabetes Mellitus", "COPD", "Parkinson's Disease",
                                         "Stroke", "Arthritis", "Depression"]),
     "Cognitive Function Score": random.randint(2, 12),  # Limited score range
     "ADL Score": random.randint(1, 8),  # Limited score range
     "Continence (Bowel)": random.choice(["Continent", "Incontinent"]),
     "Number of Medications": random.randint(1, 8),
     "High Risk Medications (Category)": random.choice(["None", "Blood Thinners", "Opioids", "Antidepressants"]),
     "Pressure Sores": random.choice(["Yes", "No"])}
    for i in range(10)  # Generate 10 residents
]

# Export data to CSV file
import csv

with open("nursing_home_sample.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=resident_data[0].keys())
    writer.writeheader()
    writer.writerows(resident_data)

print("Sample dataset with limited MDS 3.0 elements created in nursing_home_sample.csv")
