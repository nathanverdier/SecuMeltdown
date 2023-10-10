# Simulation d'une attaque Meltdown

Petit hacker que vous êtes devenu au fil des TP de sécurité, vous avez découvert qu'un dépôt github privé contient des images d'une star que vous adorez. Vous voulez donc les récupérer, et ce par tous les moyens.

Vous savez que l'adresse ssh du dépôt en question est `git@github.com:JonathanDu63/AbsoluteFan.git`, et vous savez que Jonathan, la personne ayant créé le dépôt, a rentré sa clé publique pour lui permettre de cloner le dépôt.

L'idée vous vient alors de monter une attaque Meltdown sur la machine de Jonathan pour vous permettre de récupérer la mémoire de sa machine.

Vous pourrez alors récupérer la clé privée de Jonathan en scannant les adresses mémoires, vous permettant de cloner le dépôt à votre tour.

## Comment procéder ?

Sur vdn, lancer une machine virtuelle.

Ensuite, il faut monter l'attaque Meltdown. Pour ce faire, nous vous mettons à disposition le code python suivant, qui vous permet de simuler une attaque Meltdown sur la machine de Jonathan.

Cependant, ce code ne permet que de récupérer les données à une **(et une seule)** adresse mémoire en hexadécimal. Il va donc falloir que vous utilisiez ce code à bon escient pour vous permettre de récupérer la totalité de la mémoire et la mettre dans un fichier texte.

> **Attention !** Si la partie de l'l'exécution spéculative se termine avant que vous n'ayez pu récupérer les données à l'adresse voulue, vous ne récupèrerez rien, et vous manquerez peut-être la clé ssh !!! (le programme retournera alors une exeption)

Une fois chose faite, vous n'aurez plus qu'à convertir le fichier binaire obtenu en ASCII, et parcourir la mémoire jusqu'à trouver la clé ssh privée de Jonathan. 

> **Rappel** : Un fichier de clé ssh privé commence par `-----BEGIN OPENSSH PRIVATE KEY-----` et se finit par `-----END OPENSSH PRIVATE KEY-----`

Une fois ceci fait, vous n'aurez plus qu'à crée votre dossier .ssh sur votre machine virtuelle, y créer un fichier de clé privée ssh et clôner le dépôt.

Et voilà ! 🎉 Vous pouvez maintenant admirer les photos de votre star préférée 🙈
