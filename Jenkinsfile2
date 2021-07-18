pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {
        stage('Pull images from Dockerhub') {
            steps {
                "export 'DATABASE_URI'=${DATABASE_URI}" 
                "docker pull lisajp4/plague_server"
                "docker pull lisajp4/plague_outcome"
                "docker pull lisajp4/plague_fortune"
                "docker pull lisajp4/plague_days"
            }
        }
        stage('Testing the files') {
            steps {
                "sudo apt-get update"
                "sudo apt install python3-pip python3-venv -y"
                "python3 -m venv venv"
                "source /venv/bin/activate"
                "pip install -r requirements.txt"
                "export 'DATABASE_URI'=${DATABASE_URI} && cd server && pytest"
                "export 'DATABASE_URI'=${DATABASE_URI} && cd outcome_api && pytest"
                "export 'DATABASE_URI'=${DATABASE_URI} && cd fortune_api && pytest"  
                "export 'DATABASE_URI'=${DATABASE_URI} && cd days_api && pytest" 
            }
        }
        stage('Deploy') {
            steps {
                "docker swarm init"
                "docker stack deploy plague"
            }
        }
    }
}
