pipeline {
    agent docker {
        image 'python:latest'

    } 
    stages {
        stage('Stage 1') {
            steps {
                sh 'pip install -r requirements.txt'
                echo 'Hello world!' 
            }
        }
    }
}