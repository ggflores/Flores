## Question 7: String Manipulation
# Given a string, write a Python program to check if it is a palindrome.
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward 
# (ignoring spaces, punctuation, and capitalization).
# Your program should include a function named `is_palindrome` that takes a string as an input and 
# returns `True` if it's a palindrome and `False` otherwise.

def is_Palindrome(input_string):
    return input_string == input_string[::-1]

input_string = input("Enter any single word string: ")
correct = is_Palindrome(input_string)

if correct:
    print("Yes")
else:
    print("No")