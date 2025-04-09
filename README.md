# End-to-End ML Project CI/CD Pipeline with Cloud Deployment 🚀

This repository demonstrates an **End-to-End Machine Learning Project** with a fully automated **CI/CD pipeline** and **Cloud Deployment**. The project leverages **GitHub Actions**, **AWS Elastic Container Registry (ECR)**, and **Docker** to ensure seamless integration, delivery, and deployment. 🌐

---

## 🌟 Features

- **Continuous Integration (CI)**:  
  ✅ Code linting and unit testing using GitHub Actions.  
  ✅ Ensures code quality and reliability before deployment.

- **Continuous Delivery (CD)**:  
  ✅ Dockerized ML application built and pushed to **AWS ECR**.  
  ✅ Automated deployment to a cloud environment.

- **Cloud Deployment**:  
  ✅ Deploys the ML application to **AWS ECR + EC2 Instance**.  
  ✅ Scalable and production-ready infrastructure.

---

## 🛠️ CI/CD Pipeline Overview

1. **Trigger**:  
   - The pipeline is triggered on every push to the `main` branch.  

2. **Continuous Integration**:  
   - **Code Checkout**: Pulls the latest code from the repository.  
   - **Linting**: Ensures the code adheres to best practices.  
   - **Unit Testing**: Runs automated tests to validate functionality.

3. **Build and Push Docker Image**:  
   - Builds a Docker image of the ML application.  
   - Tags and pushes the image to **AWS Elastic Container Registry (ECR)**.

4. **Deployment**:  
   - Pulls the latest Docker image from ECR.  
   - Deploys the containerized application to the cloud.  
   - Cleans up unused Docker images and containers.

---

## 📂 Folder Structure

- `.github/workflows/`: Contains the GitHub Actions workflow files for CI/CD.  
- `_Deployment Guide/`: Step-by-step instructions for deploying the application to AWS.  
- `src/`: Source code for the ML application.  
- `Dockerfile`: Configuration for building the Docker image.  

---

## 🚀 How It Works

1. **Build Phase**:  
   - The pipeline builds the Docker image and pushes it to AWS ECR.  

2. **Deployment Phase**:  
   - The pipeline pulls the Docker image and runs it in a cloud environment.  

3. **Environment Variables**:  
   - AWS credentials and configurations are securely managed using GitHub Secrets.  

---

## 📝 Prerequisites

- **AWS Account**: For Elastic Beanstalk, ECR, and ECS.  
- **GitHub Secrets**: Add the following secrets to your repository:  
  - `AWS_ACCESS_KEY_ID`  
  - `AWS_SECRET_ACCESS_KEY`  
  - `AWS_REGION`  
  - `ECR_REPOSITORY_NAME`  

---

## 🎯 Goals

- Automate the entire ML project lifecycle from development to deployment.  
- Ensure scalability, reliability, and maintainability of the deployed application.  

---

Feel free to contribute, raise issues, or suggest improvements! 😊  
