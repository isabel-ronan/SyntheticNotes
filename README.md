# Synthetic Nurse Notes for Palliative Care Research
Developing AI-driven nursing home care notes for preliminary machine learning experiments.

## Project overview
**Fictitious Data Creation:** We use OpenAI to create a potentially realistic dataset of clinical notes for palliative care research in nursing homes. This protects the privacy and upholds the ethical handling of sensitive patient data.
**Data Analysis:** Notes were assessed by qualified healthcare practitioners to determine how close to real-life practice the synthetically generated notes are. Additionally, quantitative metrics are calculated to determine how similar the outputted data is to the input data. 

## Additional Information
- `./offlineResearch/` directory uses Python version (3.12.6) and Pip version (24.2). 
- All necessary packages can be installed using the `./offlineResearch/requirements.txt` file. Package list created using `pip list --format=freeze > requirements.txt` command.
- Additionally run the `python -m spacy download en_core_web_sm` command in your Python environment to install additional Spacy dependencies.

