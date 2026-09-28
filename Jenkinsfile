pipeline {
    agent any

    environment {
        IMAGE_NAME = "taskflow-api"
        IMAGE_TAG = "build-${BUILD_NUMBER}"
        CONTAINER_NAME = "taskflow-api-test"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Python Syntax Check') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build \
                    -t ${IMAGE_NAME}:${IMAGE_TAG} \
                    .
                '''
            }
        }

        stage('Run Test Container') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} || true

                    docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p 5001:5000 \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    sleep 5
                    curl --fail http://localhost:5001/health
                '''
            }
        }
    }

    post {
        always {
            sh '''
                docker rm -f ${CONTAINER_NAME} || true
            '''
        }

        success {
            echo 'TaskFlow CI pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed. Check the Jenkins console output.'
        }
    }
}
