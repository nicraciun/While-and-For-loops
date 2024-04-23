from data import order
from os import system
from datetime import datetime

system('cls')

# CALCULS
cost = {"amount": 0,
        "currency": "MDL"
}
placed = datetime.strptime(order["placed_on"], '%Y-%m-%d %H:%M:%S')
completed = datetime.strptime(order["completed_on"], '%Y-%m-%d %H:%M:%S')

print("="*30)
print("PAYMENT ORDER")
print ("date:", placed.strftime('%d.%m.%Y'))
print ("placed on:", placed.strftime('%H:%M'))
print ("completed on:", completed.strftime('%H:%M'),"\n")

for i in range(len(order["items"])):
    n=i+1
    print (f"{n}.",order["items"][i]["name"],":",order["items"][i]["quantity"],"*",order["items"][i]["price"]["amount"],"=", order["items"][i]["price"]["amount"] * order["items"][i]["quantity"]) 
    cost["amount"] += order["items"][i]["price"]["amount"] * order["items"][i]["quantity"]
    
print ("TOTAL"+":",cost["amount"],cost["currency"])
print("="*30)
