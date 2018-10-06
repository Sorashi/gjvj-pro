def insertionsort(pole):
    result = [] # pole, kam budeme průběžně vkládat prvky na správné místo (insert -- proto insertion sort)
    while len(pole) > 0:
        prvek = pole.pop() # odstraní první prvek pole a zároveň jeho hodnotu uloží do proměnné prvek
        j = 0 # index, kam budeme vkládat prvek do pole result
        for i in range(len(result)):
            if i == 0 and len(result) >= 1 and prvek <= result[0]:
                # prvek je menší než první prvek v result, a proto ho vložíme na začátek result
                j = 0
                break
            elif i < len(result) - 1 and result[i] <= prvek and prvek <= result[i+1]:
                # našli jsme index v poli result, kde element na tomto indexu je menší než prvek a zároveň element na indexu i + 1 je větší než prvek
                # jinak řečeno, našli jsme místo, kam prvek musíme vložit
                j = i + 1 # Místo, kam vkládáme prvek je mezi i a i + 1. Budeme proto vkládat na index i + 1. Např. chceme vložit mezi indexy 0 a 1, vkládáme na index 1
                break
            elif i == len(result) - 1:
                # jsme na konci pole result, a zatím jsme nenašli pozici, takže je jasné, že patří na konec
                # např. vkládáme do result = [1,2,3] prvek 4
                j = i + 1
                break
        result.insert(j, prvek) # vložíme prvek do pole result na index j
        if __name__ == "__main__":
            print("vlozen prvek " + str(prvek) + " na index " + str(j))
    return result

if __name__ == "__main__":
    print(insertionsort([12,14,11,4,7,2,3,15,8,9,1,10,6,5,13]))