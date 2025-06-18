pipeline {
    agent any

    environment {
        COMPOSE = 'docker-compose'
        GIT_REPO = 'https://github.com/Mayur2801/flask-mongo-api.git'
        BRANCH = 'main' // or 'master' if that’s your default branch
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
                    userRemoteConfigs: [[
                        url: "${env.GIT_REPO}"
                    ]]
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

        failure {
            echo "❌ Build or Deployment failed. Check logs for details."
        }

        success {
            echo "✅ Flask API and MongoDB deployed successfully!"
        }
    }
}
