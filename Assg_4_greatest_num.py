numbers = input("Enterthree numbers(1,2,3) or END to quit ")
while numbers != "END":
    i=0
    numb1 = ""
    numb2 = ""
    numb3 = ""
    while numbers[i] != ",":
        numb1 += numbers[i]
        i+=1
    numb1 = int(numb1)
    i+=1
    while numbers[i] != ",":
        numb2 += numbers[i]
        i+=1
    numb2 = int(numb2)
    i+=1
    while i < len(numbers):
        numb3 += numbers[i]
        i+=1
    numb3 = int(numb3)
    myList = [numb1,numb2,numb3]
    myList.sort()
    print("Highest %2d Middle %2d Lowest %2d" % (myList[2],myList[1],myList[0]))
    numbers = input("Enterthree numbers(1,2,3) or END to quit ")
