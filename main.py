import string
from caesar import *

print("Welcome in Ciphers For Fun 0.1 ! ")

while True :

    while True :
        print("Available ciphers :")
        print("1 : Caesar Cipher")
        print("2 : Atbash Cipher")
        print("3 : Affine Cipher")
        print("4 : Vigenere Cipher")

        selectedCipher = input("The number affiliate to the cipher you want to use : ")
        if selectedCipher.isdigit() == False:
            print("You must enter the number affiliate to the cipher you want to use\n")
        elif int(selectedCipher) < 1 or int(selectedCipher) > 4 :
            print("You must enter the number affiliate to the cipher you want to use\n")
        else :
            break

    while True :
        selectedMethod = input("1 for encryption, 2 for decryption : ")

        if selectedMethod.isdigit() == False:
            print("\nou must enter 1 for encryption or 2 for decryption")
        elif int(selectedMethod) > 2 or int(selectedMethod) < 1:
            print("\nYou must enter 1 for encryption or 2 for decryption")
        else :
            break
    
    if selectedCipher == "1" :
        if selectedMethod == "1" :
            EncryptCaesar()
        else :
            DecryptCaesar()
    else :
        break