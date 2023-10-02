---
title: Attaque meldown cours
author: Lucie Bedouret, Rémi Regnault, Chloé Mourgand, Thomas Cha, Nathan Verdier
geometry: margin=2cm
output: pdf_document
---

## Diapo you after Meltdown

Nous allons commencer par une présentation rapide de l'attaque Meltdown.
L'attaque Meltdown est une faille de sécurité informatique découverte en 2018. Cette dernière affecte les microprocesseurs et permet à l'attaquant d'accéder à des zones de la mémoire de l'ordinateur.
Heureusement, cette attaque à été découverte par une équipe de chercheurs de Google dont la mission est de repérer les failles de sécurité avant que ces dernières soient exploitées. A ce jour, on ne sait toujours pas si l'attaque Meltdown a été utilisée dans la nature.

## Comment marche l'attaque Meltdown

L'attaque meltdown se base sur une caractéristique des processeurs modernes appelée : la séparation entre la mémoire du noyau et la mémoire utilisateur.
En résumé, lors d'une attaque meltdown, un programme malveillant exécute du code qui lui permet d'accéder à des zones de la mémoire du noyau du système, normalement hors de portée des applications. Le programme pourra ensuite extraire des données sensibles de la mémoire tel que des mots de passe, des clés de chiffrement, ...
Cette attaque peut donc toucher tous les appareils dont le processeur utilise l'exécution spéculative. 
Cette attaque est différentes de celles que nous avons pu voir en cours car elle se base sur le matériel qui compose le PC.

## Exécution spéculative

## Comment se protéger de l'attaque Meltdown

Non, vous n'avez pas besoin de revendre votre nouveau PC avec un processeur intel ! 
La plupart des systèmes d'exploitation ont publiés des correctifs permettant d'éviter les attaques Meltdown. Ces modifications ont permis d'appliquer des techniques d'isolation du noyau et donc renforcer la sécurité. Malheureusement, ces correctifs ont un impact négatif sur les performances estimé entre 5% et 30% selon le type de processeur et les tâches effectuées.
Du coté des fabriquants de processeurs, l'Isolation du noyau (KAISER) a été mise en place pour séparer les espaces mémoires du noyau .
Donc si jamais votre systeme est vieux et non mis à jour, vous pourrez donc subir les attaques Meltdown.

## Le petit frère : Spectre