# 🚀 CI/CD Pipeline (ECR + EKS + Helm)

## Overview
This project demonstrates a simple CI/CD pipeline to deploy a microservice to Kubernetes.
Also i have added kubernetes manifest and python script.py file to this repo which is part of this assignment. 

On every push to `main`:
- Docker image is built  
- Image is pushed to AWS ECR  
- Application is deployed to EKS using Helm  

---

## ⚙️ Prerequisites
- AWS account  
- EKS cluster  
- ECR repository  
- GitHub repo with secrets:
  - AWS_ACCESS_KEY_ID
  - AWS_SECRET_ACCESS_KEY

---

## 🔄 Flow
Push → Build → Push to ECR → Deploy to EKS (Helm)

---

## 🚀 Deployment
Helm is used for deployment:
---

## 🔄 Flow
Push → Build → Push to ECR → Deploy to EKS (Helm)

---

## 🚀 Deployment
Helm is used for deployment:

helm upgrade --install devops-app ./helm-chart
--set image.repository=<ECR_URI>
--set image.tag=<COMMIT_SHA>


---

## 🔍 Verify
kubectl get pods

kubectl get svc


---

## 🧠 Summary
Basic CI/CD pipeline using GitHub Actions, Docker, AWS ECR, EKS, and Helm.



## Script to check website health 
This script is developed in python having 3 different methods as
get_timestamp() →  This method is responsible to get the timestamp of when the check is performed on the website to check the uptime of the website url passed in check_website(url) method.

log_message(message) → This method takes a paramneter as message which it prints it to log file.

check_website(url) →  This method gets a paramneter as url, this is the endpoint of the website to be monitored.