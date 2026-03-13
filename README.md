# MiniFlix 🎬 — Netflix-Style App with Kubernetes & GitOps

MiniFlix is a Netflix-style web application deployed on Kubernetes using a GitOps workflow with Argo CD.

The project demonstrates a modern DevOps delivery pipeline where application changes are automatically built, published, and deployed using **Git as the single source of truth**.

The platform includes:

- A frontend UI displaying movie tiles in a Netflix-style layout
- A Catalog API serving movie data
- A GitOps deployment pipeline that continuously syncs Kubernetes with the Git repository

---

# 🌐 Live Demo

Frontend  
http://13.219.139.230

API example  
http://13.219.139.230/api/movies

Health check  
http://13.219.139.230/api/health

---

# What the App Does

MiniFlix demonstrates a simple streaming-platform style interface.

Users can:

- Open a Netflix-style UI
- Browse movie tiles
- Search titles
- Fetch movie data through the API

Example API response:

```json
[
  {
    "id": 1,
    "title": "Night Shift Lagos",
    "year": 2024,
    "genre": "Drama"
  }
]
```

---

# 🛠 Tech Stack

## Infrastructure

- AWS EC2
- Kubernetes (k3s)

## DevOps

- GitOps deployment with Argo CD
- CI pipeline using GitHub Actions
- Container registry: Docker Hub

## Application

### Frontend
- HTML
- Tailwind CSS
- Nginx

### Backend
- FastAPI

### Networking
- NGINX Ingress Controller

### Monitoring
- Prometheus
- Grafana

---

# 🏗 Architecture Overview

The deployment pipeline follows a **GitOps model**:

```text
Developer Push
      ↓
GitHub Actions (CI)
Build Docker Images
      ↓
Push Images → Docker Hub
      ↓
Update GitOps manifests
      ↓
ArgoCD detects change
      ↓
Kubernetes cluster syncs
      ↓
Pods update automatically
      ↓
NGINX Ingress exposes service
```

Application architecture inside Kubernetes:

```text
Internet
   │
   ▼
NGINX Ingress
   │
   ├── /        → Frontend service
   │
   └── /api/*   → Catalog API service
```

---

# Phase 1 — GitOps Platform Setup

## Goal

Build the GitOps foundation before deploying the application.

This phase focused on proving that the GitOps flow works:

```text
Git → ArgoCD → Kubernetes
```

## What Was Implemented

- Kubernetes environment (initially using Kind)
- NGINX Ingress Controller
- Argo CD installation
- GitOps deployment test application

ArgoCD continuously watches the Git repository and automatically applies updates to the cluster.

### Phase 1 Screenshots

Saved in:

```text
docs/screenshots/phase-1/
```

---

# Phase 2 — Deploy MiniFlix MVP

## Goal

Replace the test application with a real service:

- MiniFlix UI
- Catalog API
- Ingress routing

## Deployment Environment

Phase 2 runs on **AWS EC2 using k3s**.

Local development environments struggled with running:

- Kind
- Docker
- ArgoCD

Moving the cluster to EC2 provided a stable Kubernetes environment while keeping infrastructure costs low.

## Infrastructure Used

- 1 AWS EC2 instance
- k3s Kubernetes distribution

## Routing Configuration

Ingress rules route traffic as follows:

```text
/        → MiniFlix frontend
/api/*   → Catalog API
```

Example endpoints:

```text
/api/movies
/api/health
```

## Quick Verification Commands

Check ArgoCD application:

```bash
kubectl get app -n argocd miniflix-dev
```

Check pods:

```bash
kubectl get pods -n miniflix
```

Check ingress:

```bash
kubectl get ingress -n miniflix
```

Test API:

```bash
curl http://13.219.139.230/api/movies
```

### Phase 2 Screenshots

Saved in:

```text
docs/screenshots/phase-2/
```

Example files:

```text
01-argocd-synced-healthy-sha.png
02-miniflix-pods-running.png
03-ingress-routing.png
04-ingress-rewrite-proof.png
05-api-movies-json.png
06-ui-hero-tiles-branded.png
07-ec2-instance-details.png
08-argocd-ui-tree.png
09-full-app-details.png
```

---

# 📊 Phase 3 — Observability

Monitoring was added to observe cluster health and resource usage.

## Monitoring Stack

- Prometheus
- Grafana
- kube-prometheus-stack

## Metrics Monitored

- Pod CPU usage
- Pod memory usage
- Pod restart count
- Node resource utilization

This provides visibility into application behavior and cluster performance.

---

# 🔄 Phase 4 — CI/CD Pipeline

Phase 4 introduces full CI/CD automation.

When developers push code:

```text
Push → GitHub Actions builds containers
     → Images pushed to Docker Hub
     → GitOps manifests updated
     → ArgoCD detects change
     → Kubernetes automatically deploys new version
```

This ensures the cluster state is always synchronized with the Git repository.

---

# ✅ Phase 4 Verification

The CI/CD pipeline was verified end-to-end with the following evidence:

- GitHub Actions workflow completed successfully
- Frontend and catalog images pushed to Docker Hub
- Kustomize image tags updated in the GitOps overlay
- ArgoCD application status: **Synced and Healthy**
- Kubernetes pods running successfully
- Service wiring correctly routes traffic from port 80 to container port 5000
- Public ingress endpoints return live API responses
- MiniFlix frontend loads successfully in the browser

---

# 📸 Phase 4 Screenshots

Saved in:

```text
docs/screenshots/phase-4/
```

Example files:

```text
01-github-actions-success.png
02-kustomization-image-tags.png
03-dockerhub-catalog-tag.png
04-dockerhub-frontend-tag.png
05-argocd-tree.png
06-running-pods.png
07-catalog-service-wiring.png
08-public-ingress-health.png
09-public-ingress-movies.png
10-browser-ui-proof.png
11-ingress-resource.png
```

---

# Repository Structure

```text
apps/
  frontend/
  catalog-service/

k8s/
  base/
  overlays/dev/

argocd/
  applications/

docs/
  screenshots/

.github/workflows/
  miniflix-cicd.yaml
```

---

# 🚀 DevOps Concepts Demonstrated

This project demonstrates:

- GitOps deployment workflows
- Kubernetes application orchestration
- CI/CD container pipelines
- Docker image lifecycle
- Kubernetes ingress networking
- Observability using Prometheus and Grafana
- Cloud deployment on AWS

---

# Future Improvements

Possible next steps:

- Horizontal Pod Autoscaling
- Terraform infrastructure provisioning
- Helm packaging for the application
- Logging stack (EFK or Loki)

---

# 👤 Author

**Adedoyin Ekong**

DevOps / Cloud Engineer  
Specializing in Kubernetes, GitOps, and CI/CD pipelines
````

