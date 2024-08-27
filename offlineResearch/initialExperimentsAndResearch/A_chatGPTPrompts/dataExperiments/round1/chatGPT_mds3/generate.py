import csv
import random
from faker import Faker

fake = Faker()

def generate_resident_data():
    resident_id = 1
    data = []
    for _ in range(10):
        assessment_date = fake.date_between(start_date='-1y', end_date='today')
        first_name = fake.first_name()
        last_name = fake.last_name()
        dob = fake.date_of_birth(minimum_age=60, maximum_age=100)
        gender = random.choice(["Male", "Female"])
        marital_status = random.choice(["Single", "Married", "Widowed", "Divorced"])
        admission_date = fake.date_between(start_date='-5y', end_date='today')
        discharge_date = fake.date_between(start_date=admission_date, end_date='today') if random.random() < 0.3 else ""
        room_number = random.randint(100, 500)
        medical_record_number = fake.random_int(min=10000, max=99999)
        medicare_number = fake.random_int(min=1000000000, max=9999999999)
        medicaid_number = fake.random_int(min=1000000000, max=9999999999)
        
        data.append([
            resident_id, assessment_date, first_name, last_name, dob, gender, marital_status, admission_date,
            discharge_date, room_number, medical_record_number, medicare_number, medicaid_number
        ])
        resident_id += 1
    return data

def save_to_csv(data):
    with open('nursing_home_residents_mds3.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "ResidentID", "AssessmentReferenceDate", "FirstName", "LastName", "DOB", "Gender", "MaritalStatus",
            "AdmissionDate", "DischargeDate", "RoomNumber", "MedicalRecordNumber", "MedicareNumber", "MedicaidNumber"
        ])
        writer.writerows(data)

# Generate data and save to CSV
resident_data = generate_resident_data()
save_to_csv(resident_data)

print("Sample dataset of 10 residents for nursing home patients using MDS 3.0 standard has been saved to nursing_home_residents_mds3.csv")
