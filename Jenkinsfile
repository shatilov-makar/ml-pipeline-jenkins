pipeline {
    agent any
    stages {
        stage('Pip install'){
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Data preparation'){
            steps {
                sh 'python3 data_preprocessing.py'
            }
        }
        stage('Model preparation'){
            steps {
                sh 'python3 model_preparation.py'
            }
        }
        stage('Model testing'){
            steps {
                sh 'python3 model_testing.py'
            }
        }
    }
}