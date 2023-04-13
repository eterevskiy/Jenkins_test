pipeline {
  agent any
  stages {
    stage('Init') {
      steps {
        sh 'echo "hello world"'
        sh 'docker run python:buster'
        sh 'python3 --version'
        sh 'pip list'
      }
    }

  }
}