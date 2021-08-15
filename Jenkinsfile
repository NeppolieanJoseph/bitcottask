pipeline {
    environment {
        registry = "https://hub.docker.com/repositories/neppoliean"
        registryCredential = '231c6c3b-36d6-4223-b261-326b7cfad29c'
        }
    agent any
    stages {
        stage('Build mongodb image') {
            steps {
                script {
                    // The below will clone your repo and will be checked out to master branch by default.
                    git credentialsId: 'aaaf6d63-4496-4670-89e7-cd7b0d99dd1e', url: 'https://github.com/NeppolieanJoseph/bitcottask.git', branch: 'main'
                    // Do a ls -lart to view all the files are cloned. It will be clonned. This is just for you to be sure about it.
                    sh "ls -lart ./*" 
                    // List all branches in your repo. 
                    sh "git branch -a"
                    // Checkout to a specific branch in your repo.
                    sh "git checkout main"
                    
                    
                }
                
            }
            
        }
        stage('Build image for mongodb redis and nodejs and run the application from docker container') {
            steps {
                script {
                    sh "./dockerrm.sh"
                    sh "cd /var/lib/jenkins/workspace/bitcot-pipeline/mongodb && docker build -t neppoliean/mongodb . && docker run --name mongodb -p 27017:27017 -d neppoliean/mongodb"
                    sh "cd /var/lib/jenkins/workspace/bitcot-pipeline/redis && docker build -t neppoliean/redis . && docker run --name rediscache -p 6379:6379 -d neppoliean/redis"
                    sh "cd /var/lib/jenkins/workspace/bitcot-pipeline/ && python3 updateip.py"
                    sh "cd /var/lib/jenkins/workspace/bitcot-pipeline/nodejs && docker build -t neppoliean/nodejs . && docker run --name nodejs -p 3000:3000 -d neppoliean/nodejs"
                    
                }
                
            }
            
        }
        stage('Push imagss into dockerhub') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                        sh "docker push neppoliean/nodejs"
                        sh "docker push neppoliean/mongodb"
                        sh "docker push neppoliean/redis"
                    }
                    
                }
                
            }
            
        }
        
    }
    
}
