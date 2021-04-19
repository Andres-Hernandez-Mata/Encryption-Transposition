"""
Uso: Cifrado por transposición
Creado: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 07 Abril 2020
"""

def main():
    myMessage = input('Ingresa el mensaje a cifrar: ')
    espacios = 1
    while espacios > 0:
        clave = input('Ingresa tu palabra clave para cifrar: ')
        espacios = clave.count(' ')
        if clave.isalpha() == False:
            espacios += 1
    myKey = len(clave)

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message.
    print(ciphertext + '|')


