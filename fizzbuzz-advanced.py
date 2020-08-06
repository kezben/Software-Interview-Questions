def fizzbuzz(i):
    return ("fizz"*(i%3==0)+"buzz"*(i%5==0) or str(i))

num = int(input("Enter a number: "))
print(fizzbuzz(num))
