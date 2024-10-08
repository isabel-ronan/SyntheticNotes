# Synthetic Nurse Notes for Palliative Care Research
Developing AI-driven nursing home care notes for preliminary machine learning experiments.

**Author:** Isabel Ronan (inspired by [Eva Rombouts](https://github.com/ekrombouts/))

## Project overview
**Fictitious Data Creation:** We use OpenAI to create a potentially realistic dataset of clinical notes for palliative care research in nursing homes. This protects the privacy and upholds the ethical handling of sensitive patient data.
**Data Analysis:** Notes were assessed by a qualified nurse to determine quality. Additionally, notes were blindly labelled by the nurse to compare against the model's labels. Readability metrics were also calculated.

## Collaboration
Please reach out to me at my [email address](mailto:118441194@umail.ucc.ie) should you wish to communicate with me regarding the same. 

## Additional Information
- `./offlineResearch/` directory uses Python version (3.12.6) and Pip version (24.2). 
- All necessary packages can be installed using the `./offlineResearch/requirements.txt` file. 
- Additionally run the `python -m spacy download en_core_web_sm` command in your python environment to install additional Spacy dependencies.

