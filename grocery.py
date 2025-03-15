def main():
    list = get_item("Item: ")
    for item in list:
        print (f"{list[item]} {item}")

def get_item(prompt):
    items = {}
    while True:
        try:
            item = input(prompt).strip().capitalize()
            if item in items:
                items[item] += 1
            else :
                items[item] = 1
        
        except EOFError:
            return dict(sorted(items.items()))

main()