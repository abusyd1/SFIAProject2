pipeline {
    agent any 
    stages{
        stage("Test-Application"){
            steps{
                chmod +x test-application.sh
                sh './jenkins/test-application.sh'
            }
        }
        
        
        stage("Ansible"){
            steps{
                sh './jenkins/ansible.sh'
            }
        }
        
        
        stage("Build-Images"){
            steps{
                sh './jenkins/build-images.sh'
            }
        }
        
        
        stage("Deploy-Services"){
            steps{
                sh './jenkins/deploy-services.sh'
            }
        }                   
    }
}
