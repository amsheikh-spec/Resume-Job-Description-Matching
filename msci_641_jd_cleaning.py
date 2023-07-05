# -*- coding: utf-8 -*-
"""MSCI 641 - JD Cleaning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nHLK6KZoyDGPQKQvza-4mB3FsUrZcoqC
"""

# Importing Job Description New
import pandas as pd
jd = pd.read_csv("/content/Job Description New.csv")
jd.head(5)

# Data Preprocessing:
## 1. Keeping selected columns
selected_col = ['Title', 'jobpost']
jd_new = jd[selected_col]
jd_new.head(5)

pd.set_option('display.max_rows', None)
title_count = jd_new['Title'].value_counts()
#print(title_count)

#print(jd_new.loc[0, 'jobpost'])

#2. Data Cleaning
import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Convert title to lowercase
jd_new['title'] = jd_new['Title'].str.lower()

# Remove punctuation
jd_new['title'] = jd_new['title'].str.translate(str.maketrans('', '', string.punctuation))

jd_new.head(5)

specific_job_titles = ['software developer', 'systems administrator', 'project manager', 'web developer', 'database administrator', 'java developer', 'python developer', 'network administrator', 'security analyst']
jd_filtered = jd_new[jd_new['title'].isin(specific_job_titles)]
jd_filtered["title"].value_counts()

# Convert the job descriptions to lowercase
jd_filtered['job_description'] = jd_filtered['jobpost'].str.lower()

# Remove punctuation
jd_filtered['job_description'] = jd_filtered['job_description'].str.translate(str.maketrans('', '', string.punctuation))

# Remove stop words
stop_words = set(stopwords.words('english'))
jd_filtered['job_description'] = jd_filtered['job_description'].apply(lambda x: ' '.join(word for word in word_tokenize(x) if word not in stop_words))

jd_filtered.head(5)

selected_col = ['title', 'job_description']
jd_filtered = jd_filtered[selected_col]
jd_filtered.head(5)

# Save preprocessed jd:
jd_filtered.to_csv('preprocessed_jd.csv', index=False)

