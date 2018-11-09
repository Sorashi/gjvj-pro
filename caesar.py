def caesar(vstup, posun):
    vysledek = ''
    posun %= 26
    # A-Z -- 65-90
    # a-z -- 97-122
    for i in range(len(vstup)):
        o = ord(vstup[i])
        if o >= 65 and o <= 90:
            o = 65 + (((o-65) + posun) % 26)
        elif o >= 97 and o <= 122:
            o = 97 + (((o-97) + posun) % 26)
        vysledek += chr(o)
    return vysledek

print(caesar('Ahoj, svete, zzzz', 5))