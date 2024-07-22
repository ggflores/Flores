## Question 2: Working with Dictionaries
    # Given a dictionary, `prices = {'apple': 0.40, 'banana': 0.50, 'kiwi': 1.25}`, 
    # write a Python program to convert the prices into a list of `(fruit, price)` tuples, 
    # then print the list sorted by fruit name.

def question_2(prices):
    fruit_price_list = list(prices.items())
    sorted_fruit_price_list = sorted(fruit_price_list)
    print(sorted_fruit_price_list)

prices = {'apple': 0.40, 'banana': 0.50, 'kiwi': 1.25, 'cantalope': 6.62}
question_2(prices)