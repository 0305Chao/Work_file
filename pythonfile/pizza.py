def make_pizza(size, *toppings):
    """该书要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'peperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extea cheese')
        
