import apiInfo
import config
import format

dataStorage = apiInfo.apiCall(apiInfo.finalUrl)

lineList = (apiInfo.line(dataStorage))
runNumList = (apiInfo.runNum(dataStorage))
destList = (apiInfo.dest(dataStorage))
arrTList = (apiInfo.arrT(dataStorage))
approachList = (apiInfo.approach(dataStorage))
delayedList = (apiInfo.delayed(dataStorage))



def finalOutput():
    print("Currently scheduled trains:")
    for x in range(config.amt):
        print(format.lineDict[lineList[x]] + " line run number: " + str(runNumList[x]) + " to " + destList[x] + ", Scheduled to Arrive at: " + str(arrTList[x]),
              format.approachDict[approachList[x]] + format.delayDict[delayedList[x]])

    return False

finalOutput()



#print(apiInfo.finalUrl)
# trainDict = apiInfo.request(apiInfo.finalUrl)

# print (len(trainDict))

# print (trainDict)
# print(trainDict["ctatt"]["eta"][1]['rt'])

# for amt in trainDict["ctatt"]["eta"]:
# print(1)
