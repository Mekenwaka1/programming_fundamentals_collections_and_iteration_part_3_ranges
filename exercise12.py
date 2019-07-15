print("How many pizzas do you want to order")
quantity = int(input())
num = 1

for num in range(1, quantity + 1):
    print("How many toppings for pizza {}?".format(num))
    number_of_toppings = int(input())
    print("You have ordered a pizza with {} toppings.".format(number_of_toppings))
