import random

def get_numbers_ticket(min, max, quantity):
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except ValueError:
        print("Unacceptable numbers!")
        return []

    if min < 1 or max > 1000 or quantity > max - min:
        print("Unacceptable data")
        return []
    
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
