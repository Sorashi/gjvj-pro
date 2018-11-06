def caesar(vstup, posun):
    vysledek = ''
    posun %= 25
    # A-Z -- 65-90
    # a-z -- 97-122
    for i in range(len(vstup)):
        o = ord(vstup[i])
        if o >= 65 and o <= 90:
            o = 65 + (((o-65) + posun) % 25)
        elif o >= 97 and o <= 122:
            o = 97 + (((o-97) + posun) % 25)
        vysledek += chr(o)
    return vysledek

print(caesar('ahojz', 5))