import csv
import random

# Define lists for categorical data
genders = ["Male", "Female"]
marital_status = ["Married", "Single", "Widowed", "Divorced"]
living_situations = ["Living Alone", "Living with Family", "Care Facility"]
diagnoses = ["Dementia", "Alzheimer's Disease", "Stroke", "Heart Disease", "Diabetes"]
continence = ["Continent", "Incontinent of Urine", "Incontinent of Bowel"]
dnr_order = ["Yes", "No"]
advance_directive = ["Yes", "No"]
high_risk_meds = ["Antipsychotic", "Sedatives", "Opioids", None]  # Include 'None' for some residents

def generate_date_of_birth():
  """Generates a random date of birth between 65 and 90 years old"""
  year = random.randint(1934, 1959)
  month = random.randint(1, 12)
  day = random.randint(1, 31)
  return f"{year}-{month:02d}-{day:02d}"

def generate_record():
  """Generates a single dictionary representing a nursing home patient record"""
  return {
      "Resident ID": f"RN{random.randint(1000, 9999)}",
      "Date of Birth": generate_date_of_birth(),
      "Gender": random.choice(genders),
      "Marital Status": random.choice(marital_status),
      "Prior Living Situation": random.choice(living_situations),
      "Length of Stay (days)": random.randint(1, 365),
      "Diagnosis": random.choice(diagnoses),
      "MMSE Score": random.randint(0, 30),
      "Katz ADL Index": random.randint(0, 6),
      "Continence": random.choice(continence),
      "Number of Medications": random.randint(1, 10),
      "High Risk Medications": random.choice(high_risk_meds),
      "DNR Order": random.choice(dnr_order),
      "Advance Directive": random.choice(advance_directive),
  }

# Generate 10,000 records
records = [generate_record() for _ in range(10000)]

# Write data to CSV file
with open("nursing_home_patients.csv", "w", newline="") as csvfile:
  fieldnames = records[0].keys()
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
  writer.writeheader()
  writer.writerows(records)

print("10,000 nursing home patient records created and saved to 'nursing_home_patients.csv'")