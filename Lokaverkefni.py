import random
import time

def BubbleSort(listi):
    start = time.time()
    l = listi.copy()
    n = len(l)-1
    allSet = False
    while allSet == False:
        allSet = True
        for x in range(n):
            if l[x] > l[x+1]:
                temp = l[x]
                l[x] = l[x+1]
                l[x+1] = temp
                allSet = False
        n-=1
    t = time.time()-start
    return [l,t]

def QuickSort(listi,low,high):
    l = listi
    def partition(l, low, high):
        i = low-1
        pivot = l[high]

        for x in range(low,high):
            if l[x] <= pivot:
                i += 1
                temp = l[x]
                l[x] = l[i]
                l[i] = temp

        temp2 = l[high]
        l[high] = l[i+1]
        l[i+1] = temp2
        return i+1
    
    if len(l) <= 1:
        return l
    elif low < high:
        pi = partition(l,low,high)
        QuickSort(l,low,pi-1)
        QuickSort(l,pi+1,high)
        
def SelectionSort(listi):
    start = time.time()
    l = listi.copy()
    maxIndex = 0
    n = len(l)
    while n >1:
        for x in range(n):
            if l[x] > l[maxIndex]:
                maxIndex = x
        temp = l[n-1] 
        l[n-1] = l[maxIndex]
        l[maxIndex] = temp
        maxIndex = 0
        n-=1
    t = time.time()-start
    return [l,t]

def InsertionSort(listi):
    start = time.time()
    l = listi.copy()
    n = len(l)
    for x in range(n):
        if x >0:
            y = x
            while l[y-1] > l[y]:
                temp = l[y]
                l[y] = l[y-1]
                l[y-1] = temp
                y -= 1
                if y == 0:
                    break
    t = time.time()-start
    return [l,t]



lengd = int(input("Hversu langan lista villtu raða?  (t.d. 3: [1,2,3])"))
#maxTala = int(input("Hversu háar tölur viltu fá?       (t.d. 500: [499,100,320,...]"))
maxTala = lengd *2
OriginalListinn = []
for x in range(lengd):
    OriginalListinn.append(random.randint(0,maxTala))



print("") #----------------------------------------------------Bubble----------------------------
b = BubbleSort(OriginalListinn)
print("BubbleSort Time: ",b[1], "sec")

 
#----------------------------------------------------Quick----------------------------

n = len(OriginalListinn)
qList = OriginalListinn.copy()
qStart = time.time()#Þarf að tímasetja fallið fyrir utan fallið því það er endurkvæmt
q = QuickSort(qList,0,n-1)
qt = time.time() - qStart #Annars myndi það ekki stoppa tíman þegar listinn er tilbúinn
print("QuickSort Time: ",qt, " sec")


#----------------------------------------------------Selection----------------------------
s = SelectionSort(OriginalListinn)
print("SelectionSort Time: ", s[1], "sec")

#----------------------------------------------------insertion----------------------------
i = InsertionSort(OriginalListinn)
print("InsertionSort Time: ", i[1], "sec")

#----------------------------------------------------Sort----------------------------
SortListi = OriginalListinn.copy()
sStart = time.time()
SortListi.sort()
sT = time.time() - sStart
print("Innbyggt Sorting Fall: ", sT)

print("")
enter = input("Ýttu á ENTER til þess að sjá röðuðu listana. (Ekki er mælt með að halda áfram ef listarnir eru Risa stórir)")
print("")
print("Original: ",OriginalListinn)
print("")
print("BubbleSort: ", b[0])
print("")
print("QuickSort: ", qList)
print("")
print("SelectionSort: ", s[0])
print("")
print("InsertionSort: ", i[0])
print("")
print("Innbyggt Sort Fall: ", SortListi, " sec")
print("")
