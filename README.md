## Building and Pushing Docker Image to DockerHub Registry
- After any change to the application, we need to rebuild the image and update the copy in dockerhub registry
- `docker build -t jonahmary17/python-on-kube:latest`
- Push updated image: `docker image push jonahmary17/python-on-kube`

## Pull Image to View Content
- 


## Running the application
- Clone the repository
`git clone https://github.com/maryjonah/SCA_Devops_Minikube_Deployment.git`
- Change directory to the cloned repository
`cd SCA_Devops_Minikube_Deployment`
- Set up minikube with the article: [Minikube and Kubectl — Setting up K8s Cluster Locally](https://praveendandu24.medium.com/kubernetes-tutorial-for-beginners-mastering-the-basics-in-1-hour-332db7b5916b)
- Start default minikube cluster
`minikube start`
- Create deployment and service 
`kubectl apply -f kubernetes/deployment.yaml`
- Copy the IP address returned from the command below and paste it in a browser to view the application
`minikube service python-on-kube-service --url`

![Screenshot of Random Quotes Image of the Day displayed in a browser.](https://github.com/maryjonah/SCA_Devops_Minikube_Deployment/blob/main/app/static/minikube_random_quotes_home_page.JPG)
