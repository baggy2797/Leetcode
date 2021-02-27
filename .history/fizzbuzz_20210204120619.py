# FizzBuzz is when the number is divisible by 3 print fizz when with 5 print buzz and 
# when with both print FizzBuzz

for i in range(1,101):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz")
    elif i%3 == 0:
        print("fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)