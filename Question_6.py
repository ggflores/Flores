## Question 6: Prime Numbers
# Write a Python program to find and print all the prime numbers between two input values, start and end.
# Use a function named `find_primes` to accomplish this.
# A prime number is a number that has exactly two distinct positive divisors: 1 and itself.

def question_6(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(int(start), int(end)+1):
        if question_6(num):
            primes.append(num)
    return primes

start = input("Enter lower limit: ")
end = input("Enter upper limit: ")
prime_numbers = find_primes(start, end)
print(f"Prime numbers between {start} and {end}: {prime_numbers}")