import requests
import time
import itertools

# which stops to be used, these can be found at https://www.metrotransit.org/nextrip or on Google Maps by clicking on stop
Stops = ('170', '20048', '16839', '16837')

def getAPI(stopID):
    url = 'https://svc.metrotransit.org/NexTrip/'
    global response
    response = []
    for x in stopID:
        response.append(requests.get(url + x + '?format=json').json())
    response = list(itertools.chain.from_iterable(response))
    return response

def updateList(rawList):
    updatedList = []
    currentTime = round(time.time())
    i=0
    if bool(rawList) == False:
        updatedList.append('N/A')
    else:
        while i < len(rawList) and i < 3:
            updatedList.append((round(((int(rawList[i]['DepartureTime'][6:19]) / 1000) - currentTime) / 60)))
            i+=1
    return updatedList

def getTimes(updatedList):
     #to filter out the exact route and direction I wanted as there are multiple routes that stop at each stop
    NB = updateList(list(filter(lambda c: c['RouteDirection'] == 'NB' and c['Route'] == '4', response)))
    SB = updateList(list(filter(lambda c: c['RouteDirection'] == 'SB' and c['Route'] == '4', response)))
    EB = updateList(list(filter(lambda c: c['RouteDirection'] == 'EB' and c['Route'] == '21', response)))
    WB = updateList(list(filter(lambda c: c['RouteDirection'] == 'WB' and c['Route'] == '21', response)))
    NB_Times = ','.join([str(elem) for elem in NB if elem == True and elem < 100])
    SB_Times = ','.join([str(elem) for elem in SB if elem == True and elem < 100])
    EB_Times = ','.join([str(elem) for elem in EB if elem == True and elem < 100])
    WB_Times = ','.join([str(elem) for elem in WB if elem == True and elem < 100])
    
    busRoutes = ['4N', '4S', '21E', '21W']
    busTimes = [NB_Times, SB_Times, EB_Times, WB_Times]
    i=0
    while i < len(busTimes):
        if busTimes[i] == '':
            busTimes[i] = 'N/A'
        i+=1

   
    return [busRoutes, busTimes]
    
    
    # run every 60 seconds
    
    
response = getAPI(Stops)
updatedList = updateList(response)
times = getTimes(updatedList)
print((times[1]))
