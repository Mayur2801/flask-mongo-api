pipeline {
    agent any

    environment {
        COMPOSE = "/usr/local/bin/docker-compose"
        REPO_URL = "https://github.com/Mayur2801/flask-mongo-api.git"
        APP_DIR = "flask-mongo-api"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }
        stage('Remove Existing Containers') {
            steps {
                // Remove flask_api container if it exists to avoid name conflicts
                sh 'docker rm -f flask_api || true'
                sh 'docker rm -f mongo || true'
            }
        }
        stage('Build and Deploy') {
            steps {
                dir("${APP_DIR}") {
                    sh "${COMPOSE} build"
                    sh "${COMPOSE} up -d"
                }
            }
        }
        stage('Save Logs') {
            steps {
                dir("${APP_DIR}") {
                    sh 'mkdir -p logs'
                    // Capture Flask API container logs
                    sh "docker logs flask_api > logs/api.log || true"
                    archiveArtifacts artifacts: 'logs/api.log', fingerprint: true
                }
            }
        }
    }
}
