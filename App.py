from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from flask_mail import Mail, Message
from goose3 import Goose


# creating flask object
app = Flask(__name__)


# configuration of mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'senders_mail@gmail.com'
app.config['MAIL_PASSWORD'] = 'Password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
mail = Mail(app)


# reading the dataset from excel file
df = pd.read_excel("Static/DatasetsUsed/Train.xlsx")
y_train = df['Label']
x_train = df['News']

#Initialize a Tf-idf Vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.8)

#Fitting and transforming training data set
tfidf_train = tfidf_vectorizer.fit_transform(x_train)


# Loading Logistic Regression model
f1 = open("model.pck", 'rb')
model = pickle.load(f1)
f1.close()



# Function for predicting credibility of news from the news content provided
def Predict(text):
    x_Test = np.array([text])
    tfidf_test = tfidf_vectorizer.transform(x_Test)
    y_pred = model.predict(tfidf_test)
    return y_pred


# Function for accepting feedback and sending mail
def feedback():
    name = request.form.get('Name')
    phone = request.form.get('Phone')
    email = request.form.get('Email')
    Feedback = request.form.get('Feedback')

    msg = Message("Feedback for Fake News Detection Website",
            sender="senders_mail@gmail.com",
            recipients=["receiver1@gmail.com","receiver2@gmail.com",
                        "receiver3@gmail.com","receiver4@gmail.com"])

    msg.body = '''Hey developers,
    A Client just viewed your website. The Details of feedback are:
                  
    Name of client: %s
    Phone number: %s
    Email address: %s
    Feedback from client: %s
    '''%(name,phone,email,Feedback)

    mail.send(msg)



@app.route('/')
def home():
    return render_template('Index.html')


@app.route('/', methods=['GET', 'POST'])
def get_val():
    if (request.method == 'POST'):

        if request.form["Submit_B"]=="newsContent":
            text = request.form.get('content')
            return render_template('Index.html', prediction=Predict(text) , scroll="detection")


        elif request.form["Submit_B"]=="URLnews":
            g = Goose()
            userLink = str(request.form.get('NewsUrl'))
            text = g.extract(url=userLink)
            if 'timesofindia' not in userLink:
                scraped_text = text.cleaned_text
            else:
                scraped_text = text.title

            return render_template('Index.html', prediction=Predict(scraped_text), scroll='detection')


        elif request.form["Submit_B"]=="message":
            if request.form.get('Feedback'):
                feedback();
                return render_template('Index.html', scroll="contact_us", send="success")

            else:
                return render_template('Index.html', scroll="contact_us", send="not success")


    return render_template('Index.html')


if __name__ == "__main__":
    app.run(debug=True)
