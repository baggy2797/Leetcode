# FizzBuzz is when the number is divisible by 3 print fizz when with 5 print buzz and 
# when with both print FizzBuzz

d = ""

for i in range(1,101):
    # if i%3 == 0 and i%5 == 0:
    #     print("fizzbuzz")
    if i%3 == 0:
        d += "fizz"
    if i%5 == 0:
        d += "buzz"
    else:
        print(d or i)