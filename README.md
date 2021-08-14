Fake news and other types of false information can take on different faces. They can also have major impacts - Financial impacts or impacts on our health, Fear, Racist ideas, Bullying and violence against innocent people, Democratic impacts. Fake news can reduce the impact of real news by competing with it. It  also has the potential to undermine trust in serious media coverage.

This project is our initiative to combat these impacts by providing users an easy way to check if the news is real or not.


# Fake News Detection Website Project

For getting news these days, one has an ‘n’ number of sources via the media. There are news channels, newspapers, magazines, websites, newsletters and much more. However , how does one determine which news is fake, which is not? At times, one gets perplexed. We do not know what  to believe, who to go to for the real meat at times.

The prevalence of fake news has increased with the rise of social media. The use of anonymously-hosted fake news websites has made it difficult to prosecute sources of fake news for libel. 

<img src="https://economictimes.indiatimes.com/thumb/msid-74910166,width-1200,height-900,resizemode-4,imgsize-650870/fake-news-getty.jpg?from=mdr" width="350" height="200" align = "center" />

Fake news detection website is a utility tool that is used to detect whether the given news is fake or not, and show statistics of fake news year wise , country wise, and platform wise.

## Abstract

- The website’s front end is developed using HTML, with styles added using CSS and responsive elements added using JavaScript.
- In the backend, a dataset was created using data from various sources which was tokenized using TF-IDF vectorizer and our model was trained using Logistic Regression. 
- The Flask module was used to collect user input from the website, which was also tokenized using TF-IDF vectorizer and prediction was made by the model.The result was sent to the front end for display.
- News data from various sources was analysed and visualized using python libraries like pandas, matplotlib, seaborn and charts were displayed on the website. 

This Project comes up with the applications of NLP (Natural Language Processing) techniques for detecting the 'fake news', that is, misleading news stories that comes from the non-reputable sources. 

## Working Methodology

### Dataset Creation

The news datasets downloaded from github repositories as well as kaggle and merged them as one CSV file.
The dataset was then analyzed for biases and randomized to make for unbiased training.

### Comparing different models and vectorizers

The dataframe was cleaned by removing stop words and lemmatizing words in data. The dataset was then vectorized using TF-IDF Vectorizer to map every word to a mathematical vector based on the inverse of their frequencies in the dataset. 

This vectorized dataset was ready to be split in order to train as well as test models made using different classification algorithms. We trained our models using popular classification algorithms such as KNN, PassiveAgressive and Logistic Regression. The accuracy scores of these models were compared. It was observed that Logistic Regression gave the highest accuracy of **94.5%.** This model was dumped into a pickle file for future use in predictions.

<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/Implementation.PNG" />

### Front-end Development

The front-end is developed using HTML, CSS and JavaScript. The website was divided into following components-
- **Home**: A beautiful and welcoming home page whose background changes with time.

<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/Home%20page.PNG" width="600" height="350" />

- **Introduction**: A section that introduces users to fake news, its impacts and the purpose of the website. 

<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/introduction.PNG" width="600" height="350" />

- **Detection**: The heart of the website. This is where users can detect the credibility of news by either submitting a URL or the entire except.


<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/Detection.PNG" width="600" height="350" />

- **Statistics**: Hosts charts that show the trends of fake news spread based on various factors.

<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/statistics.PNG" width="600" height="350" />

- **About Us**: A small introduction to the developing team along with links to their socials.
- **Contact Us**: Since this is a research project, feedback is really important. Filling the form would send each member of development team an email with details of sender and feedback.

<img src="https://github.com/Radhasingh95/FakeNewsProject/blob/main/Website_images/contact%20us.PNG" width="600" height="350" />

### Back-end Development

The front end of the website was integrated with the prediction code using a python module named flask. The python file constantly runs in the background to enable computing on the website. The flask file has the following components: 
- Setting up constants and importing modules: The model is unpickled to enable prediction. Necessary modules are imported.
- Looking for inputs from website: The file keeps waiting for inputs from any text box to take necessary action.
- Text Cleaning and Encoding for Prediction: Once the user enters content, the text is tokenized and encoded using same principles mentioned in Section 2.2. 
- Text Prediction: The model then takes the input encoded text and predicts based on its learning during the training phase. This predicted value (0 or 1) is then returned to the front end where it is beautifully displayed.
- Web Scraping: if a user enters a URL, the goose() object will then scrape all necessary text which is then sent for encoding and prediction as discussed in 3 and 4. 
- Contact Us: This code snippet looks for inputs in the contact us form, then sends an E-Mail to all the developers of this project using the flask_mail object.

### Analysing and visualising trends on the website

To introduce users to various trends observed in the spread of fake news, data was obtained from statistical websites which was then visualised using matplotlib and seaborn python modules. These graphs were saved and used by the front end of the website.

You can view the file here: [https://github.com/Radhasingh95/FakeNewsProject/blob/main/Statistics.ipynb]

 
## How to Run the Code

- Fork and clone the repository.
- Install the following modules in python
     1. pip install sklearn
     2. pip install flask
     3. pip install goose3
     4. pip install Flask-Mail
     5. pip install pandas
     6. pip install numpy
- Change sender and recipient's email address in app.py file for the feedback part. Configure flask mail by adding the sender's email address and corresponding password in MAIL_USERNAME and MAIL_PASSWORD under configuration part. 
- Ensure the sender mail has ‘access from less secure apps’ enabled. For gmail IDs, this can be done from the accounts page - Account 
- Run app.py
- Open the website from local host: http://127.0.0.1:5000/
