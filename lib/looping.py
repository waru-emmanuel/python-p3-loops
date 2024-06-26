#!/usr/bin/env python3

def happy_new_year():
    # code goes here! use while loop
    # example: 1 2 3 4 5 6 7 8 9 10 "Ha
    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # example: [1, 2, 3, 4, 5] ->
    # 1 4 9 16 25
    return [x**2 for x in int_list]


def fizzbuzz():
    # code goes here!
    # example: 1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16 17 ...
    # use for loop , if statement, print
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0: 
            print("Fizz")
        elif i % 5 == 0: 
            print("Buzz")
        else: 
            print(i)

















def reverse_string(str):
    # code goes here!
    # example: "hello" -> "olleh"
    #return str[::-1]...this the built in method

    #using for loop
    reversed_str = ""
    for char in str:
        reversed_str = char + reversed_str
    return reversed_str







    
