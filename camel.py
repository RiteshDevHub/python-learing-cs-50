name = input("Type your name in camel case:")
snake_case= []

for i in range(len(name)):
    if name(i).islower():
        snake_case.append(name(i))
    else:
        snake_case.append("_")
        snake_case.append(name(i).lower())

for j in range(len(snake_case)):
    print (snake_case(j))
