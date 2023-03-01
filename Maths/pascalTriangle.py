'''
1
11
121
1331
14641
'''

orderN = int(input("Indiquez le nombre de lignes que vous voulez: "))

triangle = ['1', '11']

for line in range(1, orderN):
    print(line)
    nextLine = [1]

    for index in range(len((triangle[line]))-1):
        print("triangle[line][index]: ", triangle[line][index])
        print("triangle line index +1: ", triangle[line][index+1])

        nextLine.append(int(triangle[line][index])+int(triangle[line][index+1]))
        print("nextLine: ", nextLine)
        print("nextLine type: ", type(nextLine))
        
    
    nextLine.append(1)
    nextLine = str(nextLine) #BAD BAD BAD, converts whole list into a string with the parenthesis as well '[]'
    print("nextLine str: ", nextLine)
    print("nextLine str type: ", type(nextLine))
    triangle.append(''.join(nextLine))           #joins newLine list, turns it into a string and adds it to the triangle


print(triangle)


# n + (n+1) = (n+1)

'''
    for index, currentString in enumerate(triangle[line]):
        print("triangle: ", triangle)
        print("Triangle Line: ", triangle[line])
        print("Triangle Line type: ", type(triangle[line]))
        print("currentString: ", currentString)
        print("current string type: ", type(currentString))

        print("triangle line index +1: ", triangle[line][index+1])

        nextLine.append(int(currentString)+int(triangle[line][index+1]))
        print("nextLine: ", nextLine)
        print(currentString, type(currentString))
'''