pipeline {
    agent any

    options {
        timestamps()
    }

    triggers {
        // Check GitHub every 2 minutes for new commits
        pollSCM('H/2 * * * *')
    }

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
        SERVER_IP = '172.22.145.70'   // change if your target server IP changes
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Syntax Check') {
            steps {
                sh 'python3 -m py_compile app.py'
                sh 'ansible-playbook -i inventory.ini deploy.yml --syntax-check'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }

        stage('Verify') {
            steps {
                sh 'curl -f --retry 5 --retry-delay 3 --retry-connrefused http://${SERVER_IP}:5000'
            }
        }
    }

    post {
        success {
            echo "Deployed successfully: http://${SERVER_IP}:5000"
        }
        failure {
            echo 'Pipeline failed. Check the Console Output above.'
        }
    }
}
