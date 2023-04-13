pipeline {
  agent {
    node {
      label 'docker-python'
    }

  }
  stages {
    stage('Init') {
      parallel {
        stage('Init') {
          steps {
            sh 'echo "hello world"'
            sh 'python3 --version'
          }
        }

        stage('Enviroment') {
          steps {
            sh 'source myenv/bin/activate '
            sh 'pip install selenium'
          }
        }

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