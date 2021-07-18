pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
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
        stage('Testing the files') {
            steps {
                sh "apt-get update -y"
                sh "apt install python3-pip python3-venv -y"
                sh "python3 -m venv venv"
                sh "source venv/bin/activate"
                sh "pip install -r requiements.txt"
                sh "cd server && pytest test_mock1.py"
                sh "cd outcome_api && pytest test_mock4.py"
                sh "cd days_api && pytest test_mock2.py"
                sh "cd fortune_api && pytest test_mock3.py"
            }
        }
        stage('Deploy') {
            steps {
                sh "docker swarm init"
                sh "docker stack deploy plague"
            }
        }
    }
}
