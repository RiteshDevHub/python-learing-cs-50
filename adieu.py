def main():
    names = get_names("Name: ")  
    print("Adieu, adieu, to", end = "")
    if len(names) == 1:
        print(names[0])
    else:
        print(", ".join(names[:-1]), "and", names[-1])

def get_names(prompt):
    name_list =[]
    while True:
        try:
            name = input(prompt)
            name_list.append(name)
        except EOFError:
            return name_list
        
main()