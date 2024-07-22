## Question 1: List Comprehension
# Write a Python program that uses list comprehension to find all numbers between 1 and 20 that are divisible by 2 or 3.

def question_1():
    divisBy2_3 = []
    for num in range(x,y):
        if num % 2 == 0 or num % 3 == 0:
            divisBy2_3.append(num)
    return divisBy2_3
x = int(input("Please enter the lower limit of the range: "))
y = int(input("Please enter the upper limit of the range: "))
print(question_1())