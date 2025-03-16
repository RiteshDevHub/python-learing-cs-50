import random

def main():
    level = get_level("Level: ")
    problems = generate_integer(level)
    solve(problems)

def get_level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if 1 <= n <= 3:
                return n
            else:
                raise ValueError
        except ValueError:
            pass

def generate_integer(level):
    prob = {}
    if level == 1:
        for _ in range(10):
            x = random.randint(0,9)
            y = random.randint(0,9)
            prob[f"{x} + {y} ="] = x + y
        return prob
    elif level == 2:
        for _ in range(10):
            x = random.randint(10,99)
            y = random.randint(10,99)
            prob[f"{x} + {y} ="] = x + y
        return prob
    else:
        for _ in range(10):
            x = random.randint(100,999)
            y = random.randint(100,999)
            prob[f"{x} + {y} ="] = x + y
        return prob

def solve(que):
    correct_ans = 0
    for q in que:
        re_try = 0
        while True:
            try:
                print(q, end = "")
                ans = int(input(""))
                if ans == que[q]:
                    correct_ans += 1
                    break
                else:
                    print ("EEE")
                    re_try += 1
                    raise KeyError
            except KeyError:
                if re_try == 3:
                    print(q, que[q])
                    re_try = 0
                    break
                pass

    print("Score:", correct_ans)
    return

if __name__ == "__main__":
    main()
