import string

#Définition des variables nécessaires
alphabet = string.ascii_lowercase
upperAlphabet = string.ascii_uppercase

#Fonction d'encryption
def EncryptAffine():
    #Données nécessaires
    encrypt = ""
    message = input("Message : ")
    a = input("Slope (a) : ")
    b = input("Y-interept (b) : ")
    replacedA = ''
    replacedB = ''

    #Vérification des nombres
    allowed="0123456789-"
    if all([i in allowed for i in a]) == False:
        print("Keys must be composed full of integers")
        return
    elif all([i in allowed for i in b]) == False:
        print("Keys must be composed full of integers")
        return
    #Conertit la clé en int
    a = int(a)
    b = int(b)
    
    #Encryptage
    for letter in message:
        if letter in alphabet:
            number = (alphabet.index(letter)*a+b) % 26
            encrypt += alphabet[number]
        elif letter in upperAlphabet:
            number = (upperAlphabet.index(letter)*a+b) % 26
            encrypt += upperAlphabet[number]
        else:
            encrypt += letter
    
    #Output
    print("Encrypted Message : " + encrypt, "\n")

#Fonction de décryptage
def DecryptAffine():
    #Données nécessaires
    decrypted = ""
    message = input("Message : ")
    a = input("Slope (a) : ")
    b = input("Y-interept (b) : ")
    replacedA = ''
    replacedB = ''

    #Vérification des nombres
    allowed="0123456789-"
    if all([i in allowed for i in a]) == False:
        print("Keys must be composed full of integers")
        return
    elif all([i in allowed for i in b]) == False:
        print("Keys must be composed full of integers")
        return
    #Conertit la clé en int
    a = int(a)
    b = int(b)
    
    #Encryptage
    for letter in message:
        if letter in alphabet:
            number = ((alphabet.index(letter)-b)//a) % 26
            decrypted += alphabet[number]
        elif letter in upperAlphabet:
            number = ((upperAlphabet.index(letter)-b)//a) % 26
            decrypted += upperAlphabet[number]
        else:
            decrypted += letter
    
    #Output
    print("Encrypted Message : " + decrypted, "\n")