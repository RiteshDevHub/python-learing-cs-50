def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def lttr(a):
    for i in a[0 : 1]:
        if not ("A" <= i <= "Z"):
            return False
    
    return True

def char(b):
    if not (2 <= len(b) <=6):
        return False
    return True

def num_bet(c):
    for i in range(len(c)-1):
        if "1" <= c[i] <= "9":
            if "A" <= c[i+1] <= "Z":
                return False

        else:
            continue
    return True
        
def pun(d):
    punctuations = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    for j in range(len(d)):
        for pun in punctuations:
                if d[j] == pun:
                    return False
        
        if d[j] == "." or " ":
            return False
    return True

def is_valid(s):
    if not lttr(s):
        return False
    
    elif not char(s):
        return False
    
    elif not num_bet(s):
        return False
    
    elif not pun(s):
        return False
    
    else:
        return True

main()