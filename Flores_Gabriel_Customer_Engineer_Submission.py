def question_1():
    divisBy2_3 = []
    for num in range(x,y):
        if num % 2 == 0 or num % 3 == 0:
            divisBy2_3.append(num)
    return divisBy2_3
x = int(input("Please enter the lower limit of the range: "))
y = int(input("Please enter the upper limit of the range: "))
print(question_1())
