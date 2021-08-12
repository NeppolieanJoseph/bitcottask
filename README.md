# bitcottask

dockerfiles and docker-compose both are available for this project

Run from Dockerfile:
create images:
cd mongodb
docker build -t neppoliean/mongodb .

cd ../redis
docker build -t neppoliean/redis .

cd ../nodejs
docker build -t neppoliean/nodejs .

Run is as containers:

docker run --name mongodb -p 27017:27017 -d neppoliean/mongodb
docker run --name rediscache -p 6379:6379 -d neppoliean/redis

Now inspect the docker containers and copy their IP addresses and paste it into config.json file in nodejs/config.json

Now run the nodejs container

docker run --name nodejs -p 3000:3000 -d neppoliean/nodejs.


Now try to curl http://localhost:3000/add-student


Try to run it from docker compose run it inthe root directory docker-compose up..

It will start the new containers and communicate with each others
