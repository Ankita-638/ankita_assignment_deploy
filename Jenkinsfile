pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                sh 'mkdir -p /var/lib/jenkins/ankita_assignment_deploy'
                sh 'touch /var/lib/jenkins/ankita_assignment_deploy/playbook.yml /var/lib/jenkins/ankita_assignment_deploy/db_script.py /var/lib/jenkins/ankita_assignment_deploy/chaos_experiment.json'
            }
        }

        stage('Write Ansible Playbook') {
            steps {
                writeFile file: '/var/lib/jenkins/ankita_assignment_deploy/playbook.yml', text: '''
---
- name: Deploy Python Script
  hosts: localhost
  tasks:
    - name: Ensure Python is installed
      apt:
        name: python3
        state: present

    - name: Copy Python script
      copy:
        src: db_script.py
        dest: /home/ankita/ankita_assignment_deploy/db_script.py
        mode: '0755'
'''
            }
        }

        stage('Deploy Script') {
            steps {
                sh 'ansible-playbook /var/lib/jenkins/ankita_assignment_deploy/playbook.yml'
            }
        }

        stage('Chaos Testing') {
            steps {
                sh 'chaos run /var/lib/jenkins/ankita_assignment_deploy/chaos_experiment.json || true'
            }
        }
    }
}
