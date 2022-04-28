import requests
import json
import time
import itertools

Stops = ('170', '20048', '16839', '16837')

def getAPI(stopID):
    url = 'https://svc.metrotransit.org/NexTrip/'
    response = []
    for x in stopID:
        response.append(requests.get(url + x + '?format=json').json())
    response = list(itertools.chain.from_iterable(response))
    return response                                                          #response = raw data from MetroTransit - each index is unique and all stops combined

def updateList(lst):
    currentTime = round(time.time())
    updatedList = []
    i = 0
    while i < len(lst):
        updatedList.append((round(((int(lst[i]['DepartureTime'][6:19]) / 1000) - currentTime) / 60)))
        updatedList.append(lst[i]['Route'])
        updatedList.append(lst[i]['RouteDirection'])
        i += 1
    updatedList = sorted(list(zip(*[iter(updatedList)]*3)))
    # updatedList = [i for i in updatedList if i[0] >= 8]                #filters so only show buses that you could walk to are - comment out if you want to show all               
    return updatedList

def getTimes(updatedList):
    times = []
    i=0
    while i < len(updatedList) and i < 8:
        times.append(str(updatedList[i][0]))
        times.append(updatedList[i][1] + updatedList[i][2][0])
        i+=1
    i=0
    while i in range(16):
        if len(times) < 16:
            times.append('N/A')
        i+=1
        return list(zip(*[iter(times)]*2))

response = getAPI(Stops)
updatedList = updateList(response)
times = getTimes(updatedList)
print(times)