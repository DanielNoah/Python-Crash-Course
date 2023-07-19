pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('hey')  {
      steps {
        sh 'python ex2_Employee_employee.py'
      }
    }
  }
  }
