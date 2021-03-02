pipeline {
    agent any 
    stages{
        stage("Test-Application"){
            steps{
                sh 'export DB_URI="mysql+pymysql://root:root@34.105.84.9/flask_db"'
                sh 'export SEC_KEY="jdfhkhfvk"'
                sh "chmod +x -R ${env.WORKSPACE}"
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
                sh "export DB_URI="mysql+pymysql://root:root@34.105.84.9/flask_db""
                   "export SEC_KEY="jdfhkhfvk""
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
