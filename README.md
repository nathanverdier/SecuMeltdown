![<img src="Images/Meltdown_icon.png" width="50"/>](Images/Meltdown_icon.png)

## Qu’est-ce que c'est une attaque Meltdown

Meltdown est une vulnérabilité matérielle découverte exclusivement dans les microprocesseurs Intel x86 qui permet à un processus non autorisé l'accès privilégié à la mémoire. La vulnérabilité ne semble pas affecter les microprocesseurs AMD. Un code Common Vulnerabilities and Exposures : CVE-2017-5754 a été émis suite à sa découverte par des chercheurs de chez Google 3 janvier 2018. Tous les processeurs Intel depuis 1995 seraient touchés par cette faille.

Elles permettre donc à un attaquant d'exécution d'un code spécial de bas niveaux appelés « code noyau », qui s'exécutent notamment au cours d'un processus connu sous le nom d'exécution spéculative (du code est exécuté avant que l'on soit sûr d'en vouloir, car c'est le code le plus "probable" d'être exécuté, ce qui permet d'éviter les contrôles de sécurité)

Cette exécution spéculative inappropriée crée une vulnérabilité du processeur qu'un attaquant peut exploiter pour accéder à des données très sensibles stockées dans la mémoire du noyau, telles que des mots de passe, des clés de chiffrement, des photographies personnelles, des e-mails, etc.

Meltdown va donc surtout impacter les fournisseurs de services cloud : en effet, ces derniers permettent aux utilisateurs de faire tourner leurs programmes sur les mêmes serveurs où sont stockées des données sensibles.
On peut aussi noter que la paravirtualisation (docker …) est aussi impactée par l’attaque meltdown.

**Voici ce que nous dit sa CVE (CVE-2017-5754):**
les systèmes dotés de microprocesseurs utilisant l'exécution spéculative et la prédiction de branchement indirecte peuvent permettre la divulgation non autorisée d'informations à un attaquant disposant d'un accès utilisateur local via une analyse par canal secondaire du cache de données.

**En ce qui concerne le système Linux, voici ce que nous dit ce site débian:**

Plusieurs chercheurs ont découvert une vulnérabilité dans les processeurs Intel, permettant à un attaquant contrôlant un processus non privilégié de lire la mémoire à partir d'adresses arbitraires, y compris à partir du noyau et de tous les autres processus en cours d’exécution sur le système.

Cette attaque particulière a été appelée Meltdown et est traitée dans le noyau Linux pour l'architecture Intel x86-64 par un ensemble de correctifs nommés « Kernel Page Table Isolation », imposant une séparation presque complète entre les mappages d'adresses du noyau et de l'espace utilisateur et empêchant l'attaque. Cette solution peut avoir un impact en termes de performance, et elle peut être désactivée lors de l'amorçage en passant le code pti=off sur la ligne de commande du noyau.

Nous vous recommandons de mettre à jour vos paquets Linux.

Pour disposer d'un état détaillé sur la sécurité de Linux, veuillez consulter sa page de suivi de sécurité à l'adresse

## Déroulement de l'attaque
### Etape 1 : Accès aux données
* On déplace les informations stockées dans un registre
* Il se passe deux choses :
  * on envoie l'instruction à l'unité dédié qui va éxécuter la commande grâce à l'exécution dans le désordre
  * cpu il cherche à savoir si oui ou non, le processus courant à le droit d'accèder à la mémoire ciblée
* exécuter l'étape 2 avant que le cpu lève une exception sur les droits d'accès
### Etape 2 : transmission des données
* On alloue un espace dans le stockage de façon à ce que aucune partie de l'espace ne soit dans la mémoire cache
* Pour ça, si taille des pages = $(4KB), alloue un espace de $(256x4KB) > à la taille des pages
### Etape 3 : Reception des données
* On récupère les données en iterant sur le tableau
### On refait jusqu'à récupérer TOUTE la mémoire

[Voir presentation](Presentation_Meltdown_Oral/)

## Pratique 

### Système Linux prérequis:
désactiver le correctif nommé Kernel *Page Table Isolation* lors de l'armosage en passant le code pti=off sur la ligne de commande du noyau.

### L'attaque !

[Maintenant la pratique](TP/)

