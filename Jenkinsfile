pipeline {
    agent any
    environment {
        DATABASE_URI = credentials("DATABASE_URI")
    }
    stages {
        stage('Build') {
            steps {
                sh "export 'DATABASE_URI'=${DATABASE_URI}" 
                sh "docker pull lisajp4/plague_server"
                sh "docker pull lisajp4/plague_outcome"
                sh "docker pull lisajp4/plague_fortune"
                sh "docker pull lisajp4/plague_days"
            }
        }
        stage('Test') {
            steps {
                sh "sudo apt-get update && sudo apt-get install -y python-pip && rm -rf /var/lib/apt/lists/*"
                sh "pip install -U pytest"
                sh "cd server && pytest test_mock1.py"
                sh "cd outcome_api && pytest test_mock4.py"
                sh "cd days_api && pytest test_mock2.py"
                sh "cd fortune_api && pytest test_mock3.py"

            }
        }
        stage('Deploy') {
            steps {
                sh "docker stack deploy plague"
            }
        }
    }
}