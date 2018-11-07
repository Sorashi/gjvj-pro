def caesar(vstup, posun):
    vysledek = ''
    posun %= 26
    # A-Z -- 65-90
    # a-z -- 97-122
    for i in range(len(vstup)):
        o = ord(vstup[i])
        if o >= 65 and o <= 90:
            o = 65 + (o - 65 + posun) % 26
        elif o >= 97 and o <= 122:
            o = 97 + (o - 97 + posun) % 26
        vysledek += chr(o)
    return vysledek

if __name__ == "__main__":
    assert caesar((
        # vstupní řetězec, posun o 7 znaků
        'If he had anything confidential to say, he wrote it in ' +
        'cipher, that is, by so changing the order of the letters of the ' +
        'alphabet, that not a word could be made out.'), 7) == (
        # očekávaný výsledek:
        'Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu ' +
        'jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol ' +
        'hswohila, aoha uva h dvyk jvbsk il thkl vba.')