#import libraries
import requests
import re
from bs4 import BeautifulSoup
from requests import get
url = "https://hackr.io/tutorials/learn-adobe-experience-design"
response = get(url)

#We’ll now create a BeautifulSoup object, or a parse tree. This object takes as its arguments the page.text document from Requests (the content of the server’s response) and then parses it from Python’s built-in html.parser.
soup = BeautifulSoup(response.text, 'html.parser')

# Pull all text from the tuturial divison that contains course listing
courses = soup.find_all('div', class_ ="tut-list tut-list-new tut-row")


# Lists to store the scraped data in
CourseTitles = []
Votes = []
CourseLink = []
AuthorName = []
AuthorLink = []
HackrLink = []
CourseCost = []
CourseType = []
StudentType = []


    
for course in courses:
    CourseTitle = course.div.find('span', class_ = 'tutorial-title-txt').text.strip()
    CourseTitles.append(CourseTitle)


    NoOfVote  = course.div.find('span', class_ = 'count').text.strip()
    Votes.append(NoOfVote)

    Link1 = course.find("div", class_="title-links no-margin").find('a')["href"]
    CourseLink.append(Link1)
    
    Name = course.find("a", class_="author no-marginright paddingleft-xs")
    if Name is None:
        AuthorName.append(None)
    else:
        Names=Name.text.strip()
        AuthorName.append(Names)
    
    auth  = course.find("div", class_="action author").find('a')
    if auth is None:
        AuthorLink.append(None)
    else:
        Link2 = auth["href"]
        AuthorLink.append(Link2)
    
    hackr = course.find("a", attrs={'href': re.compile("https://hackr.io/tutorial/")}) 
    if hackr is None:
        HackrLink.append(None)
    else:
        Link3=hackr.get("href")
        HackrLink.append(Link3)
        
    features  = course.find_all('div', class_ = "tut-label-group marginright-sm")
    for future in features:
        x=future.text.split()
    feat1 = x[0]
    if len(x) > 2:
        feat2 = x[1]
        feat3 = x[2]
    elif x[1] == ("Beginner" or "Advanced"):
        feat2 =None
        feat3= x[1]
    else:
        feat2 = x[1]
        feat3 = None
    CourseCost.append(feat1)
    CourseType.append(feat2)
    StudentType.append(feat3)


import pandas as pd
AdobeXDCourses = pd.DataFrame({'Course': CourseTitles,
'Votes': Votes,
"Course Link":CourseLink,
"Author ":AuthorName,
"Author Link":AuthorLink,
"Hackr Link":HackrLink,
"Course Cost":CourseCost,
"Course Type":CourseType,
"Course Cost":CourseCost,
"Student Type":StudentType
})

AdobeXDCourses.to_csv('AdobeXD.csv')