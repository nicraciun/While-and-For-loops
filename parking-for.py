PARKING_PLACES = 7
FREE_PLACE = 3

print("#"*PARKING_PLACES*5)

for place_index in range(1, PARKING_PLACES + 1):
    if place_index == 3:
       print("|  |", end="") 
    else:    
       print("| X |", end="")

print("\n","#"*PARKING_PLACES*5, sep="")

# sep() este un parametru al funcției print() care permite formatarea elementelor cu separare atunci când sunt tipărite sau concatenate. 