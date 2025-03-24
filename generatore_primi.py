import random

def inserisci_valori():
    while True:
        try:
            bits_str = input("Enter the number of bits for the prime number n: ")
            bits = int(bits_str)

            break
        except ValueError:
            print("You must enter an integer!")

    return bits
def esponenziazione_veloce(a, e, n):
    d = 1

    # trasformo l'esponenete in binario (è una stringa)
    e_bin = bin(e)[2:]

    for bit in e_bin:
        d = (d * d) % n

        if bit == '1':
            d = (d * a) % n

    return d
def miller_rabin(n, x):

    # definisco n-1 come 2^r * m con m dispari
    m = n - 1
    r = 0
    while m % 2 == 0:
        m //= 2
        r += 1

    # calcolo x^m % n  con l'algoritmo di esponenziazione veloce (lo stesso definito per il punto precedente dell'esercizio)
    x = esponenziazione_veloce(x, m, n)

    # se x^m % n == 1 restituisco falso (probabilmente non è composto)
    if x == 1:
        return False

    # controllo se x0 = -1
    if x == n-1:
        return False


    for _ in range(r - 1):
        x = (x * x) % n
        if x == n - 1:
            return False

    return True

def genera_primo(bits):
    # itero fin quando il test non restituisce False
    while True:
        # genero un numero dispari fissato il numero di bit
        n = random.getrandbits(bits) | 1
        is_primo = True

        # applico il Test di Miller-Rabin 5 volte per essere sicuro che sia primo
        for _ in range(5):
            # passo come x un valore random tra 2 e n-2.
            if miller_rabin(n, random.randint(2, n - 2)):
                # se il test restituisce True allor n non è primo
                is_primo = False
                break
        # se n è primo lo restituisco in output
        if is_primo:
            return n


if __name__ == '__main__':
    # genera un numero primo di n bit
    bits = inserisci_valori()
    n = genera_primo(bits)
    print(n)