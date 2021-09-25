import string

#Définition des variables nécessaires
alphabet = string.ascii_lowercase
upperAlphabet = string.ascii_uppercase
specialChar = "@_!#$%^&*()?/\|}{~:]’"

#Fonction d'encryption
def EncryptVigenere():
    #Données nécessaires
    message = input("Message : ")
    key = input("Key : ")
    encrypted = "" 
    
    #Sépare le message par la longueur de la clé
    splited_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    
    #Verification de la clé et encryption
    for each_split in splited_message:
        i = 0
        for letter in each_split:
            if key[i] in upperAlphabet:
                print("The key must consist of lowercase letters only")
                return
            if key[i] in specialChar or key[i].isdigit() == True:
                print("The key must be made up of letters only")
                return
            elif letter in alphabet:
                number = (alphabet.index(letter) + alphabet.index(key[i])) % 26
                encrypted += alphabet[number]
            elif letter in upperAlphabet:
                number = (upperAlphabet.index(letter) + alphabet.index(key[i])) % 26
                encrypted += upperAlphabet[number]
            elif letter == " " :
                encrypted += " "
            i += 1
    
    #Output
    print("Encrypted message : " + encrypted + "\n")


#Fonction de decryptage
def DecryptVigenere():
    #Données nécessaires
    message = input("Encrypted message : ")
    key = input("Key : ")
    decrypted = "" 
    
    #Sépare le message par la longueur de la clé
    splited_message = [message[i:i + len(key)] for i in range(0, len(message), len(key))]
    
    #Verification de la clé et encryption
    for each_split in splited_message:
        i = 0
        for letter in each_split:
            if key[i] in upperAlphabet:
                print("The key must consist of lowercase letters only")
                return
            if key[i] in specialChar or key[i].isdigit() == True or key[i] == " ":
                print("The key must be made up of letters only \n")
                return
            elif letter in alphabet:
                number = (alphabet.index(letter) - alphabet.index(key[i])) % 26
                decrypted += alphabet[number]
            elif letter in upperAlphabet:
                number = (upperAlphabet.index(letter)- alphabet.index(key[i])) % 26
                decrypted += upperAlphabet[number]
            elif letter == " " :
                decrypted += " "
            i += 1
    
    #Output
    print("Decrypted message : " + decrypted + "\n")