from shlex import join
from tabnanny import check
import threading
import time
import random as random
import sys

list = []

def lire_fichier():
    with open("test.txt", 'r') as fichier:
        lignes = fichier.readlines()
    return lignes

def parser_contenu(contenu):
    resultat = {}
    for ligne in contenu:
        # Séparer la clé et la valeur à partir de la ligne
        cle, valeur = ligne.strip().split(':')
        resultat[cle] = valeur
    return resultat

def obtenir_valeur(cle, resultat):
    return resultat.get(cle, "error")

def ReadMemory(adress, list):
    time.sleep(random.randint(1, 8)/1000)
    contenu = lire_fichier()
    resultat = parser_contenu(contenu)
    valeur_obtenue = obtenir_valeur(adress, resultat)
    if valeur_obtenue=="error":
        raise Exception(f"Memory space: {adress} doesn't exist")
    list.append(valeur_obtenue)

def CheckPrivilege():
    time.sleep(7/1000)

def main(adress):
    thread1 = threading.Thread(target=ReadMemory, args=(adress, list,))
    thread2 = threading.Thread(target=CheckPrivilege)
    thread1.start()
    thread2.start()
    while (thread2.is_alive()):
        time.sleep(1/1000)
    if thread1.is_alive():
        raise Exception("Accès refusé")
    else:
        print("".join(list))

if len(sys.argv)!=2:
    print("Nombre d'arguments incorrect, exemple: ", sys.argv[0], " adresse")
    exit(-1)

main(sys.argv[1])