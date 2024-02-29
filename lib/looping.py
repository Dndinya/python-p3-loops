#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")
    pass

def square_integers(int_list):
    return [x ** 2 for x in int_list]
    # code goes here!
    # squared_list = []
    # for x in int_list:
    #     squared_list.append(x ** 2)
    #     return squared_list
    # pass


def fizzbuzz():
    # code goes here!
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
          print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
            
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass
