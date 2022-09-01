import collections
import apiInfo
import config
import format
import time

global test
test = []

def finalOutput():
    for x in range(config.amt):
        print(format.lineDict[lineList[x]] + " line run number: " + str(runNumList[x]) + " to " + destList[
            x] + ", Scheduled to Arrive at: " + str(arrTList[x]),
              format.approachDict[approachList[x]] + format.delayDict[delayedList[x]])

    return False


def dataGrab():
    dataStorage = apiInfo.apiCall(apiInfo.finalUrl)

    lineList = (apiInfo.line(dataStorage))
    runNumList = (apiInfo.runNum(dataStorage))
    destList = (apiInfo.dest(dataStorage))
    arrTList = (apiInfo.arrT(dataStorage))
    approachList = (apiInfo.approach(dataStorage))
    delayedList = (apiInfo.delayed(dataStorage))

    return lineList, runNumList, destList, arrTList, approachList, delayedList


def comparison(lineList, runNumList, destList, arrTList, approachList, delayedList):
    if (len(test) == 0):
        for data in runNumList:
            test.append(data)
    else:
        for data in lineList:
            if collections.Counter(test) != collections.Counter(runNumList):
                print("Change")
            if collections.Counter(test) == collections.Counter(runNumList):
                print("Same")
    return False


while True:
    lineList, runNumList, destList, arrTList, approachList, delayedList = dataGrab()
    comparison(lineList, runNumList, destList, arrTList, approachList, delayedList)
    finalOutput()
    time.sleep(10)

# print(apiInfo.finalUrl)
# trainDict = apiInfo.request(apiInfo.finalUrl)

# print (len(trainDict))

# print (trainDict)
# print(trainDict["ctatt"]["eta"][1]['rt'])

# for amt in trainDict["ctatt"]["eta"]:
# print(1)
