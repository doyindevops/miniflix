Paste this **exactly** into `README.md` and save.

# MiniFlix 🎬 — Netflix-Style App with Kubernetes + GitOps

MiniFlix is a small **Netflix-style web application** deployed on Kubernetes using a **GitOps workflow with Argo CD**.

The goal of this project is to demonstrate a **modern DevOps delivery pipeline** where application changes are automatically built, published, and deployed using Git as the single source of truth.

The application includes:

*  A **frontend UI** displaying movie tiles in a Netflix-style layout
*  A **Catalog API** providing movie data
*  A **GitOps deployment pipeline** that automatically updates the cluster when code changes

---

##  Live Demo

**Frontend**

[http://13.219.139.230](http://13.219.139.230)

**API example**

[http://13.219.139.230/api/movies](http://13.219.139.230/api/movies)

**Health check**

[http://13.219.139.230/api/health](http://13.219.139.230/api/health)

---

##  What the App Does

MiniFlix demonstrates a simple streaming-platform style interface.

Users can:

* 🎬 Open a Netflix-style UI
* 🧾 Browse movie tiles
* 🔎 Search titles
* 📡 Fetch movie data through the API

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

## 🛠 Tech Stack

###  Infrastructure

* AWS EC2
* Kubernetes (**k3s**)

###  DevOps

* GitOps deployment with **Argo CD**
* CI pipeline using **GitHub Actions**
* Container registry: **Docker Hub**

###  Application

**Frontend**

* HTML
* Tailwind CSS
* Nginx

**Backend**

* FastAPI

**Networking**

* NGINX Ingress Controller

**Monitoring**

* Prometheus
* Grafana

---

##  Architecture Overview

The deployment pipeline follows a **GitOps model**:

```text
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

##  Phase 1 — GitOps Platform Setup

###  Goal

Build the **GitOps foundation** before deploying the application.

This phase focused on proving that:

```text
Git → ArgoCD → Kubernetes
```

works correctly.

###  What Was Implemented

* Kubernetes environment, initially using **Kind**
* **NGINX Ingress Controller**
* **Argo CD installation**
* GitOps deployment test application

ArgoCD continuously watches the Git repository and automatically applies updates to the cluster.

###  Phase 1 Screenshots

Saved in:

```text
docs/screenshots/phase-1/
```

---

##  Phase 2 — Deploy MiniFlix MVP

###  Goal

Replace the test application with a real service:

* 🎨 MiniFlix UI
* 📦 Catalog API
* 🌐 Ingress routing

###  Deployment Environment

Phase 2 runs on **AWS EC2 using k3s**.

Local laptop resources struggled with:

```text
Kind + Docker + ArgoCD
```

Moving to EC2 allowed a stable Kubernetes environment while keeping costs low.

Infrastructure used:

* 1 EC2 instance
* k3s, a lightweight Kubernetes distribution

###  Routing Configuration

Ingress rules route traffic like this:

```text
/       → MiniFlix frontend
/api/*  → Catalog API
```

Example endpoints:

```text
/api/movies
/api/health
```

###  Quick Verification Commands

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

###  Phase 2 Screenshots

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

##  Phase 3 — Observability

Monitoring was added to observe system health and resource usage.

Stack deployed:

* Prometheus 📈
* Grafana 📊
* kube-prometheus-stack

Metrics monitored:

* Pod CPU usage
* Pod memory usage
* Pod restarts
* Node resource usage

This gives visibility into how the application behaves in the cluster.

---

## 🔄 Phase 4 — CI/CD Pipeline

Phase 4 introduces **full CI/CD automation**.

When developers push code:

```text
Push → GitHub Actions builds containers ⚙️
     → Images pushed to DockerHub 📦
     → GitOps manifests updated 📝
     → ArgoCD detects change 🔄
     → Kubernetes automatically deploys new version ☸️
```

This means the cluster state is always synchronized with the Git repository.

###  Phase 4 Verification

The Phase 4 pipeline was verified end to end with the following evidence:

* GitHub Actions workflow completed successfully
* Frontend and catalog images were pushed to Docker Hub
* Kustomize image tags were updated in the GitOps overlay
* ArgoCD showed the application as **Synced** and **Healthy**
* Kubernetes pods were running successfully
* Service wiring correctly routed traffic from port 80 to container port 5000
* Public ingress endpoints returned live API responses
* The MiniFlix frontend loaded successfully in the browser

### 📸 Phase 4 Screenshots

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

##  Repository Structure

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

##  Key DevOps Concepts Demonstrated

This project demonstrates:

* 🔁 GitOps deployment workflows
* ☸️ Kubernetes application orchestration
* ⚙️ CI/CD container pipelines
* 🐳 Docker image lifecycle
* 🌐 Kubernetes ingress networking
* 📊 Observability with Prometheus and Grafana
* ☁️ Infrastructure deployment on AWS

---

##  Future Improvements

Possible next steps:

*  Horizontal Pod Autoscaling
*  Terraform infrastructure provisioning
*  Helm packaging for the application
*  Logging stack with EFK or Loki

---

##  Author

Built by **Adedoyin Ekong**

DevOps / Cloud Engineer
Specializing in **Kubernetes, GitOps, and CI/CD pipelines**




