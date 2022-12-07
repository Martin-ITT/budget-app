pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mkdir -p jenkinsdir1'
                echo 'I like git'
                writeFile encoding: 'UTF-8', file: 'cheese-is-no-meat', text: 'Boys in blue'
            }
        }
        stage('Test') {
            steps {
                git 'https://github.com/Martin-ITT/budget-app.git'
            }
        }
        stage('Deploy') {
            steps {
                echo 'I like cheese'
            }
        }
    }
}
