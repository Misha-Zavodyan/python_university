for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s)
    if n % 2 == 0:
        s += "01"
    else:
        s += "10"
    r = int(s, 2)  # перевод в десятичную систему
    if r > 102:
        print(r)
        break