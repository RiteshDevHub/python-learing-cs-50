def main():
    coke = 50

    while coke > 0:
        coin = int(input("Enter coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            coke = coke - coin
        else:
            pass
        if coke >= 0:
             print ("Amount deu:", coke)
        else:
             pass

    if coke == 0:
            print ("Here is your coke")

    else:
        print("Here is your coke")
        print("Change:", coke - (2 * coke))

main()
