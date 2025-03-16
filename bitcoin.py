import requests
import sys

def main():
    num = get_bit(sys.argv)
    response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    cost = response.json()
    for data in cost["data"]:
        a = float(cost["data"]["priceUsd"])
    final_cost = round((a * num), 4)
    print(f"${final_cost}")

def get_bit(n):
    if len(n) != 2:
        sys.exit("Missing command-line argument.")
    else:
        try:
            return float(n[1])
        except ValueError:
            sys.exit("Command line argument is not a number.")

main()