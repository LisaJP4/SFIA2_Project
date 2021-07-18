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
                sh "sudo apt-get update"
                sh "sudo apt install python3-pip python3-venv -y"
                sh "python3 -m venv venv"
                sh ". ./venv/bin/activate"
                sh "pip install -r requirements.txt"
                sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd server/server_tests && python3 -m pytest test_mock1.py"
                sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd outcome_api && pytest"
                sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd fortune_api && pytest"  
                sh "export 'DATABASE_URI'=${DATABASE_URI} && . ./venv/bin/activate && cd days_api && pytest" 
            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy --compose-file docker-compose.yaml plague"
            }
        }
    }
}
