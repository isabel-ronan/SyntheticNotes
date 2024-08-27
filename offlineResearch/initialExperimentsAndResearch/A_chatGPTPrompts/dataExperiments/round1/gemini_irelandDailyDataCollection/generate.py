import csv

residents = [
    # Name, Age, County, Data Notes
    ["Maureen O'Sullivan", 82, "Kerry", "Woke up feeling refreshed. Enjoyed breakfast (porridge and fruit). Participated in morning chair yoga with good mobility. Blood pressure: 130/80 mmHg."],
    ["Sean Murphy", 78, "Cork", "Reports feeling a bit stiff this morning. Assisted with dressing and personal hygiene. Ate half of his breakfast (eggs and toast). Blood sugar: 7.2 mmol/L. Scheduled for physiotherapy later today."],
    ["Eileen Kelly", 91, "Galway", "Slept well. Appears in good spirits. Engaged in conversation during breakfast (cereal and milk). Requested assistance with showering. Blood pressure: 145/90 mmHg. Medication review scheduled for this afternoon."],
    ["Patrick Ryan", 85, "Dublin", "Restless night due to back pain. Took pain medication as prescribed. Assisted with transferring to wheelchair. Refused breakfast but enjoyed a cup of tea. Pain level: 5/10. Nurse to monitor pain throughout the day. "],
    ["Áine Ní Cheallaigh", 76, "Donegal", "Independent with daily activities. Enjoyed social time with other residents during breakfast (fruit and yogurt). Scheduled for a video call with family later today. Blood pressure: 120/70 mmHg."],
    ["Michael Brennan", 88, "Mayo", "Reports feeling anxious this morning. Participated in a calming hand massage session. Drank fluids well. Ate half of his breakfast (scrambled eggs). Blood pressure: 150/85 mmHg. Scheduled to speak with a social worker this afternoon."],
    ["Siobhán O'Connor", 80, "Clare", "Appears withdrawn this morning. Encouraged to participate in group activities. Ate a small breakfast (toast and jam). Blood pressure: 110/60 mmHg. Nurse to assess mood and offer support. "],
    ["Liam O'Reilly", 90, "Limerick", "Independent with most daily activities. Enjoyed breakfast (pancakes and syrup). Reported feeling a bit forgetful this morning. Cognitive assessment scheduled for next week. Blood pressure: 135/88 mmHg."],
    ["Brigid Flaherty", 84, "Wexford", "Requires assistance with all daily activities. Appears content. Enjoyed pureed breakfast (fruit and yoghurt). Blood pressure: 125/75 mmHg. Scheduled for occupational therapy to practice using adaptive equipment."],
    ["Dáithí Walsh", 79, "Waterford", "Energetic and chatty this morning. Participated in a morning walk with assistance. Enjoyed a full breakfast (sausage and potatoes). Blood pressure: 140/90 mmHg. Scheduled for podiatry appointment this afternoon."],
]

# Create CSV file with headers
with open("nursing_home_residents.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Age", "County", "Data Notes"])

    # Write resident data to CSV file
    for resident in residents:
        writer.writerow(resident)

print("CSV file generated successfully!")