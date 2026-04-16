pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/pytest'
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                echo 'Deploying to Staging Server...'
                // Add SSH or Docker deploy commands here
            }
        }
    }
    post {
        failure { mail to: 'admin@example.com', subject: "Build Failed: ${env.JOB_NAME}" }
    }
}
