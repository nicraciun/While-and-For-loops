from os import system

garden = ['.','.','v','.','.','.','v','.','v','.','.']
system ("cls")
print()

action = 0 
count = 0
system ("cls")
while action != 3:
    
    for pi in range(len(garden)):
        print (garden[pi], end="")
        if garden[pi] =="v":
            count +=1

    plants = count*100/len(garden)
    print()
    print(f"plants:{plants:3.0f}%")
    print ("\nACTION:\n1. Plant\n2. gather\n3. exit")
    action = int(input("> "))

    if action  == 1:
        idx = int(input("Where: "))
        if garden [idx] == ".":
            garden [idx] = 'v'
        else:
            print ("Plant exists !")
    elif action  == 2:
        idx = int(input("Where: "))
        if garden [idx] == "v":
            garden [idx] = '.'
        else:
            print ("The plant doesn't exist !")
    count = 0
    
print()
