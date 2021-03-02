pipeline {
    agent any 
    stages{
        stage("Test-Application"){
            steps{
                sh "chmod +x -R ${env.WORKSPACE}"
                sh './jenkins/test-application.sh'
            }
        }
        stage('Build'){
            steps{
                sh ''' sudo chmod 666 /var/run/docker.sock
                docker-compose down --rmi all
                docker-compose build
                sudo docker login -u abusyd1 -p TempPass2021
                sudo docker-compose push
                '''
            }
        }
        stage("Ansible"){
            steps{
                sh '''
                    cd ansible
                    chmod 666 inventory.yaml playbook.yaml
                    ls -la
                    ansible-playbook -i inventory.yaml playbook.yaml
                    '''     
            }
        }
        stage("Deploy-Services"){
            steps{
                sh './jenkins/deploy-services.sh'
            }
        }                   
    }
}

