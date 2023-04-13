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
        sh 'pip list'
      }
    }

  }
}