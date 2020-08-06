def fizzbuzz(i):
    if i%3 == 0 and i%5 != 0:
        return "fizz"
    elif i%3 != 0 and i%5 == 0:
        return "buzz"
    elif i%3 == 0 and i%5 == 0:
        return "fizzbuzz"
    else:
        return i

num = int(input("Enter a number: "))
print(fizzbuzz(num))
