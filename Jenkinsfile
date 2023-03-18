pipeline {
    agent any
    stages {
        stage('data_preparation'){
            steps {
                sh 'python3 data_preprocessing.py'
            }
        }
        stage('model_preparation'){
            steps {
                sh 'python3 model_preparation'
            }
        }
        stage('model_testing'){
            steps {
                sh 'python3 model_testing.py'
            }
        }
    }
}