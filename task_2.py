import random

def get_numbers_ticket(min, max, quantity):
    set_of_numbers = set()
    number = 0
    while len(set_of_numbers) < quantity:
        num = random.randint(min, max)
        set_of_numbers.add(num)

    list_of_numbers = list(set_of_numbers)
    return list_of_numbers
        
while True:
    minimum = input("Enter minimum: ")
    try:
        minimum = int(minimum)
        if minimum >= 1 or minimum >= 1000:
            break
        else:
            print("Enter minimum >= 1")
    except ValueError:
        print("Enter a number!")

while True:
    maximum = input("Enter maximum: ")
    try:
        maximum = int(maximum)
        if minimum <= maximum <= 1000:
            break
        else:
            print(f"Enter number {minimum} <= number <= 1000")
    except ValueError:
        print("Enter a number!")

while True:
    quantity = input("Enter quantity between min and max: ")
    try:
        quantity = int(quantity)
        if  maximum - minimum >= quantity:
            break
        else:
            max_qty = maximum - minimum
            print(f"Enter number <= {max_qty}")
    except ValueError:
        print("Enter a number!")

print(get_numbers_ticket(minimum, maximum, quantity))

