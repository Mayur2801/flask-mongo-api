pipeline {
    agent any

    environment {
        COMPOSE = 'docker-compose'
        GIT_REPO = 'https://github.com/Mayur2801/flask-mongo-api.git'
        BRANCH = 'main' // Update if your branch is different
    }

    options {
        timestamps()
        skipDefaultCheckout(true)
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.BRANCH}"]],
                    userRemoteConfigs: [[url: "${env.GIT_REPO}"]]
                ])
            }
        }

        stage('Build Docker Images') {
            steps {
                sh "${COMPOSE} build"
            }
        }

        stage('Deploy Services') {
            steps {
                sh """
                    ${COMPOSE} down || true
                    ${COMPOSE} up -d
                """
            }
        }
    }

    post {
        always {
            script {
                sh "mkdir -p logs || true"
                sh "docker logs flask_api > logs/api.log || true"
            }

            archiveArtifacts artifacts: 'logs/**', allowEmptyArchive: true
        }

        success {
            echo "✅ Deployment succeeded!"
        }

        failure {
            echo "❌ Deployment failed. Check logs for troubleshooting."
        }
    }
}
