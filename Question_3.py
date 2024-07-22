## Question 3: Nested Loops
    # Write a Python program that prints the following pattern using nested loops.

    # For n=5, the pattern should look like this:
#    1
#    22
#    333
#    4444
#    55555

def print_pattern(n):
    for x in range(1, n+1):
        for y in range(x):
            print(x, end='')
        print()
n = 5

print_pattern(n)