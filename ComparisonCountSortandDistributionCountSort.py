import random
import time

dataLists =[]
for i in range(0,1000):
    numri = random.randint(0,100)
    dataLists.append(numri)
    
    
    #Comparison Count Sort
def comparisonCountSort(list):
    start_time = time.time()
    dataDict = {}
    ListaeSortuar = []
    count = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] > list[j]:
                count = count + 1
        d = {count: list[i]}
        dataDict.update(d)
        count = 0
    for i in range(0, len(list)):
        try:
            ListaeSortuar.append(dataDict[i])
            continue
        except:
            data = 0
    print("%s seconds " % (time.time() - start_time))
    print('Lista e pa sortuar {}'.format(list))
    print('Lista e sortuar me Comparison Count Sort {}'.format(ListaeSortuar))

#Distribution Counting Sort
def DistributinCountSort(list):
    start_time = time.time()
    dataDict = {}
    unique = set(list)
    unique = sorted(unique)
    distributionValues = {}
    sortedList = []
    count = 0
    for i in range(0, len(list)):
        for j in range(0, len(list)):
            if list[i] == list[j]:
                count = count + 1
        encounter = {list[i]: count}
        dataDict.update(encounter)
        dataDict = dict(sorted(dataDict.items(), key=lambda item: item[0]))
        count = 0
    print('Encounter Times{}'.format(dataDict))
    j = 0
    for i in unique:
        j = j + dataDict[i]
        dValues = {i: j}
        distributionValues.update(dValues)
    print('Distributed Values {}'.format(distributionValues))
    for i in dataDict.keys():
        for j in range(0, dataDict[i]):
            if dataDict[i] == 0:
                break
            else:
                sortedList.append(i)
                dataDict[i] = dataDict[i] - 1
                continue
    print('Lista e sortuar me Distribution Count Sort {}'.format(sortedList))
    print("%s seconds " % (time.time() - start_time))



print('\nComparison Count Sort:\n')
comparisonCountSort(dataLists)

print('\nDistribution Count Sort:\n')
DistributinCountSort(dataLists)