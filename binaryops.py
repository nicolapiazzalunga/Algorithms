import binarylib as bb

def main():
    byn, numbits = bb.askBinInput()
    
    # crea lista cifre binarie
    byn_2 = bb.rappbin(byn, numbits)
    # stampa numero binario
    print("Il numero binario inserito è: ", end="")
    bb.stampabin(byn_2)
    # Calcola l'inverso c2
    print("Il numero opposto c2 è: ", end="")
    oppc2 = bb.invc2(byn, numbits)
    bb.binarylib.stampabin(oppc2)
    # Calcola la rappresentazione decimale
    dec = bb.rapp10(byn, numbits)
    print(f"Il suo corrispondente b10 è: {dec}")
        

if __name__ == '__main__':
    main()