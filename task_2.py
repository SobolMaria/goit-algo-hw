import random

def get_numbers_ticket(min, max, quantity):
    while True:
        try:
            min = int(min)
            if min >= 1 or min >= 1000:
                break
            else:
                print("Enter minimum >= 1")
        except ValueError:
            print("Enter a number minimum!")
            min = input("Enter minimum: ")

    while True:
        try:
            max = int(max)
            if  min <= max <= 1000:
                break
            else:
                print(f"Enter number {min} <= number <= 1000")
        except ValueError:
            print("Enter a number maximum!")
            max = input("Enter maximum: ")

    while True:
        try:
            quantity = int(quantity)
            if  max - min >= quantity:
                break
            else:
                max_qty = max - min
                print(f"Enter number <= {max_qty}")
        except ValueError:
            print("Enter a number between min and max!")
            quantity = input("Enter quantity between min and max: ")
        set_of_numbers = set()
        
    while len(set_of_numbers) < quantity:
        num = random.randint(min, max)
        set_of_numbers.add(num)

    list_of_numbers = list(set_of_numbers)
    return list_of_numbers
        



minimum = input("Enter minimum: ")
maximum = input("Enter maximum: ")
quantity = input("Enter quantity between min and max: ")
print(get_numbers_ticket(minimum, maximum, quantity))