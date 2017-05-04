from random import randint

def displayList(PList):
    for i in range(0,99):
        print("%5d" %(PList[i]),end='')
    print(" ")

def loadList(PList):
    for i in range (1,100):
        PList.append(randint(1,100))

def seqSrch(PList,Pnum):
    i=0
    while i < 99 and PList[i] != Pnum:
        i+=1
    if i < 99 and PList[i] == Pnum:
        print("%5d FOUND. It took %5d accesses."%(Pnum,i))
    else: 
        print("%5d NOT FOUND. It took %5d accesses."%(Pnum,i))

def binSrch(PList,Pnum):
    top=99
    bott=0
    mid=(top+bott) // 2
    cnt=0
    while top > bott and PList [mid] != Pnum:
        cnt+=1
        if Pnum > PList[mid]:
            bott=mid + 1
        else:
            top=mid - 1
        mid=(top+bott) // 2
    if PList[mid] == Pnum:
        print("%5d FOUND. It took %5d accesses."%(Pnum,cnt))
    else:
        print("%5d NOT FOUND. It took %5d accesses."%(Pnum,cnt))        
        
def main():
    myList=[]
    loadList(myList)
    myList.sort()
    displayList(myList)
    for i in range(1,10):
        num=randint(1,100)
        seqSrch(myList,num)
        binSrch(myList,num)
    

main()
