def main():
    lyst, sortMethod = askInput()
    if sortMethod == 1:
        selSort(lyst)
    elif sortMethod == 2:
        bubbleSort(lyst)
    elif sortMethod == 3:
        optBubbleSort(lyst)
    elif sortMethod == 4:
        insSort(lyst)
    elif sortMethod == 5:
        quickSort(lyst, 0, len(lyst) - 1)

# Richiesta input
def askInput():
    lyst = []
    value = int(input("inserire numero:"))
    while value != 0:
        lyst.append(value)
        value = int(input("inserire numero:"))
    options = [1, 2, 3, 4, 5]
    sortMethod = None
    while sortMethod not in options:
        sortMethod = int(input("seleziona metodo: 1) selection sort; 2) bubble sort; 3) optimal bubble sort; 4) insertion sort; 5) quicksort: "))
    return lyst, sortMethod

# Selection sort
def selSort(lyst):
    length = len(lyst)
    i = 0
    for i in range(0, length - 1):
        minPos = i
        j = i + 1
        for j in range(i + 1, length):
            if lyst[minPos] > lyst[j]:
                minPos = j
        lyst[i], lyst[minPos] = lyst[minPos], lyst[i]
        print(lyst)

# Bubble sort
def bubbleSort(lyst):
    length = len(lyst)
    for i in range(0, length - 1):
        for j in range(0, length - 1 - i):
            if lyst[j] > lyst[j+1]:
                lyst[j], lyst[j+1] = lyst[j+1], lyst[j]
            print(lyst)

# Bubble sort ottimizzato
def optBubbleSort(lyst):
    length = len(lyst)
    i = 0
    top = length - 1
    while i < (length - 1) and top > 0:
        last = -1
        for j in range(0, top):
            if lyst[j] > lyst[j+1]:
                lyst[j], lyst[j+1] = lyst[j+1], lyst[j]
                last = j
                print(lyst)
        top = last
        i += 1

# Insertion sort
def insSort(lyst):
    length = len(lyst)
    i = 1
    for i in range(1, length):
        j = i
        while j > 0 and lyst[j] < lyst[j-1]:
            lyst[j-1], lyst[j] = lyst[j], lyst[j-1]
            print(lyst)
            j -= 1

# Quicksort
def partition(lyst, start, end):
    pIndex = start
    pivot = lyst[end]
    i = start
    for i in range(start, end):
        if lyst[i] <= pivot:
            lyst[pIndex], lyst[i] = lyst[i], lyst[pIndex]
            pIndex += 1
    lyst[pIndex], lyst[end] = lyst[end], lyst[pIndex]
    return pIndex


def quickSort(lyst, start, end):
    if start < end:
        pIndex = partition(lyst, start, end)
        print(lyst)
        quickSort(lyst, start, pIndex - 1)
        quickSort(lyst, pIndex + 1, end)


if __name__ == '__main__':
    main()