for i in range(1, 11):
    print("Round:", i)
    print("Square of i:", i**2)
    #Je veux étudier l'espace entre les carrés des nombres: entre 1^2 et 2^2 il y a 3; entre 2^2 et 3^2 il y a 5; entre 3^2 et 4^2 il y a 7...
    print("Difference:", i**2-(i+1)**2)