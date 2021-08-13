# Flask sendmail not showing any errors, but no email received
from flask import Flask , render_template , request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from flask_mail import Mail, Message

app= Flask(__name__)

#reading the train file
df=pd.read_excel("Static/DatasetsUsed/Train.xlsx")
y_train=df['Label']
x_train=df['News']

tfidf_vectorizer=TfidfVectorizer(stop_words='english', max_df=0.8)
tfidf_train=tfidf_vectorizer.fit_transform(x_train)

f1=open("model.pck",'rb')
model=pickle.load(f1)
f1.close()


@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/', methods=['GET','POST'])
def Predict():
    if request.form.get('content') :
        if (request.method == 'POST'):
            x_Test = np.array([request.form.get('content')])
            tfidf_test = tfidf_vectorizer.transform(x_Test)
            y_pred = model.predict(tfidf_test)
            return render_template('Index.html', prediction=y_pred , scroll='detection')

    return render_template('Index.html')


# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'musk.prat.pri.radha@gmail.com'
app.config['MAIL_PASSWORD'] = 'FakeNewsWebsite1'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
mail = Mail(app)

@app.route('/', methods=['GET','POST'])
def feedback():
    if (request.method == 'POST'):
        name = request.form.get('Name')
        phone = request.form.get('Phone')
        email = request.form.get('Email')
        Feedback = request.form.get('Feedback')

    msg = Message("Hello",
                  sender="musk.prat.pri.radha@gmail.com",
                  recipients=["1234muskangupta@gmail.com"])

    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)


    return render_template('Index.html', sent='not success')

if __name__== "__main__":
    app.run(debug=True)