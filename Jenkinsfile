pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python --version'
      }
    }
    stage('hey')  {
      steps {
        sh 'python ex2_Employee_employee.py'
      }
    }
  }
  }
