# Simple Footballer Generator
### _A simple app in which you can generate a Football player_

## Project Brief
According to the project specification, the objective of this project is to create a simple web application, made up of 4 services:
* Service 1 - Communicates with other 3 services, renders Jinja2 templates to interact with application, persists data in an SQL database
* Services 2 & 3 - Generate random objects
* Service 4 - Generates another object, based upon the results of Services 2 & 3
The application will also encapsulate the following:
* Asana Board
* Feature-Branch model within GitHub, subsequently built through CI Server (Jenkins) and deployed to a cloud-based virtual machine
* Jenkins webhook to recreate and redeploy changes
* Deployed using containerisation and an orchestration tool (Docker)
* Ansible Playbook to provision enviornment for application to run
* Reverse Proxy (NGINX) 

For this project, I will be creating a Footballer Generator - where Service 2 generates a position, Service 3 generates a nationality and Service 4 generates a random short description of the player, which is then displayed on Service 1.

