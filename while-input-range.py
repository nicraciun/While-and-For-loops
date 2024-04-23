
start_n  = int(input("Start: "))
end_n= int(input("End: "))

while start_n != end_n :
    if start_n < end_n:
        print(start_n)
        start_n += 1
    else:
        print(start_n)
        start_n -= 1
    if end_n == start_n:
        print(start_n)


