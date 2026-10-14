# Exercise 1: Hello Pod Using Kubernetes

## Aim
To deploy an Nginx application inside a Kubernetes Pod and access it using a NodePort Service.

## Tools Used
- Docker Desktop
- Minikube
- Kubernetes
- kubectl
- Nginx

## Procedure

### 1. Start Minikube
```bash
minikube start --driver=docker
```

### 2. Create the Pod
```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod
```bash
kubectl get pods
```

### 4. Expose the Pod
```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Verify the Service
```bash
kubectl get services
```

### 6. Access the Application
```bash
minikube service hello-k8s
```

## Result
Verify that the Nginx application runs inside the Pod and is accessible through the NodePort Service.
