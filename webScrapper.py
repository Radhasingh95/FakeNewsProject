# script to scrape content from link
#dependencies: pyflask.py (muskan's backend file) to fetch url, send timePublished, genre, text to be added to DB
#-----------------------------------------------------------------------------------------------------------------
userLink = "https://timesofindia.indiatimes.com/tv/news/hindi/a-10-hour-shift-isnt-enough-to-shoot-a-daily-soap-say-producers/articleshow/83308584.cms"
#-----------------------------------------------------------------------------------------------------------------
#import stuff
import requests
from bs4 import BeautifulSoup
from goose3 import Goose
g = Goose()
text = ""
#function to scrape blogspot blogs
def blogspotScrapper():
    
    global text 
    text = soup.find_all("p")
    title = text[0]
    text = text[1:]
    #TODO prettify and store all the p tag stuff

#-----------------------------------
def TOIScrapper():
    global text 
    text = g.extract(url=userLink)
    with open("sampleTOI.txt", 'a') as ut:
        print(text.title) #TODO check clean text function 
#-----------------------------------

url = requests.get(userLink) #url only prints status code, use userLink for linkSource checks
if url.status_code != 200:
    #TODO add error as a dialog box in frontend
    print("Error fetching website. Check link.")
    #terminate program

src = url.content
soup = BeautifulSoup(src,'html.parser')

#if link from blogspot
if ('blogspot' in userLink):
    blogspotScrapper()
elif ('timesofindia' in userLink):
    TOIScrapper()

##debug
#text_file = open("sample1.txt", "w")
#n = text_file.write(str(text))
#text_file.close()
#