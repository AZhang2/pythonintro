def pizzashop():
    name = input("what is your name?: ")
    print("please answer the following with numbers only:")
    pizzas = input("How many pizzas would you like? ")
    pepperonis = input("How many pepperonis do you want? ")
    olives = input("How many olives do you want? ")
    print(str(name) + " ordered " + str(pizzas) + " pizzas with " + str(pepperonis) + " pepperonis and " + str(olives) + " olives.")

pizzashop()