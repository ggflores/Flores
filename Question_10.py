# Question 10: Recursive Functions
# Write a Python program that implements a recursive function named calculate_fibonacci to find the nth number in the Fibonacci sequence.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
# Your function should take the term n as an input and return the nth Fibonacci number.

def calc_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calc_fibonacci(n-1) + calc_fibonacci(n-2)
    
n = int(input("Enter the term number to find in the fibonacci sequence: "))
result =  calc_fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")