def five(x):
    if x % 5 == 0:
        print("Buzz")
    else:
        print(x)


def three(x):
    if x % 3 == 0:
        print("Fizz")
    else:
        five(x)


def threefive(x):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        three(x)


def fizzbuzz(x):
    numbers = list(range(x))
    for i in numbers:
        threefive(i)


fizzbuzz(101)