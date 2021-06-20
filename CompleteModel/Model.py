import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

#reading the train file
df=pd.read_csv("Static/Train.csv")

y_train=df['Label']
x_train=df['News']

#Initialize a TfidfVectorizer
tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.8)
#Fit and transform train set, transform test set
tfidf_train=tfidf_vectorizer.fit_transform(x_train)
#tfidf_test=tfidf_vectorizer.transform(x_ans)

#Initialize a PassiveAggressiveClassifier
model=PassiveAggressiveClassifier(max_iter=50)
model.fit(tfidf_train,y_train)

#y_pred=model.predict(tfidf_test)

file=open("model.pck",'wb')
pickle.dump(model,file)
file.close()