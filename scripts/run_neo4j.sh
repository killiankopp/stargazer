#!/bin/sh
docker pull neo4j
docker run \
  --name neo4j \
  -d \
  -p 7474:7474 \
  -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/mypassword \
  neo4j
  echo "Neo4j is running at http://localhost:7474"
  echo "Username: neo4j"
  echo "Password: mypassword"