VelibStats
=========

Ce petit script permet de vérifier à intervalle réguliers (à lancer _via_ une tâche Cron) l'état des stations de Vélib que vous souhaitez surveiller. Il est ainsi possible de récupérer un graphe d'utilisation des stations que vous utilisez fréquemment en fonction de l'heure de la journée / du jour de la semaine etc. C'est également un petit exemple d'utilisation de l'API REST de Vélib en Python.

## Utilisation
Ce script sert à surveiller une station et à noter les vélos disponibles et les emplacements disponibles à chaque exécution, afin d'avoir des statistiques sur les stations alentours.

Il s'utilise en ligne de commande :
```` 
velib_stats.py NUMERO_DE_STATION 
````

Pour trouver le numéro unique identifiant la station qui vous intéresse, rendez-vous sur le site de Vélib (http://www.velib.paris.fr/Plan-stations) et recupérez le numéro de la station qui vous intéresse dans l'infobulle.

## Pré-requis
Vous aurez besoin de python3 et du module urllib3 (à installer avec pip au besoin) pour utiliser ce script.

## License
Please, send me an email if you use or modify this program, just to let me know if this program is useful to anybody or how did you improve it :) You can also send me an email to tell me how lame it is ! :)

### TLDR; 
I don't give a damn to anything you can do using this code. It would just be nice to
quote where the original code comes from.


--------------------------------------------------------------------------------
"THE NO-ALCOHOL BEER-WARE LICENSE" (Revision 42) :

    Phyks (phyks@phyks.me) wrote this file. As long as you retain this notice you
    can do whatever you want with this stuff (and you can also do whatever you want
    with this stuff without retaining it, but that's not cool...). If we meet some 
    day, and you think this stuff is worth it, you can buy me a <del>beer</del> soda 
    in return.
                                                                     Phyks
---------------------------------------------------------------------------------
