def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    cost = get_order("Item: ", menu)
    print (f"Total: ${cost: .2f}")

def get_order(prompt , items):
    cost = 0
    while True:
        try:
            dish = input(prompt)
            for item in items:
                if item == dish:
                    cost = cost + items[item]
                    print (f"Total: ${cost: .2f}")

        except EOFError:
            return cost
        
main()