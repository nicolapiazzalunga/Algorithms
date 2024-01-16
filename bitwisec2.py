import sys
byn1 = 15785555
byn2 = 325
inputcarry = 0
output = 0
mask = 1

maxnumbits = max(sys.getsizeof(byn1), sys.getsizeof(byn2))
minnumbits = min(sys.getsizeof(byn1), sys.getsizeof(byn2))

if maxnumbits == minnumbits:
    numbits = minnumbits
    print(bin(byn1)[2:].zfill(numbits), bin(byn2)[2:].zfill(numbits))
    for bitcount in range(numbits):
        bitvalue1 = byn1 & (mask << bitcount)
        bitvalue2 = byn2 & (mask << bitcount)
        print("-----------")
        print(f"Bitcount: {bitcount}")
        print(f"Bitvalue1: {bin(bitvalue1)[2:].zfill(numbits)}")
        print(f"Bitvalue2: {bin(bitvalue2)[2:].zfill(numbits)}")
        print(f"Input carry: {bin(inputcarry)[2:].zfill(numbits)}")
        halfadder = bitvalue1 ^ bitvalue2
        fulladder = inputcarry ^ halfadder
        output = output ^ fulladder
        halfcarry1 = bitvalue1 & bitvalue2
        halfcarry2 = inputcarry & halfadder
        outputcarry = (halfcarry1 | halfcarry2) << 1
        inputcarry = outputcarry
        print(f"Half adder: {bin(halfadder)[2:].zfill(numbits)}")
        print(f"Full adder: {bin(fulladder)[2:].zfill(numbits)}")
        print(f"Output: {bin(output).zfill(numbits)}")
        print(f"Half carry 1: {bin(halfcarry1)[2:].zfill(numbits)}")
        print(f"Half carry 2: {bin(halfcarry2)[2:].zfill(numbits)}")
        print(f"Output carry: {bin(outputcarry)[2:].zfill(numbits)}")
    print("===============")
    print(f"Final Output {output}")
    print(f"Check: {byn1 + byn2}")
else:
    print("------------")
    print("OVERFLOW")
    print("------------")