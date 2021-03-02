# SSH into manager
#! /bin/bash
sh 'ssh -o StrictHostKeyChecking=no root@10.138.0.11'
ssh 10.138.0.11 << EOF 
# Remove any previous locally built images 
docker-compose down --rmi local
# build the images for the services from the docker-compose.yaml
docker-compose build
# log into docker with the account credentials  
sudo docker login -u abusyd1 -p TempPass2021
# push our built images to dockerhub
sudo docker-compose push
EOF
