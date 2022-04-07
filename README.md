# NB6VAC-SB7-API
Réplique de l'API de la NB6VAC pour faire fonctionner le décodeur SB7 de chez SFR.  

Cette API à été développé dans le but de remplacer la box SFR par un routeur OpenWrt afin d'avoir une bien meilleure stabilité dans le temps (salut la box qui crash sur un maj Xbox) et pouvoir tirer profit au maximum de ce que ligne offre.  

L'API tourne sur du x86 (i3-5005U) sans soucis, pareil pour du mipsel_24kc (MT7621)

## Dépendances
- flask
- pytz
- waitress

Nécessite d'installer pip
`# pip3 install flask pytz waitress`

Ou sinon de compiler son image directement avec ces dépendances.

## Lancement
On est obligé de mettre l'API sur le port 80 à cause du décodeur. Il faudra donc les privilèges super utilisateur pour lancer le script.

`# python3 app.py`

Comme LuCi prend le port 80 par défaut, il faut le remap sur un autre (ex: 81)
