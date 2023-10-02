---
title: Présentation meltdown 3min
author: Lucie Bedouret, Rémi Regnault, Chloé Mourgald, Thomas Chazot, Nathan Verdier
geometry: margin=2cm
output: pdf_document
---

Meltdown est une vulnérabilité matérielle qui touche les processeurs Intel x86 et qui permet à un processus non autorisé l’accès à la mémoire de l’ordinateur et donc à toutes les informations de son utilisateur.
Elle a donc été nommée Meltdown, car elle fait fondre les barrières de sécurité qui isolant les données sensibles.
Cette attaque à été découverte par des chercheurs de Google le 3 janvier 2018, un code Common Vulnerabilities and Exposures : CVE-2017-5754 a été émis.

Selon eux, il est possible que chaque processeur Intel qui implémente l’exécution dans le désordre ou l’exécution spéculative soit affecté (= tous les processeurs depuis 1995)  
exécution dans le désordre : quand le processeur réorganise l’ordre dans lequel les instructions vont s’exécuter. Permets de mieux exploiter les ressources du processeur et de gagner du temps de calcul  
exemple : si une opération attend certaines données, au lieu de ne rien faire, le processeur lance une opération indépendante.  
Exécution spéculative : anticipation basée sur des prédictions de branchement qui vise à éviter les temps d’attente potentiels. Si la prédiction est correcte : le processeur à gagner du temps sinon il annule les opérations. Tous les processeurs utilisant le principe d’exécution spéculative peuvent être touchés.

Meltdown va surtout impacter les fournisseurs de services cloud : en effet, ces derniers permettent aux utilisateurs de faire tourner leurs programmes sur les mêmes serveurs où sont stockées des données sensibles.
On peut aussi noter que la paravirtualisation (docker …) est aussi impactée par l’attaque meltdown. 
paravirtualisation : système d’exploitation est conscient de son excès dans un environnement virtualisé, il communique avec le processeur.

Des correctifs ont été mis en place afin d’éviter à avoir à changer de processeur, mais ils ont toutefois conduit à la diminution des performances de ces derniers. Le concept est d’avoir une plus grande séparation entre la mémoire du noyau et les processus utilisateurs.
 

L’attaque Meltdown est associée à une attaque similaire : Spectre. Il touche les processeurs Intel, Apple, ARM et AMD, et peut être exploité pour les tromper et leur faire exécuter du code qu'ils ne devraient pas être autorisés à exécuter. Selon les experts en sécurité de Google, Spectre est beaucoup plus difficile à exploiter que Meltdown, mais aussi beaucoup plus difficile à atténuer.

