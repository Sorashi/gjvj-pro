from random import random
import math

def rndint(n, s=0):
    return math.floor(random() * (n-s) + s)

def shuffle(pole):
    result = []
    while(len(pole) > 0):
        result.insert(0, pole.pop(rndint(len(pole))))
    pole.extend(result)

def swap(pole, i, j):
    pole[i], pole[j] = pole[j], pole[i]

def checkSorted(pole):
    for i in range(len(pole)-1):
        if not(pole[i] < pole[i+1]):
            return False
    return True

def bogosort(pole):
    n=0
    while not checkSorted(pole):
            shuffle(pole)
            n+=1
    if __name__ == "__main__":
        print(n)
    return pole

def bozosort(pole):
    n=0
    while not checkSorted(pole):
        swap(pole, rndint(len(pole)), rndint(len(pole)))
        n+=1
    if __name__ == "__main__":
        print(n)
    return pole

if __name__ == "__main__":
    pole = [4,5,6,78,1,2]
    print(bozosort(pole))
