## Question 9: Data Filtering
# Given a list of dictionaries representing different people, write a Python program to filter out those who are not eligible to vote.
# The criteria for voting eligibility are being at least 18 years old and holding citizenship.
# Your program should include a function named filter_voters that takes the list of dictionaries and 
# returns a new list containing only the dictionaries of those who are eligible to vote.

def filter_voters(people):
    eligible_voters = []
    for person in people:
        if person.get("age", 0) >= 18 and person.get("citizenship", "").lower() == "yes":
            eligible_voters.append(person)
    return eligible_voters

people = [
    {"name": "Alice", "age": 25, "citizenship": "Yes"},
    {"name": "Bob", "age": 17, "Visa": "Yes", "Expiration": "2025-01-01"},
    {"name": "Charlie", "age": 20, "citizenship": "No"},
    {"name": "Raul", "age": 18, "citizenship": "Unknown", "state": "MI"},
    {"name": "David", "age": 30, "citizenship": "Yes", "Visa": "Yes", "Expiration": "2023-01-01"},
    {"name": "Eve", "age": 42, "state": "CA", "citizenship": "Yes", "felony_conviction": "Yes"},
]

eligible_voters = filter_voters(people)
print(eligible_voters)