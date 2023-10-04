---
title: Attaque meldown cours
author: Lucie Bedouret, Rémi Regnault, Chloé Mourgand, Thomas Cha, Nathan Verdier
geometry: margin=2cm
output: pdf_document
---

## Diapo you after Meltdown

Nous allons commencer par une présentation rapide de l'attaque Meltdown.
L'attaque Meltdown est une faille de sécurité informatique découverte en 2012. Cette dernière affecte les microprocesseurs et permet à l'attaquant d'accéder à des zones de la mémoire de l'ordinateur.
Heureusement, cette attaque à été découverte par une équipe de chercheurs de Google dont la mission est de repérer les failles de sécurité avant que ces dernières soient exploitées. A ce jour, on ne sait toujours pas si l'attaque Meltdown a été utilisée dans la nature.

## Comment marche l'attaque Meltdown

L'attaque meltdown se base sur une caractéristique des processeurs modernes appelée : la séparation entre la mémoire du noyau et la mémoire utilisateur.
En résumé, lors d'une attaque meltdown, un programme malveillant exécute du code qui lui permet d'accéder à des zones de la mémoire du noyau du système, normalement hors de portée des applications. Le programme pourra ensuite extraire des données sensibles de la mémoire tel que des mots de passe, des clés de chiffrement, ...
Cette attaque peut donc toucher tous les appareils dont le processeur utilise l'exécution spéculative. 
Cette attaque est différentes de celles que nous avons pu voir en cours car elle se base sur le matériel qui compose le PC.

## Exécution spéculative

## Les 3 étapes de l'attaque 

## Comment se protéger de l'attaque Meltdown

Non, vous n'avez pas besoin de revendre votre nouveau PC avec un processeur intel ! 
La plupart des systèmes d'exploitation ont publiés des correctifs permettant d'éviter les attaques Meltdown. Ces correctifs modifient la façon dont l'ordonnanceur du processeur et isolent les données sensibles. Malheureusement, ces correctifs ont un impact négatif sur les performances estimé entre 5% et 30% selon le type de processeur et les tâches effectuées.
Du coté des fabriquants de processeurs, l'Isolation du noyau (KAISER) a été mise en place pour séparer les espaces mémoires du noyau .
Donc si jamais votre systeme est vieux et non mis à jour, vous pourrez donc subir les attaques Meltdown.

## Kaiser : qu'est-ce que c'est ?

Kaiser signifie Kernel Address Isolation to have Side-channels Efficiently Removed. C'est un projet mis en oeuvre pour atténuer certaines vulnérabilités matérielles. 
Ce dernier créer une isolation plus strict entre l'espace mémoire du noyau et la mémoire de l'utilisateur. Il a été mis en place dans les processeurs Intel.

Il est composé de :
* KPTI (Kernel Page Table Isolation) : maintient des tables de pagination distinctes pour l'espace mémoire du noyau et pour la mémoire utilisateur.
Avant l'introduction du KPTI, le noyau et les processus utilisateurs partageaient les mêmes tables de pagination mémoire. 
(Rappel : une table de pagination permet de traduire les adresses mémoires virtuelles utilisées par les programmes en adresses mémoires physiques. La mémoire est divisée en pages et une table de pagination est créer pour suivre la correspondance entre adresses virtuelles et adresses physiques).
Quand un processus passe du mode utilisateur au mode noyau pour effectuer une opération , les tables de paginations appropriées sont activées garantissant que seule les adresses virtuelles autorisées pour le mode en cours sont autorisés.   
* PCID (Process-Context Identifiers)  : fonctionnalité matérielle permettant de conserver les tables de pagination en cache distinct pour chaque contexte de processus.
Reduit la surchage lors du changement de contexte entre les processus. 

Le point négatif de KAISER est qu'il peut avoir un impact sur les performances du système car fonctionne avec une surchage de gestion de la mémoire. Les performances peuvent donc varier en fonction de la charge de travail et de l'architecture matérielle.

## Le petit frère : Spectre

Spectre est une attaque très similaire à Meltdown. 
Ce dernier utlise l'execution spéculative pour lire la mémoire cache. 
Il existe plusieurs variantes de cette attaque et elles exploitent differemment la spéculation du processeur pour accéder aux données sensibles.
Cette dernière est quasiement impossible à détecter et donc il est possible que vous ayez été victime d'une attaque Spectre sans le savoir.

## Différences entre Spectre et Meltdown

Il est interressant de noter que l'attaque Meltdown repose sur Spectre pour fonctionner. 