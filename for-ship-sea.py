big_ship = int(input("introdu valoare: "))

if big_ship > 5:
    for x in range(1,big_ship):
        if x == int(big_ship/2)-1:
            print( "w", end="" )
        elif  x == int(big_ship/2):
            print( "W", end="" )
        elif  x == int(big_ship/2)+1:
            print( "w", end="" )
        else:
            print( "~", end="" )
else:
    print ("Eror")