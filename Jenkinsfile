pipeline {
    agent any

    environment {
        COMPOSE_CMD = 'docker-compose'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/flask-mongo-api.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh "${COMPOSE_CMD} build"
            }
        }

        stage('Deploy Services') {
            steps {
                sh "${COMPOSE_CMD} down || true" // shut down old services if any
                sh "${COMPOSE_CMD} up -d"
            }
        }
    }

    post {
        always {
            sh "mkdir -p logs && docker logs flask_api > logs/api.log || true"
            archiveArtifacts artifacts: 'logs/**', allowEmptyArchive: true
        }
    }
}
