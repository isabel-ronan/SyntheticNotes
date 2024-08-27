# OpenAI Usage


- Data generated using the following prompt: "John was assisted with a shower this morning. He had his lunch in the canteen, he ate half a bowl of soup, half a chicken salad and a full bowl of ice cream along with 2 cups of tea. Johns sister Mary came to see him today, he was in good form. He experienced some nausea in the evening and was given Zofran (anti emetic) with good relief from same. John was given his regular analgesia and has no complaints of pain with same. John’s sister has expressed her concern that his mobility is reduced and an appointment with the GP has been scheduled for tomorrow."
- Query was divided into two main parts with further subdivisions. 
- Processing was carried out using Google Colab and was inspired by the work of [Eva Rombouts](https://github.com/ekrombouts/GenCareAI).
- Further details of the data generation process can be found at this [GitHub Repo Link](https://github.com/isabel-ronan/GenCareAI). 




## Query Part One - System Role


- "You are a specialist in generating fictitious data for natural language processing projects in healthcare. You speak the language of a nurse in an Irish nursing home. Namely, you speak hiberno-English."



## Query Part Two - Note Generation


- unmet needs notes were generated seperately to met needs notes



### Query 2.A - unmet needs


- "This is an example of a nurse note for a patient in a day:
"John was assisted with a shower this morning. He had his lunch in the canteen, he ate half a bowl of soup, half a chicken salad and a full bowl of ice cream along with 2 cups of tea. Johns sister Mary came to see him today, he was in good form. He experienced some nausea in the evening and was given Zofran (anti emetic) with good relief from same. John was given his regular analgesia and has no complaints of pain with same. John’s sister has expressed her concern that his mobility is reduced and an appointment with the GP has been scheduled for tomorrow."
Other reports may include: washing, dressing, brushing teeth, getting ready for the day, getting ready for the night, showering, cleaning dental prostheses, or assistance after incontinence.
Other reports could include: what the client has or has not eaten, what help is needed with eating (full help, encouragement, adapted cutlery or cup), choking, keeping hydration and nutrition lists.
Other reports could include: Organised activities, getting visitors, browsing through a magazine, interacting with fellow residents. Keep in mind that these are reports from people in a nursing home, with severe disabilities, so social interaction and activities are limited. Usually it involves sociability, but not always.
Other reports may include, for example: oedema, pressure ulcers, peeling, redness and itching of the skin. Nails that are too long, blemishes.
Other reports could include, for example: care plan discussions, minor medical complaints, family requests, ordering medication.
Reports can be, for example, about: restlessness and wandering at night, sleeping well, going to the toilet at night, phoning, lying crookedly in bed.
Reports may include: agitation, restlessness, apathy, confusion; usually the confusion is subtle, but sometimes more intense.
Reports may include, for example: pain, tightness of breath, nausea, diarrhoea, back pain, palliative care; usually the complaints are subtle, but sometimes more severe.
Other reports can be about, for example: walking aids, the wheelchair, falls, fall incidents, transfers, lifts.
Most reports are about everyday things, so not everything is a serious incident.
Make up 25 such reports for 25 residents with unmet palliative care needs. Return only the reports separated by "\n---". Vary the sentence structure and style."



### Query 2.B - met needs


- "This is an example of a nurse note for a patient in a day:
"John was assisted with a shower this morning. He had his lunch in the canteen, he ate half a bowl of soup, half a chicken salad and a full bowl of ice cream along with 2 cups of tea. Johns sister Mary came to see him today, he was in good form. He experienced some nausea in the evening and was given Zofran (anti emetic) with good relief from same. John was given his regular analgesia and has no complaints of pain with same. John’s sister has expressed her concern that his mobility is reduced and an appointment with the GP has been scheduled for tomorrow."
Other reports may include: washing, dressing, brushing teeth, getting ready for the day, getting ready for the night, showering, cleaning dental prostheses, or assistance after incontinence.
Other reports could include: what the client has or has not eaten, what help is needed with eating (full help, encouragement, adapted cutlery or cup), choking, keeping hydration and nutrition lists.
Other reports could include: Organised activities, getting visitors, browsing through a magazine, interacting with fellow residents. Keep in mind that these are reports from people in a nursing home, with severe disabilities, so social interaction and activities are limited. Usually it involves sociability, but not always.
Other reports may include, for example: oedema, pressure ulcers, peeling, redness and itching of the skin. Nails that are too long, blemishes.
Other reports could include, for example: care plan discussions, minor medical complaints, family requests, ordering medication.
Reports can be, for example, about: restlessness and wandering at night, sleeping well, going to the toilet at night, phoning, lying crookedly in bed.
Reports may include: agitation, restlessness, apathy, confusion; usually the confusion is subtle, but sometimes more intense.
Reports may include, for example: pain, tightness of breath, nausea, diarrhoea, back pain, palliative care; usually the complaints are subtle, but sometimes more severe.
Other reports can be about, for example: walking aids, the wheelchair, falls, fall incidents, transfers, lifts.
Most reports are about everyday things, so not everything is a serious incident.
Make up 25 such reports for 25 residents with met palliative care needs. Return only the reports separated by "\n---". Vary the sentence structure and style."




