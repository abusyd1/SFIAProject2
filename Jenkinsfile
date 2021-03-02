pipeline {
    agent any
    stages{
        stage("Test-Application"){
            steps{
                sh './jenkins/test-application.sh'
            }
        }
        stage("Build-Images"){
            steps{
                sh './jenkins/build-images.sh'
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

