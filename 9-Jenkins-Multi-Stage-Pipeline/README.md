# Exercise 9: Python Multi-Stage Jenkins Pipeline
## Objective
Build, test, deploy, run, and verify a Python Flask application using a multi-stage Jenkins pipeline.
## Technologies Used
- Python 3
- Flask
- Jenkins
- Git and GitHub
- Linux shell commands
## Application
The Flask application responds to requests at `/` with:
`Hello, Jenkins Multi-Stage Pipeline!`
## Pipeline Stages
1. **Build:** Creates a Python virtual environment and installs dependencies.
2. **Test:** Runs automated unit tests.
3. **Deploy:** Copies application files into `python-app-deploy`.
4. **Run Application:** Starts the Flask application.
5. **Test Application:** Checks the HTTP endpoint and reruns the unit tests.
## Project Files
- `app.py`: Flask application.
- `requirements.txt`: Python dependencies.
- `test_app.py`: Automated unit test.
- `Jenkinsfile`: Defines the five pipeline stages.
- `hello-world.sh`: Jenkins Hello World shell script.
- `screenshots/`: Exercise screenshots.
## Local Testing
The unit test was executed locally using Python 3.10.9.
Result: **1 test passed.**
## Jenkins Configuration
- Suggested job name: `Python-MultiStage-Pipeline`
- Pipeline script: `Jenkinsfile`
- Agent requirement: Linux environment with Python 3, pip, and curl.
## Sample Code Attribution
This exercise uses sample code from:
https://github.com/rufiya06/devops-sample-code
## Jenkins Build Status
The Jenkins pipeline has not yet been independently verified in this repository.
## Screenshots
See the `screenshots` folder for the available exercise screenshots.
