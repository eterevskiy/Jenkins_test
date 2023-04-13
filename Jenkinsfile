pipeline {
  agent none
  stages {
    stage('Init') {
      agent {
        docker {
          image 'python:buster'
        }

      }
      steps {
        sh 'echo "hello world"'
        sh 'python3 --version'
        sh 'pip list'
        sh 'pwd'
      }
    }

    stage('Test') {
      steps {
        sh 'python3 test1.py'
      }
    }

  }
}