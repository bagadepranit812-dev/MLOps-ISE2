pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Getting source code from GitHub'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-performance-app .'
            }
        }

        stage('Deploy Application') {
            steps {
                bat 'docker rm -f student-app || exit /b 0'
                bat 'docker run -d -p 5000:5000 --name student-app student-performance-app'
            }
        }
    }
}
