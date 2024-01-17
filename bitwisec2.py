import sys

def main():
    byn1 = 750
    byn2 = -48

    adder(byn1, byn2)

# if byn<0, returns a two's complement emulation of size numbits
def preprocess(byn):
    if byn < 0:
        mask = (1 << sys.getsizeof(byn)) - 1
        byn = ((~byn + 1) ^ mask) + 1
    return byn

# convert output into decimal
def b10out(byn):
    dec = 0
    sign = 1
    numbits = sys.getsizeof(byn)
    # if negative, inverti segno
    if byn & (1 << (numbits - 1)):
        byn = ~byn + 1
        sign = -1
    for i in range(numbits - 1):
        dec += byn & (1 << i)
    return sign * dec

# performs addition of emulated complement of two binary numbers 
def adder(byn1, byn2):
    inputcarry = 0
    output = 0

    maxnumbits = max(sys.getsizeof(byn1), sys.getsizeof(byn2))
    minnumbits = min(sys.getsizeof(byn1), sys.getsizeof(byn2))

    if maxnumbits == minnumbits:
        inputmask = 1
        numbits = minnumbits
        check = byn1 + byn2
        byn1 = preprocess(byn1)
        byn2 = preprocess(byn2)
        print(bin(byn1)[2:].zfill(numbits), bin(byn2)[2:].zfill(numbits))
        for bitcount in range(numbits):
            bitvalue1 = byn1 & inputmask
            bitvalue2 = byn2 & inputmask
            inputmask <<= 1
            print("-----------")
            print(f"Bitcount:     {bitcount}")
            print(f"Bitvalue1:    {bin(bitvalue1)[2:].zfill(numbits)}")
            print(f"Bitvalue2:    {bin(bitvalue2)[2:].zfill(numbits)}")
            print(f"Input carry:  {bin(inputcarry)[2:].zfill(numbits)}")
            halfadder = bitvalue1 ^ bitvalue2
            fulladder = inputcarry ^ halfadder
            output ^= fulladder
            halfcarry1 = bitvalue1 & bitvalue2
            halfcarry2 = inputcarry & halfadder
            outputcarry = (halfcarry1 | halfcarry2) << 1
            inputcarry = outputcarry
            print(f"Half adder:   {bin(halfadder)[2:].zfill(numbits)}")
            print(f"Full adder:   {bin(fulladder)[2:].zfill(numbits)}")
            print(f"Output:       {bin(output)[2:].zfill(numbits)}")
            print(f"Half carry 1: {bin(halfcarry1)[2:].zfill(numbits)}")
            print(f"Half carry 2: {bin(halfcarry2)[2:].zfill(numbits)}")
            print(f"Output carry: {bin(outputcarry)[2:].zfill(numbits)}")
        outputmask = (1 << (numbits - 1))
        msb1 = byn1 & outputmask
        msb2 = byn2 & outputmask
        msb_output = output & outputmask
        overflow = outputcarry >> 1
        if (msb1 & msb2) != (msb_output & overflow):
            print("===============")
            print("NON RAPPRESENTABILE")
            print("===============")
        else:
            print("===============")
            print(f"Final Output:     {bin(output)[2:].zfill(numbits)}")
            print(f"MSB:              {bin(msb_output)[2:].zfill(numbits)}")
            print(f"Overflow:         {bin(overflow<<1)[2:].zfill(numbits)}")
            print(f"Dec Output:       {b10out(output)}")
            print(f"Dec Check:        {check}")
    else:
        print("------------")
        print("OVERFLOW")
        print("------------")

if __name__ == '__main__':
    main()
