from flask import Flask , render_template , request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

app= Flask(__name__)

#reading the train file
df=pd.read_excel("Static/DatasetsUsed/Train.xlsx")
y_train=df['Label']
x_train=df['News']

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.8)
tfidf_train=tfidf_vectorizer.fit_transform(x_train)

f1=open("model.pck",'rb')
model=pickle.load(f1)


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/', methods=['GET','POST'])
def Predict():
    if (request.method == 'POST'):
       x_Test = np.array([request.form.get('content')])
       tfidf_test = tfidf_vectorizer.transform(x_Test)
       y_pred = model.predict(tfidf_test)
       return render_template('Index.html', prediction=y_pred)

    return render_template('Index.html', prediction=y_pred ,scroll='login')

if __name__== "__main__":
    app.run(debug=True)