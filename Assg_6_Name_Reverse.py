fullname=input("Enter full name as LastName,FirstName or END to quit: ")
while fullname != "END":
    lastname=""
    firstname=""
    i=0
    while fullname[i] != ",":
        lastname+=fullname[i]
        i+=1
    i+=1
    while i < len(fullname):
        firstname+=fullname[i]
        i+=1
    newFullname = firstname + " " + lastname
    print("The name %20s converts to %20s" % (fullname, newFullname))
    fullname=input("Enter full name as LastName,FirstName or END to quit: ")

print("program completed")


