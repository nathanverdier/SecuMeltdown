---
title: Attaque meldown Cours
Author: Lucie Bedouret, Rémi Regnault, Chloé..., Thomas..., Nathan Verdier
---

## Quesque c'est un attaque Meltdown

Meltdown est une vulnérabilité matérielle découverte exclusivement dans les microprocesseurs Intel x86 qui permet à un processus non autorisé l'accès privilégié à la mémoire. La vulnérabilité ne semble pas affecter les microprocesseurs AMD. Un code Common vulnerabilities and Exposures : CVE-2017-5754 a été émis. 

Elle permettre donc à un attaquant d'éxécution d'un code spécial de bas niveau appelé « code noyau », qui s'exécute notamment au cours d'un processus connu sous le nom d'exécution spéculative (du code est exécuté avant que l'on soit sûr d'en vouloir car c'est le code le plus "probable" d'être exécuté, ce qui permet d'éviter les contrôles de sécurité)

Cette exécution spéculative inappropriée crée une vulnérabilité du processeur qu'un attaquant peut exploiter pour accéder à des données très sensibles stockées dans la mémoire du noyau, telles que des mots de passe, des clés de chiffrement, des photographies personnelles, des e-mails, etc.

**Voici ce que nous dit sa CVE (CVE-2017-5754):**
Les systèmes dotés de microprocesseurs utilisant l'exécution spéculative et la prédiction de branchement indirecte peuvent permettre la divulgation non autorisée d'informations à un attaquant disposant d'un accès utilisateur local via une analyse par canal secondaire du cache de données.

**En ce qui concerne le system linux, voici ce que nous dit ce site débian:**

Plusieurs chercheurs ont découvert une vulnérabilité dans les processeurs Intel, permettant à un attaquant contrôlant un processus non privilégié de lire la mémoire à partir d'adresses arbitraires, y compris à partir du noyau et de tous les autres processus en cours d’exécution sur le système.

Cette attaque particulière a été appelée Meltdown et est traitée dans le noyau Linux pour l'architecture Intel x86-64 par un ensemble de correctifs nommés « Kernel Page Table Isolation », imposant une séparation presque complète entre les mappages d'adresses du noyau et de l'espace utilisateur et empêchant l'attaque. Cette solution peut avoir un impact en termes de performance, et elle peut être désactivée lors de l'amorçage en passant le code pti=off sur la ligne de commande du noyau.

Nous vous recommandons de mettre à jour vos paquets linux.

Pour disposer d'un état détaillé sur la sécurité de linux, veuillez consulter sa page de suivi de sécurité à l'adresse

## Pratique 

**Cette Partie n'est pas finit je drop juste de la théorie et des idées**

Pour faire l'attaque sur un système linux:

### Systeme linux prérequie:
désactiver le correctif nommée Kernel *Page Table Isolation* lors de l'armosage en passant le code pti=off sur la ligne de commande du noyau.

### L'attaque ![Attaque](Images/AttaqueIcon.png)

**Maintenant la prattique:**

