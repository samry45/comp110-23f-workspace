"""Instantiating a Class!"""

# This is where we instantiate the class we defined. 
# In other words, we are creating objects that belong 
# to that class.

# import the class from <file_name>.<module_name>
from lessons.classes.pizza import Pizza


my_pizza: Pizza = Pizza("large", 10, True) # <- called a Constructor
# access/update attribute values using period notation
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True
my_pizza.toppings += 2
print("My Pizza: ")
print(f"Size: {my_pizza.size}")
print(f"Toppings: {my_pizza.toppings}")
print(f"Gluten Free: {my_pizza.gluten_free}")

sals_pizza: Pizza = Pizza("medium", 5, False)
print("Sal's Pizza: ")
print(f"Size: {sals_pizza.size}")
print(f"Toppings: {sals_pizza.toppings}")
print(f"Gluten Free: {sals_pizza.gluten_free}")

def price(input_pizza: Pizza) -> float:
    """Function to compute price of a pizza."""
    if input_pizza.size == "large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += 0.75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

# Calling function
print(price(my_pizza))
print(price(sals_pizza))

# Calling method
print(my_pizza.price())
print(sals_pizza.price())

my_pizza.add_toppings(3)
print(my_pizza.price())

my_second_pizza: Pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)