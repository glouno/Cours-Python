from logging import StringTemplateStyle
import secrets
import string
import math
import csv
import os
import hashlib
from cryptography.fernet import Fernet


#Possible additional features:
'''
Calculate password quality (entropy)
Save a secure hash in a file. With a password file with title of account type, username, password etc.
Encrypt files
Create a GUI !!! 
'''

def boolInput():                # Vérifie l'écriture correcte pour le flag et assigne sa valeur
    booleanInput = input("Écrivez 'Oui' ou 'Non': ")
    if booleanInput == "Oui":
        return True
    if booleanInput == "Non":
        return False
    else:
        print("Vous n'avez pas écrit de valeur correcte, réessayez.")
        return boolInput()

def randPass(length):           # Takes random choices from ascii_letters, digits and punctuation
    generatePass = ''.join([secrets.choice( string.ascii_uppercase * lettersFlag + 
                                            string.ascii_lowercase + 
                                            string.digits * numbersFlag +
                                            string.punctuation * punctuationFlag )
                                            for n in range(length)])
    
    return generatePass 

def passEntropy():              # Calculates password entropy
    nbCharacters = 26          #every password has lowercase letters, 26 characters in the set of lowercase letters
    if punctuationFlag == True:
        nbCharacters += len(string.punctuation)
    if numbersFlag == True:
        nbCharacters += len(string.digits)
    if lettersFlag == True:
        nbCharacters += len(string.ascii_uppercase)

    print("Number of characters in set:", nbCharacters)
    entropy = math.log2(nbCharacters) * passLength
    print(f"Entropy of your password: {entropy} bits of entropy per character")
    print("Un mot de passe avec 35 bits ou plus peut être considéré comme bon!")
    return entropy

def passDB():           # ¡¡¡ MAIN !!! (Base de données pour enregistrer les mdp et les username)
    global punctuationFlag, numbersFlag, lettersFlag, passLength
    accountName = input("Indiquez le nom du service pour lequel vous créez un mot de passe: ")
    userName = input("Indiquez votre nom d'utilisateur: ")

    passLength = int(input("Indiquez la longueur de votre mot de passe, elle doit être supérieure à 12: "))
    lengthFlag = False              #flag to check password length is superior to 12

    while lengthFlag == False:      #loop to check password length > 12
        if passLength >= 12:
            lengthFlag = True
        else:
            passLength = int(input("Veuillez indiquer une longueur de mot de passe supérieure à 12: "))

    print("Indiquez si vous voulez des charactères de ponctuation complexe '%;,:/&@{[]}': ")
    punctuationFlag = boolInput()
    print("Indiquez si vous voulez des charactères des chiffres: ")
    numbersFlag = boolInput()
    print("Indiquez si vous voulez des lettres Majuscules: ")
    lettersFlag = boolInput()

    newRow = [accountName, userName, randPass(passLength), passEntropy()]
    print("Here is your new account information, with a randomly generated password: ", newRow)


    file_exists = os.path.isfile('passwordDatabase.csv')        #Checking if file exists to write header later
    print(file_exists)
    with open('passwordDatabase.csv', 'a') as filout:
        pwDatabaseHEADER = ['Nom du service', "Nom d'utilisateur", "Mot de passe", "Entropie du mot de passe"]
        writer = csv.writer(filout)         #Schema is the following: ['Nom du service', "Nom d'utilisateur", "Mot de passe", "Entropie du mot de passe"]
        
        if not file_exists:
            writer.writerow(pwDatabaseHEADER)  # file doesn't exist yet, write a header
        
        writer.writerow(newRow)


def encryptpassDB():
    key = Fernet.generate_key()             # key generation
    
    with open('passwordDatabase.key', 'wb') as filekey:
        filekey.write(key)                  # string the key in a file

    fernet = Fernet(key)                    # using generated key

    with open('passwordDatabase.csv', 'rb') as file:
        original = file.read()              # opening the original file to encrypt
    
    encrypted = fernet.encrypt(original)    # encrypting the file
    
    # opening the file in write mode and
    # writing the encrypted data
    with open('passwordDatabase.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    

def decryptpassDB():
    with open('passwordDatabase.key', 'rb') as filekey:
        key = filekey.read()                  # read the fernet key in previously stored file
    
    fernet = Fernet(key)

    # opening the encrypted file
    with open('passwordDatabase.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # opening the file in write mode and
    # writing the decrypted data
    with open('passwordDatabase.csv', 'wb') as dec_file:
        dec_file.write(decrypted)
    

''' START EXECUTION '''

passDB()
encryptpassDB()

#To decrypt the DataBase:
#ATTENTION si vous enlevez le # ici, mettez en 2 sur passDB() et encryptpassDB()
#decryptpassDB()

'''
COMMENTAIRE:
Je n'ai pas finalisé ce que je voulais faire pour encrypter le fichier. Je voulais le decrypter 'live' pour modifier la donnée
et le réencrypter tout de suite
Actuellement les fonctions encryptpassDB() et decryptpassDB() servent juste à encrypter le fichier tel qu'il est.

ATTENTION elles doivent être utilisées séparément (et sans passDB(), sinon le fichier sera modifié et la clé ne sera plus valide)

J'ai juste rajouté ces fonctions pour tester la fonctionnalité d'encrypter, mais ça n'est pas utile pour un utilisateur lambda
car il faut changer le code pour ne pas éxecuter passDB() quand on veut décrypter / encrypter. 
'''