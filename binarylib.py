import sys

# Input di numero binario
def askBinInput(numbits):
    byn = int(input("Inserire numero binario: "), 2)
    if byn >= 2**numbits:
        print("OVERFLOW")
    else:
        return byn

# Crea lista ordinata che rappresenta numero binario
def rappbin(byn, numbits):
    byn_2 = []
    # consuma byn
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

# Calcola opposto c2
def oppc2(byn, numbits):
    oppc2 = []
    byn_2 = rappbin(byn, numbits)
    # controllo overflow semantico
    count = 0
    for i in range(1, numbits):
        if byn_2[i] != 0:
            count += 1
    if count == 0 and byn_2[0] == 1:
        print("non rappresentabile")
    # se passa controllo
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

# opposto c2 con masking
def oppc2ms(byn):
    control = 0
    threshold = 0
    mask = 1
    numbits = sys.getsizeof(byn)
    while (control == 0) and (threshold < numbits):
        # if one is found
        if byn & mask:
            # set exit condition
            control = 1
            # flip the bits
            for i in range(numbits - threshold - 1):
                mask <<= -(~i)
                byn = byn ^ mask
            # add one
            byn = -(~byn)
        # if zero is found continue scanning
        else:
            mask <<= 1
            threshold = -(~threshold) # bitwise increment
    return byn

# opposto c2 con bitwise
def oppc2bw(byn):
    byn = ~byn
    byn = -(~byn)
    return byn


# Crea rappresentazione decimale
def rapp10(byn, numbits):
    dec = 0
    sign = 1
    byn_2 = rappbin(byn, numbits)
    # se negativo calcola modulo e imposta segno
    if byn_2[0] != 0:
        byn_2 = oppc2(byn, numbits)
        sign = -1
    # conversione
    for i in range(1, numbits):
        dec += byn_2[i] * (2**(numbits - i - 1))
    return sign * dec

# half-adder
def halfadder(bit1, bit2):
    sum = int(bit1 ^ bit2)
    carry = int(bit1 & bit2)
    return sum, carry

# full-adder
def fulladder(byn1, byn2, cin):
    halfsum, cout1 = halfadder(byn1, byn2)
    fullsum, cout2 = halfadder(halfsum, cin)
    cout = int(cout1 | cout2)
    return fullsum, cout

# somma due int con bitwise
def intsumbw(byn1, byn2):
    length = sys.getsizeof()
    pass