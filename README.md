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



## Website Health Check Script

This is a simple Python script to monitor the health of a website by checking its HTTP status and logging the results.

### Functions

- **get_timestamp()**  
  Returns the current timestamp. This is used to record when each health check is performed.

- **log_message(message)**  
  Takes a message as input and writes it to a log file along with the timestamp.

- **check_website(url)**  
  Accepts a website URL as input and checks its availability by making an HTTP request.  
  Logs whether the website is **UP** or **DOWN** based on the response status.

### Usage

Update the URL inside the script and run:

```bash
python script.py