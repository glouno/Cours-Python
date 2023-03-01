from re import X


print("Hello World!")
'''
clientDataExample = ['Beglin', 'Paul', +447808586415, 22]  #Schema: ['Nom', 'Prénom', Téléphone, Age]

name = input("Votre Nom: ")
firstName = input("Votre Prénom: ")
phoneNumber = input("Votre numéro de téléphone: ")
age = input("Votre Age: ")

clientData = [name, firstName, phoneNumber, age]

print(clientDataExample)
print(clientData)

drinksMenu = ["café", "bière", "mojito", "caipirinha"]

for i, drink in enumerate(drinksMenu, start=1):
    print(i, drink)


impairs = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
pairs = []
for nb in impairs:
    pairs.append(nb+1)

print(pairs)
'''
'''
#Dessiner un triangle rectangle puis triangle isocèle à partir de '*' de 10 de haut
space = ' '
print('test')
print(space*0,'test')
for i in range(10):
    print('*',space*i,'*')

print('*'*13)
'''
'''
for i in range(11):
    print('*'*i)

for i in range(11):
    print(' '*(10-i),'*'*i+'*'*i)
    print(' '*(10-i),'*'*2*i)
'''
'''
for i in range(11):
    for j in range(11):
        print(' '*)
'''

'''
combinaison = []

for i in range(201):                            #le nombre est inférieur à 200
    if i % 2 == 0:                               #c'est un nombre pair
        iSTR = str(i)
        iLIST = list(map(int, iSTR.strip()))
        if sum(iLIST) == 5:                     #la somme des chiffres = 5
            x1 = iSTR[0]
            x2 = iSTR[1]
            if i < 100:
               x3 = 0 
            else:
                x3 = iSTR[2]
            if x1 == x2 or x1 == x3 or x2 == x3:
                combinaison.append(iSTR)
            else:
                continue
        else:
            continue

    else:
        continue

print(combinaison)

test = '50'
testSTR = str(test)
print(testSTR)
print(testSTR[0])
print(testSTR[1])
'''

'''
test = 122
testSTR = str(test)
print(testSTR)
testLIST = list(map(int, testSTR.strip()))
'''

### SYRACUSE CONJECTURE:

#newX = int(input("Nombre de départ: "))

'''
for x in range(2,20):
    flag = 0
    print("User input: ", x)
    while flag < 3:
        if x % 2 == 0:
            x = int(x/2)
            print(x)
        else:
            x = 3*x + 1
            print(x)
        
        if  x == 1:
            flag +=1
        else:
            continue
        
        print("ENDENDENDEND")

## Très utile pour la syntaxe:
print(f"Syracuse terminé {x}")
print("Syracuse Terminé {}".format(x))
'''
'''
def Syracuse(n):
    print(n)
    if n == 1:
        return n
    if n % 2 == 0:
        return Syracuse(int(n/2))
    else:
        return Syracuse(3*n+1)


C = int(input("Syracuse Conjecture: "))
Syracuse(C)

'''


with open('/Users/glouno/Code/Cours Python/oddnumb.txt', 'r') as filin, open('/Users/glouno/Code/Cours Python/evennumb.txt', 'w') as filout:
    for nb in filin:
        print(nb)
        print(type(nb))
        filout.write(str(int(nb)+1) + '\n')

notPrime = []
prime = []
notSure = []

def is_prime(nRange):
    print("2 est premier")
    prime.append(2)
    print("3 est premier")
    prime.append(3)
    for n in range(4, nRange):
        if n % 2 == 0:                  #if even we discard those numbers
            print(n, "n'est pas premier")
            notPrime.append(n)
            continue
        else:
            if n == 5:
                print("5 est premier")
                prime.append(5)
            elif n % 5 == 0:            #gets rid of numbers divisible by 5
                print(n, "n'est pas premier")
                notPrime.append(n)
                continue
            else:
                for i in range(2, int(n/2)+1):
                    if n%i == 0:
                        print(n, "n'est pas premier")
                        notPrime.append(n)
                        break
                    elif i == int(n/2):
                        print(n, "est premier")
                        prime.append(n)
                        
            


is_prime(100)
print("Not Prime:", notPrime)
print("Number of Primes", len(prime), "Prime:", prime)
print("Not Sure: ", notSure)