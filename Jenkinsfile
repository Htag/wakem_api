/* groovylint-disable CompileStatic, GStringExpressionWithinString, LineLength */
pipeline {
    agent any
    options {
        ansiColor('css')
    }
    environment {
        BRANCH_NAME = "${GIT_BRANCH.split('/')[1]}"
        GITHUB_TOKEN = credentials('jenkins-github-token')
    }

    stages {
        stage('Initialisation') {
            steps  {
                echo 'Initialisation.....................'
                withCredentials([usernamePassword(credentialsId: 'jenkins-github-uname-pwd', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
                    sh '''
                    echo \"https://${USERNAME}:${PASSWORD}@github.com\" > ~/.git-credentials
                    git config --global credential.helper 'store --file ~/.git-credentials'
                    git remote -v
                    make venv && make install
                    '''
                }
            }
        }
        stage('Checkout SCM') {
            steps {
                checkout([
                $class: 'GitSCM',
                branches: [[name: "${BRANCH_NAME}"]],
                userRemoteConfigs: [[
                    url: 'https://github.com/Htag/wakem_api',
                    credentialsId: '',
                    ]]
                ])
            }
        }

        stage('Setup') {
            steps {
                sh 'make venv && make install'
                echo "Branch name: ${BRANCH_NAME}"
            }
        }
        stage('Test') {
            when {  anyOf { branch 'ops' } }
            steps {
                sh 'make run-test'
            }
        }
        stage('Deploy Docker for developement environment') {
            when {  anyOf { branch 'dev' } }
            steps {
                echo 'Start building docker image for development'
                sh 'docker build --build-arg ARG_FLASK_ENV=1 -t  wakem/wakem_api_dev .'
                script {
                    try {
                        sh 'docker rm -f $(docker ps -a --no-trunc --filter name=wakem_api_dev -q)'
                        echo 'Container found...'
                    }
                    catch (err) {
                        ansiColor('css') {
                            echo "Unable to find that container: ${err}"
                        }
                    }
                    finally {
                        sh 'docker run --name kraft-api-dev -d -p 5000:5000 wakem/wakem_api_dev'
                    }
                }
            }
        }
    }
    post {
        // Clean after build
        always {
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true,
                    patterns: [[pattern: '.gitignore', type: 'INCLUDE'],
                               [pattern: '.propsfile', type: 'EXCLUDE']])
        }
    }
}
