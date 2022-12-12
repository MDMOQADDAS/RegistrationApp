pipeline {
    agent any

    stages {
        stage('scm') {
            steps {
                echo 'It is scm stages'
                git branch: 'main', url: 'https://github.com/MDMOQADDAS/RegistrationApp.git'
            }
        }
       stage('build'){
           steps{
              sh 'docker build -t moqaddas/registrationapp:$app_version .'
           }
       }
       
      stage('test'){
          steps{
              sh 'docker rm -f test || date'
              sh "docker run -d --name test -t -p 80:80 moqaddas/registrationapp:$app_version"
              sh "curl localhost | grep Registration"
          }
        }
        stage("Centralized Container Registery"){
            steps{
                sh 'docker login https://docker.io -u $dockerUser -p $dockerpassword'
                sh 'docker push moqaddas/registrationapp:$app_version'
            }
        }
    }
}

