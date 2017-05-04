from random import randint

def displayList(PList):
    for i in range(0,10):
        print(PList[i])
    print(" ")

def loadList(PList):
    for i in range(1,11):
        PList.append(randint(1,10))

def sortList(PList,PDirection):
    sorted=False
    cmp=0
    swap=0
    i=9
    while not sorted and i > 0:
        sorted=True
        for j in range(0,i): #Passes
            cmp+=1
            need2Swap=False
            if (PList[j] > PList[j+1]) and (PDirection=="A"):
                #Need to Swap
                need2Swap=True
            if (PList[j] < PList[j+1] and (PDirection=="D")):
                need2Swap=True
            if need2Swap:
                sorted=False
                swap+=1
                (PList[j],PList[j+1]) = (PList[j+1],PList[j])
        i-=1
    print("%10d Comparison      %10d Swaps"%(cmp,swap))
                    


# main code section
def main():
    myList=[]  #OR ["Ben","Jerry","Bill","Jim","Bob","Jeff","Susan","Britt","Marge","Tom"]Looks at first string character during each pass. Compares the string value and orders them. Result is alphabetical order.
    loadList(myList)
    displayList(myList)
    sortList(myList,"A")
    displayList(myList)
    sortList(myList,"D")
    displayList(myList)

main()
