def swap(pole, i, j):
    pole[i], pole[j] = pole[j], pole[i]

def bubblesort(pole):
    while True:
        swaps = 0
        for i in range(len(pole) - 1):
            if pole[i] > pole[i+1]:
                swap(pole, i, i+1)
                swaps += 1
        if swaps == 0:
            break
    return pole

if __name__ == "__main__":
    print(bubblesort([3,12,1,8,2,4,89,51,1,1,2,3,4,5]))
