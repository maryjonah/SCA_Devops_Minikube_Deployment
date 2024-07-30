## Running the application
- Clone the repository
`git clone `
- Start minikube
`minikube start`
- Create deployment and service 
`kubectl apply -f kubernetes/deployment.yaml`
- Check the url to view the application
`minikube service python-on-kube-service --url`
