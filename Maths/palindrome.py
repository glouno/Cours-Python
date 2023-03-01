#Écrire une fonction qui prend en argument une chaine de caractère en argument et dit si c'est un palindrome

def palindrome(text):
    string = text.lower()
    string = string.replace(' ', '')            #Could use the .translate() function to get rid of \n ... characters

    for i, character in enumerate(string):
        if i+1 > len(string)//2:
            print("This is a palindrome!")
            break
        if character == string[-(i+1)]:
            continue
        else:
            print("Cette chain de caractères n'est pas un palindrome")
            break

palindrome(input("Votre chaine de caractères:"))
