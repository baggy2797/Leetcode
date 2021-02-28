c3,c5 = 0,0
res =""
for i in range(0,101):
    c3 = c3+1
    c5 = c5+1
    if c3 == 3:
        res = res + "fizz"
        c3 = 0
    if c5 == 5:
        res = res + "buzz"
        c5 = 0
    
    print(res)