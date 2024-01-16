import binarylib as bb

def main():
    # richiede input di due numeri binari
    numbits = int(input("Inserire numero di bit: "))
    byn1 = bb.askBinInput(numbits)
    byn2 = bb.askBinInput(numbits)
    
    # crea lista cifre binarie
    byn1_2 = bb.rappbin(byn1, numbits)
    byn2_2 = bb.rappbin(byn2, numbits)

    # somma i due numeri
    bynsum_2 = []
    # controlla se qualcuno è negativo (temp: esegui solo positivi)
    if byn1_2[0] == 0 and byn2_2[0] == 0:
        cin = 0
        for i in range(0, numbits - 1):
            bit1 = byn1_2[numbits - i - 1]
            bit2 = byn2_2[numbits - i - 1]
            sum, cin = bb.fulladder(bit1, bit2, cin)
            bynsum_2.insert(0, sum)
        bynsum_2.insert(0, 0)
    if cin != 0:
        print("OVERFLOW")   
    else:
        print("La somma dei due numeri b2 è: ", end="")
        bb.stampabin(bynsum_2)


    # # stampa numero binario
    # print("Il numero binario inserito è: ", end="")
    # bb.stampabin(byn_2)
    # Calcola l'opposto c2
    print("Il numero opposto c2 è: ", end="")
    oppc2 = bb.oppc2(byn1, numbits)
    # # Calcola la rappresentazione decimale
    # dec = bb.rapp10(byn, numbits)
    # print(f"Il suo corrispondente b10 è: {dec}")
        

if __name__ == '__main__':
    main()