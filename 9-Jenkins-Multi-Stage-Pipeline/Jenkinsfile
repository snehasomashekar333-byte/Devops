pipeline {
    agent any
    environment {
        APP_DIR = "${WORKSPACE}/python-app-deploy"
        VENV = "${WORKSPACE}/.venv"
    }
    stages {
        stage('Build') {
            steps {
                echo 'BUILD: Installing Python dependencies'
                sh '''
                    python3 -m venv "$VENV"
                    "$VENV/bin/python" -m pip install --upgrade pip
                    "$VENV/bin/pip" install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'TEST: Running unit tests'
                sh '''
                    "$VENV/bin/python" -m unittest discover -s . -v
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'DEPLOY: Copying application files'
                sh '''
                    mkdir -p "$APP_DIR"
                    cp app.py requirements.txt test_app.py "$APP_DIR/"
                '''
            }
        }
        stage('Run Application') {
            steps {
                echo 'RUN APPLICATION: Starting Flask'
                sh '''
                    if [ -f "$APP_DIR/app.pid" ]; then
                        OLD_PID=$(cat "$APP_DIR/app.pid")
                        kill "$OLD_PID" 2>/dev/null || true
                        rm -f "$APP_DIR/app.pid"
                    fi
                    cd "$APP_DIR"
                    nohup "$VENV/bin/python" app.py > app.log 2>&1 &
                    echo $! > app.pid
                '''
            }
        }
        stage('Test Application') {
            steps {
                echo 'TEST APPLICATION: Checking the deployed endpoint'
                sh '''
                    cd "$APP_DIR"
                    for i in $(seq 1 15); do
                        if curl --fail --silent http://127.0.0.1:5000/ -o response.txt; then
                            break
                        fi
                        sleep 2
                    done
                    test -f response.txt
                    grep -Fx 'Hello, Jenkins Multi-Stage Pipeline!' response.txt
                    "$VENV/bin/python" -m unittest discover -s . -v
                '''
            }
        }
    }
    post {
        success {
            echo 'SUCCESS: All five pipeline stages completed!'
        }
        failure {
            echo 'FAILURE: Check the Console Output for the error.'
        }
    }
}
