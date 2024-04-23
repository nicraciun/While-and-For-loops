from os import system
friends=["James", "Robert","John"]
option=""
while option != "x":
    #system("cls")
    newf = input("Add a new friend: ")
    friends.append(newf)
    print ("Number of friends:",len(friends))
    option =input("Exit enter 'x' continue any key: ")