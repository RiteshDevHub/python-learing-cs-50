import pyfiglet
import sys

def main():
    while True:
        try:
            if len(sys.argv) == 1:
                f = pyfiglet.figlet_format(get_text("Input: "))
            elif len(sys.argv) == 3:
                if sys.argv[1] == "-f" or "--font":
                    fonts = pyfiglet.FigletFont.getFonts() # Returns a list of available fonts

                    if sys.argv[2] not in fonts:
                        sys.exit()
                    else:
                        f = pyfiglet.figlet_format(get_text("Input: "), font = sys.argv[2])
                else:
                    sys.exit()
            else:
                sys.exit()

            print(f"Output: {f}")
            break
        
        except ValueError:
            pass

def get_text(prompt):
    while True:
        try:
            return input(prompt)
        except ValueError:
            pass

main()