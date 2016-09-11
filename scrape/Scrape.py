'''
Created on Sep 10, 2016

@author: pgrewal
'''

from bs4 import BeautifulSoup   # scrape
import io   # file io
import re   # regex
from Event import Event

class Scrape(object):

    summaries = []
    dates = []
    times = []
    detailLinks = []
    imageLinks = []
    htmlFile = ""
    soup = None

    def __init__(self, htmlFile):
        self.htmlFile = htmlFile
        
        with io.open(htmlFile,'r',encoding='utf8') as f:
            htmlPage = f.read()

        self.soup = BeautifulSoup(htmlPage, "html.parser")
        
    def getBh(self):
        i = 0
        venue = self.soup.title.string
        print(venue)
        
        for tag in self.soup.find_all(class_=re.compile("^list-view-item")): 
            ev = Event()
            ev.venue = venue
            
            ev.summary = tag.find(class_="headliners summary").a.string     # tag.h1.a.string
            
            ev.date = tag.find(class_="dates").string                       # tag.h2.string
            
            timedoorTag = tag.find(class_="times").find(class_="doors")
            if(timedoorTag is not None):
                ev.timedoor = timedoorTag.string #.find(class_="doors").string
            else:
                ev.timedoor = ""
                
            timeshowTag = tag.find(class_="times").find(class_="start dtstart")
            timeshowTagDate = timeshowTag.find(class_="value-title")
            if(timeshowTagDate is not None):
                ev.timeshow = timeshowTagDate["title"]
            else:
                ev.timeshow = "" 
            if(timeshowTag is not None):
                ev.timeshowEng = timeshowTag.text   # Note the text instead of string
            else:
                ev.timeshowEng = ""

            ev.imageLink = tag.a.img["src"]

            ev.detailLink = tag.find(class_="more-info").a["href"]
            
             
            priceTag = tag.find(class_="ticket-price")   
            priceRange = priceTag.find(class_="price-range")
            if(priceTag.find(class_="sold-out") is not None):
                ev.ticketStatus = "Sold out"
                ev.price = priceRange.text
                ev.ticketLink = ""
            elif(priceTag.find(class_="free") is not None):
                ev.price = "Free"
                ev.ticketLink = ""  
            elif(priceTag.find(class_="tickets-at-the-door") is not None):
                ev.ticketStatus = "Tickets at the Door"
                ev.price = priceRange.text
                ev.ticketLink = ""  
            elif(priceTag.find(class_="custom") is not None):
                ev.ticketStatus = priceTag.find(class_="custom").string
                ev.ticketLink = ""                                               
            elif(priceTag.find(class_="future-sale") is not None):
                futureSale = priceTag.find(class_="future-sale")
                ev.ticketStatus = futureSale.a.text
                ev.price = priceRange.text
                ev.ticketLink = futureSale.a["href"] 
            else:
                ev.price = priceTag.find(class_="price-range").text
                ev.ticketLink = priceTag.find(class_="ticket-link primary-link").a["href"]
            
            performers = tag.find(class_="supports description")
            if(performers is not None):
                ev.performers = performers.a.text
                ev.performersParse()
            else:
                ev.performers = ""
            
            print(ev.toString())

   
scr = Scrape("Bh.html")
scr.getBh()
