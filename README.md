# 🚀 CI/CD Pipeline (ECR + EKS + Helm)

## Overview
This project demonstrates a simple CI/CD pipeline to deploy a microservice to Kubernetes.

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