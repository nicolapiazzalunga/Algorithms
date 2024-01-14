# Input di numero binario
def askBinInput():
    numbits = int(input("Inserire numero di bit: "))
    byn = int(input("Inserire numero binario: "), 2)
    if byn >= 2**numbits:
        print("OVERFLOW")
    else:
        return byn, numbits

# Crea lista ordinata che rappresenta numero binario
def rappbin(byn, numbits):
    byn_2 = []
    while byn > 0:
        byn_2.insert(0, byn%2)
        byn = byn // 2
    # filler bits
    for i in range(numbits - len(byn_2)):
        byn_2.insert(0, 0)
    return byn_2

# Stampa la lista che rappresenta il numero binario
def stampabin(byn_2):
    for i in range(len(byn_2)):
        print(byn_2[i], end="")
    print()

# Calcola inverso c2
def invc2(byn, numbits):
    oppc2 = []
    byn_2 = rappbin(byn, numbits)
    # controllo overflow semantico
    count = 0
    for i in range(1, numbits):
        if byn_2[i] != 0:
            count += 1
    if count == 0 and byn_2[0] == 1:
        print("non rappresentabile")
    # se passa controllo, inverti
    else:
        control = 0
        i = numbits - 1
        while i > 0 and not control:
            if byn_2[i] == 1:
                control = 1
                oppc2.insert(0, 1)
            else:
                i -= 1
                oppc2.insert(0, 0)
        for j in range(i - 1, -1, -1):
            oppc2.insert(0, int(not byn_2[j]))
    return oppc2

# Crea rappresentazione decimale
def rapp10(byn, numbits):
    dec = 0
    sign = 1
    byn_2 = rappbin(byn, numbits)
    if byn_2[0] != 0:
        byn_2 = invc2(byn, numbits)
        sign = -1
    for i in range(1, numbits):
        dec += byn_2[i] * (2**(numbits - i - 1))
    return sign * dec