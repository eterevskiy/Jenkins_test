pipeline {
  agent none
  stages {
    stage('Init') {
      steps {
        sh 'echo "hello world"'
        sh 'python3 --version'
        sh 'pip list'
        sh 'docker run python:buster'
      }
    }

  }
}