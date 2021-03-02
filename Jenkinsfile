pipeline {
    agent any 
    stages{

        stage('Test'){
            steps{
                sh '''
                cd ./service1
                pip3 install -r requirements.txt
                pytest --cov=application --cov-report=term-missing
                cd ..
                # test service2
                cd ./service2
                pytest --cov=application --cov-report=term-missing
                cd ..
                # test service3
                cd ./service3
                pytest --cov=application --cov-report=term-missing
                cd ..
                # test service4
                cd ./service4
                pytest --cov=application --cov-report=term-missing
                cd ..
                '''
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

