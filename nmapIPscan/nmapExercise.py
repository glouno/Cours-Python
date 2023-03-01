import os
import sys
'''
with open('/Users/glouno/Code/Cours Python/ipAddress.txt', 'r') as filin:
    for address in filin:
        print(address)
        os.system(f"nmap -Pn -A {address} -oA ip_date_scan")

'''

#faire un chmod pour rendre le fichier executable



with open(sys.argv[1], 'r') as filin:
    for address in filin:
        print(address)
        os.system(f"nmap -Pn -A {address} -oA ip_date_scan")

