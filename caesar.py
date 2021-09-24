import string

#Définition des variables nécessaires
alphabet = string.ascii_lowercase*2
upperAlphabet = string.ascii_uppercase*2
specialChar = "@_!#$%^&*()?/\|}{~:]â€™"

#Fonction d'encryption
def EncryptCaesar():
    #Données nécessaires
    message = list(input("Your message : "))
    key = input("Your key : ")
    
    encrypted = ""

    #Vérification de la clé
    if key.isdigit() == False:
        print("The key must be an intenger beetween 1 and 26")
        return

    key = int(key)
    if key < 1 :
        print("The key must be an intenger beetween 1 and 26")
    elif key > 26 :
        print("The key must be an intenger beetween 1 and 26")
    
    #Encryption
    for x in message :
        if x in alphabet :
            encrypted += alphabet[alphabet.index(x) + key]                  
        elif x in upperAlphabet:
            encrypted += upperAlphabet[upperAlphabet.index(x)+key]
        elif x == " " :
            encrypted += " "
        else:
            encrypted += x
    
    #Output
    print(encrypted, "\n")



#Fonction de décryptage
def DecryptCaesar() :
    #Données nécessaires et choix de la manière de décryptage
    message = list(input("Initial message : "))
    haveKey = input("Do you have the key ? (y/n) ")
    decrypted = ""

    #Lorsque l'on connaît la clé
    if haveKey == "y" :
        key = input("The key of the message : ")
        
        #Vérification de la clé
        if key.isdigit() == False:
            print("The key must be an intenger beetween 1 and 26")
            return

        key = int(key)
        if key < 1 :
            print("The key must be an intenger beetween 1 and 26")
        elif key > 26 :
            print("The key must be an intenger beetween 1 and 26")

        #Décryptage
        for x in message :
            if x in alphabet :
                decrypted += alphabet[alphabet.index(x) - key]                  
            elif x in upperAlphabet:
                decrypted += upperAlphabet[upperAlphabet.index(x) - key]
            elif x == " " :
                decrypted += " "
            else:
                decrypted += x
            
        print(decrypted, "\n")
    #Lorsque l'on ne connaît pas la clé
    elif haveKey == "n" :
        print("Here are the 26 possibilities to find the initial message :")
        for number in range(26) :
            for x in message :
                if x in alphabet :
                    decrypted += alphabet[alphabet.index(x) - number]                  
                elif x in upperAlphabet:
                    decrypted += upperAlphabet[upperAlphabet.index(x) - number]
                elif x == " " :
                    decrypted += " "
                else:
                    decrypted += x
            print(number, " : ", decrypted)
            decrypted = ""
        print("\n")
    #Si la répoonse n'est pas valide
    else :
        print("You must respond with y (for yes) or n (for no)")
    

    
    
    