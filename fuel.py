def main():
    frac = get_frac("Fraction: ")
    perc = int(round((frac[0]/frac[1])*100))

    if perc < 1:
        print("E")
    elif perc > 99:
        print("F")
    else:
        print(f"{perc}%")

def get_frac(prompt):
    while True:
        try:
            x = input(prompt)
            num , den = map(int, x.split("/"))
            
            if den == 0:
                raise ZeroDivisionError
            if num > den:
                raise KeyError
            
            return (num , den)

        except (ValueError, ZeroDivisionError, KeyError):
            pass

main()