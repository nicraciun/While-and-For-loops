from os import system

garden2d = [
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','v','.','v','.','.','v'],
]

action = 0 

print()
while action !=3:
    system ("cls")
    count = 0
    plants =0
    for ri in range(len(garden2d)):
        for pi in range(len(garden2d[ri])):
            plants +=len(garden2d[ri][pi])
            if garden2d[ri][pi] =="v":
                count +=1
            print (garden2d[ri][pi], ' ', end="")
        print()
     
    plants = count*100/plants
    print()
    print(f"Fruit:{plants:3.0f}%")
    print ("ACTION:\n1. watering\n2. collect\n3. exit")
    action = int(input("> "))
    if action  == 1:
        idx = int(input("Where: "))
        for ir in reversed(range(len(garden2d))):
            if garden2d[ir][idx] == '.':
                garden2d[ir][idx] = 'v' 
                break
    elif action  == 2:
        idx = int(input("Where: "))
        for ir in range(len(garden2d)):
            if garden2d[ir][idx] == 'v':
                garden2d[ir][idx] = '.' 
                break
print()    
