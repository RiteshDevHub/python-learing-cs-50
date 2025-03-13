poster = {"Apple":"52", "Banana":"89", "Orange":"47", "Strawberry":"32", "Mango":"60", "Grapes":"32", "Pineapple":"60"}

fruit = input("Enter name of fruit: ")

for post in poster:
    if fruit == post:
        print ("Calories:", poster[post])
    else:
        continue