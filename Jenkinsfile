pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {
        stage('Build and push images') {
            steps {
                sh "docker rm -f $(docker ps -aq)
                sh "docker-compose up --build"
                sh "docker push lisajp4/plague_server"
                sh "docker push lisajp4/plague_outcome"
                sh "docker push lisajp4/plague_fortune"
                sh "docker push lisajp4/plague_days"
    stages {
        stage('Pull images from Dockerhub') {
            steps {
                sh "export 'DATABASE_URI'=${DATABASE_URI}" 
                sh "docker pull lisajp4/plague_server"
                sh "docker pull lisajp4/plague_outcome"
                sh "docker pull lisajp4/plague_fortune"
                sh "docker pull lisajp4/plague_days"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy --compose-file docker-compose.yaml plague"
            }
        }
    }
}
