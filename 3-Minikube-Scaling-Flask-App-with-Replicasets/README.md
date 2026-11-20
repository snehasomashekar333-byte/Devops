# Exercise 3: Minikube Scaling Flask App with ReplicaSets
## Aim
To understand how Kubernetes ReplicaSets maintain the desired number of replicas of an application.
## Tools Used
- Docker
- Minikube
- Kubernetes
- kubectl
- Python Flask
## Overview
A Kubernetes ReplicaSet ensures that a specified number of pod replicas are running. If a pod fails or is deleted, the ReplicaSet attempts to create another pod to maintain the desired number of replicas.
## Files
- `app.py` - Flask application code
- `Dockerfile` - Instructions for building the application image
- `flashsale-replicaset.yaml` - Kubernetes ReplicaSet configuration
- `outputs/` - Saved command outputs and logs
- `screenshots/` - Exercise screenshots
## Procedure
1. Review the Flask application and Dockerfile.
2. Examine the ReplicaSet configuration.
3. Review the Kubernetes commands used to manage the ReplicaSet.
4. Inspect the saved outputs and screenshots to understand pod scaling and replica management.
## Result
This exercise covers the use of Kubernetes ReplicaSets to maintain application pod replicas.
