## Question 4: Functions and Namespaces
# Write a function `multiply_by_factor` that takes a list of numbers and a `factor` with which to multiply each number. 
# The function should modify the original list and not return anything.

def question_4(numbers_list,factor):
    for x in range(len(numbers_list)):
        numbers_list[x] *= factor


numbers_list = [1, 2, 3, 4, 5]
factor = 2
question_4(numbers_list,factor)
print(numbers_list)