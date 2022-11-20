# Fursa - Hw3

1-Create a Python Web APP (use either Flask or FastAPI libraries) that:
- Presents the Current BitCoin Price
- Stores the price in a Redis Database
- Presents the Average Price for the last 10 minutes

2- Dockerize the applications (Create Dockerfile and docker-compose.yml)

3- Create a Jenkinsfile for CI/CD that creates and pushes the generated Web application Docker image to Docker Hub

## after running the app:
```sh
http://localhost:5000
```

## Some screenshots

### localhost view 
![alt text](https://github.com/muhammad197/Fursa-home-work-3/blob/71b6e4c893d7a1d2753a70dd23ef57e9789f67d4/SH1.png)

### last 10 reads from API 
![alt text](https://github.com/muhammad197/Fursa-home-work-3/blob/71b6e4c893d7a1d2753a70dd23ef57e9789f67d4/SH2.png)

### Docker hub image
![alt text](https://github.com/muhammad197/Fursa-home-work-3/blob/48e900bffe8d977e96f5f1edd948c65b96e9e407/SH3.png)

## jenkins pipeline script:
```sh
pipeline {

  agent any
  
  stages {
      stage('clone') {
            steps {
                git url:"https://github.com/muhammad197/Fursa-home-work-3.git", branch:'main'
            }
        }
        
    stage('Build') {
      steps {
        sh 'docker build -t btc_to_ils_app:$BUILD_NUMBER .'
      }
    }
     stage('Build Tag') {
        steps{
            sh 'docker tag btc_to_ils_app:latest muhammadkrad/btc_to_ils_app:latest'
        }
         
     }

    stage('Push imp') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Doker-hub', passwordVariable: 'pass', usernameVariable: 'username')]) {
                   
                    sh 'docker login -u ${username} -p ${pass}'
                    sh 'docker push muhammadkrad/btc_to_ils_app:latest'
                }
            }
        }
    }

    
}
```
