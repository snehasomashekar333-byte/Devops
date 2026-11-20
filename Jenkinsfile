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
                dir('11-Jenkins-Metrics-Exporter') {
                    sh 'python3 -m pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                dir('11-Jenkins-Metrics-Exporter') {
                    sh 'python3 -m pytest -v'
                }
            }
        }

        stage('Package') {
            steps {
                dir('11-Jenkins-Metrics-Exporter') {
                    sh '''
                    mkdir -p dist
                    python3 -c "import zipfile; z=zipfile.ZipFile('dist/delivery-metrics.zip','w'); z.write('app.py'); z.write('requirements.txt'); z.close()"
                    '''
                    archiveArtifacts artifacts: '11-Jenkins-Metrics-Exporter/dist/delivery-metrics.zip', fingerprint: true
                }
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