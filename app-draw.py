from turtle import *
import turtle

forward(0)

while True:
    d = input('Directiona (w,d,a,s, color-c ) > ')
    if d == '-':
        break
    if d == 'w':
        forward(10)
    elif d == 'd':
        right(90)
    elif d == 'a':
        left(90)        
    elif d == 's':
        left(180)
    elif d =='c':
        cursor_color = input("'red', 'blue', 'green', 'black' > ") 
        color(cursor_color)        
print("Thank you for using turtle")  