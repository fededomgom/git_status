def math(number):
    square = number * number
    third = number * number * number
    print("The square of your number is {a} and to the third power is {b}.".format(a=square, b=third)


while True:
    while True:
        number = int(input("Tell me a number"))
        math(number)
