# NB6VAC-SB7-API
Réplique de l'API de la NB6VAC pour faire fonctionner le décodeur SB7 de chez SFR

## Dépendances
- flask
- pytz
- waitress

`# pip3 install flask pytz waitress`

## Lancement
On est obligé de mettre l'API sur le port 80 à cause du décodeur. Il faudra donc les privilèges super utilisateur pour lancer le script.

`# python3 app.py`

J'utlise un routeur ARM maison avec OpenWrt pour faire tourner ce script alors j'ai dû changer le port de LuCi sur le 81.
