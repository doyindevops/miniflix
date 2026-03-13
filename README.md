MiniFlix 🎬 — Netflix-Style App with Kubernetes + GitOps

MiniFlix is a small Netflix-style web application deployed on Kubernetes using a GitOps workflow with Argo CD.

The goal of this project is to demonstrate a modern DevOps delivery pipeline where application changes are automatically built, published, and deployed using Git as the single source of truth.

The application includes:

A frontend UI displaying movie tiles (Netflix-style layout)

A Catalog API providing movie data

A GitOps deployment pipeline that automatically updates the cluster when code changes

Live Demo

Frontend:

http://13.219.139.230

API example:

http://13.219.139.230/api/movies

Health check:

http://13.219.139.230/api/health
What the App Does

MiniFlix demonstrates a simple streaming-platform style interface.

Users can:

• Open a Netflix-style UI
• Browse movie tiles
• Search titles
• Fetch movie data via the API

Example API response:

[
  {
    "id": 1,
    "title": "Night Shift Lagos",
    "year": 2024,
    "genre": "Drama"
  }
]
Tech Stack
Infrastructure

• AWS EC2
• Kubernetes (k3s)

DevOps

• GitOps deployment with Argo CD
• CI pipeline using GitHub Actions
• Container registry: Docker Hub

Application

Frontend
• HTML
• Tailwind CSS
• Nginx

Backend
• FastAPI

Networking
• NGINX Ingress Controller

Monitoring
• Prometheus + Grafana

Architecture Overview

The deployment pipeline follows a GitOps model.

Developer Push
      ↓
GitHub Actions (CI)
Build Docker Images
      ↓
Push Images → DockerHub
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

Application architecture inside Kubernetes:

Internet
   │
   ▼
NGINX Ingress
   │
   ├── /        → Frontend service
   │
   └── /api/*   → Catalog API service
Phase 1 — GitOps Platform Setup
Goal

Build the GitOps foundation before deploying the application.

This phase focused on proving that:

Git → ArgoCD → Kubernetes

works correctly.

What was implemented

• Kubernetes environment (initially Kind)
• NGINX Ingress controller
• Argo CD installation
• GitOps deployment test application

ArgoCD continuously watches the Git repository and automatically applies updates to the cluster.

Phase 1 Screenshots

Saved in:

docs/screenshots/phase-1/
Phase 2 — Deploy MiniFlix MVP
Goal

Replace the test application with a real service:

• MiniFlix UI
• Catalog API
• Ingress routing

Deployment environment

Phase 2 runs on AWS EC2 using k3s.

Reason:

Local laptop resources struggled with:

Kind + Docker + ArgoCD

Moving to EC2 allowed a stable Kubernetes environment while keeping costs low.

Infrastructure used:

• 1 EC2 instance
• k3s (lightweight Kubernetes)

Routing configuration

Ingress rules route traffic like this:

/       → MiniFlix frontend
/api/*  → Catalog API

Example:

/api/movies
/api/health
Quick verification commands

Check ArgoCD application:

kubectl get app -n argocd miniflix-dev

Check pods:

kubectl get pods -n miniflix

Check ingress:

kubectl get ingress -n miniflix

Test API:

curl http://13.219.139.230/api/movies
Phase 2 Screenshots

Saved in:

docs/screenshots/phase-2/

Example files:

01-argocd-synced-healthy-sha.png
02-miniflix-pods-running.png
03-ingress-routing.png
04-ingress-rewrite-proof.png
05-api-movies-json.png
06-ui-hero-tiles-branded.png
07-ec2-instance-details.png
08-argocd-ui-tree.png
09-full-app-details.png
Phase 3 — Observability

Monitoring was added to observe system health and resource usage.

Stack deployed:

• Prometheus
• Grafana
• kube-prometheus-stack

Metrics monitored:

• Pod CPU usage
• Pod memory usage
• Pod restarts
• Node resource usage

This allows visibility into how the application behaves in the cluster.

Phase 4 — CI/CD Pipeline

Phase 4 introduces full CI/CD automation.

When developers push code:

Push → GitHub Actions builds containers
     → Images pushed to DockerHub
     → GitOps manifests updated
     → ArgoCD detects change
     → Kubernetes automatically deploys new version

This means the cluster state is always synchronized with the Git repository.

Repository Structure
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
Key DevOps Concepts Demonstrated

This project demonstrates:

• GitOps deployment workflows
• Kubernetes application orchestration
• CI/CD container pipelines
• Docker image lifecycle
• Kubernetes ingress networking
• Observability with Prometheus + Grafana
• Infrastructure deployment on AWS

Future Improvements

Possible next steps:

• Horizontal Pod Autoscaling
• Terraform infrastructure provisioning
• Helm packaging for the application
• Logging stack (EFK or Loki)

Author

Built by

Adedoyin Ekong

DevOps / Cloud Engineer
Specializing in Kubernetes, GitOps, and CI/CD pipelines.
