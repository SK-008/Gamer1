# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food u like (q to quit): ")
    if food.lower() == "q" :
        break
    else:
        price = float(input(f"Enter the price {food}: $"))
        foods.append(food)
        prices.append(price)

print("----your food cart----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"total is : ${total}")