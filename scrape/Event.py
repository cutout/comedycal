'''
Created on Sep 11, 2016

@author: pgrewal
Event details
'''

class Event(object):

    venue = ""
    summary = ""
    date = ""
    timedoor = ""
    timedoorEng = ""
    timeshow = ""
    timeshowEng = ""
    detailLink = ""
    imageLink = ""   
    ticketLink = ""
    ticketStatus = ""
    price = ""
    ageRestriction = ""
    performers = ""
    performersList = []

    def __init__(self):
        '''
        Constructor
        '''
        
    def toString(self):
        s = "venue: " + self.venue + ", " 
        s += "summary: " + self.summary + ", "
        s += "date: "+ self.date + ", "
        s += "timedoor: " + self.timedoor + ", "
        s += "timedoorEng: " + self.timedoorEng + ", "
        s += "timeshow: " + self.timeshow + ", "
        s += "timeshowEng: " + str(self.timeshowEng) + ", "
        s += "detailsLink: " + self.detailLink + ", "
        s += "imageLink: " + self.imageLink + ", "
        s += "ticketLink: " + self.ticketLink + ", "
        s += "ticketStatus: " + self.ticketStatus + ", "
        s += "price: " + self.price + ", "
        #s += "performers: " + self.performers + ", "
        s += "performersList: " + str(self.performersList)
        return s
        
    def performersParse(self):
        print("Parsing performer list")
        self.performersList = self.performers.split(",")       
        