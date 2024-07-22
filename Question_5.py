## Question 5: Error Handling
# Write a Python program that includes a function divide_numbers which takes two parameters, numerator and denominator.
# This function should attempt to divide the numerator by the denominator and return the result.
# However, if the denominator is zero, the function should return -1.

def question_5(numerator, denominator):
    if denominator == 0:
        return -1
    else:
        return numerator/denominator
    

numerator = int(input("Enter the numerator integer: "))
denominator = int(input("Enter the denominator integer: "))
print(question_5(numerator, denominator))