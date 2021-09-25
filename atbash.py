import string

#Définition des variables nécessaires
alphabet = string.ascii_lowercase
reversedAlphabet = string.ascii_lowercase [::-1]
upperAlphabet = string.ascii_uppercase
reversedUpperAlphabet = string.ascii_uppercase [::-1]
specialChar = "@_!#$%^&*()?/\|}{~:]’"

#Fonction d'encryption
def EncryptAtbash():
    #Données nécessaires
    message = input("Your message : ")
    message = list(message)
    encrypted = ""
    
    #Encryption
    for letter in message:
        if letter in alphabet:
            encrypted += reversedAlphabet[alphabet.index(letter)]
        elif letter in upperAlphabet:
            encrypted += reversedUpperAlphabet[upperAlphabet.index(letter)]
        else:
            encrypted += letter

    #Output
    print("Encrypted message :", encrypted, "\n")


#Fonction de decryptage
def DecryptAtbash():
    #Données nécessaires
    message = input("Encrypted message : ")
    message = list(message)
    decrypted = ""
    
    #Encryption
    for letter in message:
        if letter in alphabet:
            decrypted += reversedAlphabet[alphabet.index(letter)]
        elif letter in upperAlphabet:
            decrypted += reversedUpperAlphabet[upperAlphabet.index(letter)]
        else:
            decrypted += letter

    #Output
    print("Decrypted message :", decrypted, "\n")