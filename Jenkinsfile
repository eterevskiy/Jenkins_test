pipeline {
  agent any
  stages {
    stage('Init') {
      steps {
        sh 'echo "hello world"'
        sh 'python3 --version'
        sh 'pip list'
        sh 'pwd'
      }
    }

    stage('Test') {
      steps {
        sh 'source myenv/bin/activate'
        sh 'python3 test1.py'
      }
    }

  }
}