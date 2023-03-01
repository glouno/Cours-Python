import hashlib
# MODULE SYS
'''On peut mettre un argument avec 

sys.argv[0]

pour appeler un script Python dans le terminal et mettre un argument directement à coté (comme une fonction)

Dans le terminal:
--> fichier.py argument0

Modules:
- sys
- os

'''

#ENVIRONNEMENT VIRTUALISÉS
'''
python3 -m pip install <module>

Besoin de versions différentes ... --> on créé des environnements virtualisés

python3 -m venv virtualenv/MonProjet

on peut utiliser .virtualenv pour cacher le répertoire par exemple (faire ls -la pour voir les élements cachés dans le terminal)

changer les permissions du script pour le transformer en éxecutable, et au lieu d'appeler python3, 
on peut faire pleins de truc en plus et simplifier la commande qui l'appelle

script python executable system path


'''

'''
nmap -Pn -A <ipAddress> -oA filename-nmap
-Pn permet de forcer la machine a répondre au ping / passer outre les blocages
-A scan complet / global
-oA write all the results in this file?


'''

#ANECDOTE WORDPRESS:
'''
on peut connaitre le admin user en mettant /?author=1 à la fin du lien wordpress
on peut avoir accès aussi en faisant /wp-admin 
et on n'a plus qu'à brute force le mot de passe...


nslookup https://ece.fr
--> ça va donner l'adresse ip public ...
 
'''

'''
Méthode split 
'''
test = "girafe tigre singe"
test.split()

def passDBhashed():     #On découpe le fichier pour éviter d'utiliser trop de RAM quand on le hash
    #J'ai vu cette méthode en ligne qui consiste à découper le fichier en petits chunks pour éviter d'utiliser trop de RAM
    
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    sha1 = hashlib.sha1()

    with open('passwordDatabase.csv', 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    print("SHA1: {0}".format(sha1.hexdigest()))
    ...