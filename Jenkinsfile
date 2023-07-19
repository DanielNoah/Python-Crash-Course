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
        sh 'python3 ex2_Employee_employee.py'
      }
    }
  }
  }
