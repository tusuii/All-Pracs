Installation docker and open docker-cli


https://docs.docker.com/desktop/install/windows-install/

Requirement json file practical 4 (spatial database)


https://raw.githubusercontent.com/mongodb/docs-assets/geospatial/neighborhoods.json

docker mongo setups


docker run mongo


docker ps (mongodb server should be running in background)


docker exec -it <Hash> mongosh
  
  
# execute mongodb practicals...
  

docker Redis setups
  
docker run redis
  
  
docker ps (redis server should be running in background)
  
  
docker exec -it <hash> redis-cli
  
  
# execute Redis practicals...

docker cassandra setup
  
  
docker pull cassandra
  
  
docker images
  
  
docker run -d --name cassandra cassandra-node -p 9042:9042 cassandra
  
  
docker ps
  
  
docker exec  -it cassandra-node bash
  
cqlsh   
  
cqlsh> cassandra practicals...
