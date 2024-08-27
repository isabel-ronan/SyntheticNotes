from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pandas as pd
import operator
from gensim.parsing.preprocessing import remove_stopwords
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

unmet_nurse_notes = ""
met_nurse_notes = ""
unmet_carer_notes = ""
met_carer_notes = ""
for x in os.listdir('./data'):
    temp_dataframe = pd.read_csv('./data/' + x)
    if x.endswith("_unmetNeeds.csv"):
        for i in range(len(temp_dataframe['Notes'])):
            text = temp_dataframe['Notes'][i]
            filtered_words = remove_stopwords(text)
            if temp_dataframe['Role'][i] == 'Nurse':
                unmet_nurse_notes += filtered_words
            else:
                unmet_carer_notes += filtered_words
    elif x.endswith("_metNeeds.csv"): 
        for i in range(len(temp_dataframe['Notes'])):
            text = temp_dataframe['Notes'][i]
            filtered_words = remove_stopwords(text)
            if temp_dataframe['Role'][i] == 'Nurse':
                met_nurse_notes += filtered_words
            else:
                met_carer_notes += filtered_words

# print("Carer Met:", met_carer_notes)
# print("----------------------------")
# print("Nurse Met:", met_nurse_notes)
# print("----------------------------")
# print("Carer Unmet:", unmet_carer_notes)
# print("----------------------------")
# print("Nurse Unmet:", unmet_nurse_notes)

            
documents = [met_nurse_notes, met_carer_notes, unmet_nurse_notes, unmet_carer_notes]
document_names = ["Met Needs Nurse Notes", "Met Needs Carer Notes", "Unmet Needs Nurse Notes", "Unmet Needs Carer Notes"]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = vectorizer.get_feature_names_out()
tfidf_values = {}

for doc_index, doc in enumerate(documents):
    feature_index = tfidf_matrix[doc_index, :].nonzero()[1]
    tfidf_doc_values = zip(feature_index, [tfidf_matrix[doc_index, x] for x in feature_index])
    tfidf_values[doc_index] = {feature_names[i]: value for i, value in tfidf_doc_values}

dataframe = pd.DataFrame()
for i in range(len(tfidf_values.keys())):
    tfidf_values[i] = dict(sorted(tfidf_values[i].items(), key=operator.itemgetter(1), reverse=True))
    dataframe[document_names[i]] = tfidf_values[i]

dataframe.to_csv("frequency_of_words.csv")

wordcloud = WordCloud().generate(unmet_carer_notes)
plt.imshow(wordcloud)
plt.savefig('unmet_carer_notes.png')

wordcloud = WordCloud().generate(met_carer_notes)
plt.imshow(wordcloud)
plt.savefig('met_carer_notes.png')

wordcloud = WordCloud().generate(unmet_nurse_notes)
plt.imshow(wordcloud)
plt.savefig('unmet_nurse_notes.png')

wordcloud = WordCloud().generate(met_nurse_notes)
plt.imshow(wordcloud)
plt.savefig('met_nurse_notes.png')