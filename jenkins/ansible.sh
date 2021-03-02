# Run ansible the playbook.yaml which will set up the docker swarm and install docker onto the swarm-manager, swarm-worker and ansible VM 
cd ansible
ansible-playbook playbook.yaml -i inventory.yaml
cd .. 