# imports
import apiKey
import json
import requests
import config

base = "https://lapi.transitchicago.com/api/1.0/ttarrivals.aspx"

# this is the string builder for the final URL, allowing the data inside to be changed rather than hard coded.
finalUrl = base + "?key=" + apiKey.key + "&stpid=" + str(config.stopID) + "&max=" + str(config.amt) + "&outputType=" + config.outputType


# request block
# this part I got from a youtube tutorial, as I couldn't figure out how to
# get a request working. His github repo can be found at this link:
# https://github.com/kpphillips/Pythonista-Projects/tree/master/CTA%20Bus%20Tracker%20API
def request(URL):
    r = requests.get(URL)
    parsedJson = json.loads(r.content)
    return parsedJson

def apiCall(finalURL):
    trainDict = request(finalURL)
    return trainDict

def line(trainDict):
    lineList = []
    for x in range(config.amt):
        lineList.append(trainDict["ctatt"]["eta"][x]["rt"])
    return lineList

def runNum(trainDict):
    runNumList = []
    for x in range(config.amt):
        runNumList.append(trainDict["ctatt"]["eta"][x]["rn"])
    return runNumList

def dest(trainDict):
    destList = []
    for x in range(config.amt):
        destList.append(trainDict["ctatt"]["eta"][x]["destNm"])
    return destList

def arrT(trainDict):
    arrTList = []
    for x in range(config.amt):
        arrTList.append(trainDict["ctatt"]["eta"][x]["arrT"])
    return arrTList

def approach(trainDict):
    appList = []
    for x in range(config.amt):
        appList.append(trainDict["ctatt"]["eta"][x]["isApp"])
    return appList

def delayed(trainDict):
    delList = []
    for x in range(config.amt):
        delList.append(trainDict["ctatt"]["eta"][x]["isDly"])
    return delList


