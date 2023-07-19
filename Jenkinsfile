pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'python3.8 --version'
      }
    }
    stage('hey')  {
      steps {
        sh 'python3.8 ex2_Employee_employee.py'
      }
    }
  }
  }
