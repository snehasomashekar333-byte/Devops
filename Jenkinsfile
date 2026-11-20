pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code checked out successfully'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Package') {
            steps {
                bat 'if not exist dist mkdir dist'
                powershell 'Compress-Archive -Path app.py,requirements.txt -DestinationPath dist\\delivery-metrics.zip -Force'
                archiveArtifacts artifacts: 'dist/delivery-metrics.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the console output.'
        }
    }
}
