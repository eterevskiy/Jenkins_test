pipeline {
  agent {
    node {
      label 'docker-python'
    }

  }
  stages {
    stage('Init') {
      steps {
        sh 'echo "hello world"'
        sh 'python3 --version'
        sh 'source myenv/bin/activate  '
      }
    }

    stage('Test') {
      steps {
        sh 'echo "Working..."'
        sh 'python3 test1.py'
      }
    }

  }
}