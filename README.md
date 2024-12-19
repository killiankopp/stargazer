# stargazer

Référence : https://mergify.notion.site/Stargazer-4cf5427e34a542f0aee4e829bb6d9035

Github API : https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28

Packages :
- 

**Objectif**
- créer un endpoint
```GET /repos/<user>/<repo>/starneighbours```
- retourner
```
[
 {
   "repo": <repoA>,
    "stargazers": [<stargazers in common>, ...],
 },
 {
   "repo": <repo>,
    "stargazers": [<stargazers in common>, ...],
 },
 ...
]
```

**Todo**
- lister les utilisateurs qui ont mis une étoile sur le repo
- Pour chaque utilisateur, lister les repos sur lesquels il a mis une étoile
- pour chaque repo, récupérer les utilisateurs en commun

## Quickstart

Pour lancer les services, exécuter le script `start.sh` à la racine du projet.

```sh
./start.sh
```

Vous obtiendrez les services suivants :

- base de données Neo4J
- API FastAPI

Utilisation

```sh
curl --request GET -sL \
     --url 'http://example.com'\
     --output './path/to/file'
```

## Installation des services (si vous ne voulez pas utiliser start.sh)

### installation de Neo4J

```sh 
cd scripts
./install_neo4j.sh
```

Interface de neo4J http://localhost:7474
Credentials : neo4j / mypassword