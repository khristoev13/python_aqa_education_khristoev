# Stage #1

messages = '''Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!'''

print(messages)


# Stage #2

print("Write how many cups of coffee you will need: ")
cups_of_coffee = int(input())

water_per_one_cup = 200
milk_per_one_cup = 50
beans_per_one_cup = 15

water = water_per_one_cup * cups_of_coffee
milk = milk_per_one_cup * cups_of_coffee
beans = beans_per_one_cup * cups_of_coffee

print("For %s cups of coffee you will need: " % cups_of_coffee)
print("%d ml of water " % water)
print("%d ml of milk " % milk)
print("%d g of beans " % beans)


# Stage #3

print("Write how many ml of water the coffee machine has: ")
water_ml = int(input())
print("Write how many ml of milk the coffee machine has: ")
milk_ml = int(input())
print("Write how many grams of coffee beans the coffee machine has: ")
beans_gr = int(input())

print("Write how many cups of coffee you will need: ")
needed_cups_of_coffee = int(input())

water_per_one_cup = 200
milk_per_one_cup = 50
beans_per_one_cup = 15

available_cups_of_coffee = min(water_ml // water_per_one_cup, milk_ml // milk_per_one_cup,
                               beans_gr // beans_per_one_cup)

if needed_cups_of_coffee == available_cups_of_coffee:
    print("Yes, I can make that amount of coffee")
elif needed_cups_of_coffee > available_cups_of_coffee:
    print(f"No, I can make only {available_cups_of_coffee} cups of coffee")
elif needed_cups_of_coffee < available_cups_of_coffee:
    print(f"Yes, I can make that amount of coffee "
          f"(and even {available_cups_of_coffee - needed_cups_of_coffee} more than that)")
