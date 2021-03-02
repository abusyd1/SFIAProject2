#! /bin/bash
ssh 10.138.0.11 << EOF 
sudo rm -rf SFIAProject2
  
git clone https://github.com/abusyd1/SFIAProject2.git
cd SFIAProject2
sudo docker login
 
 
sudo docker stack deploy --compose-file docker-compose.yaml generator
EOF