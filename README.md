````markdown
# MiniFlix 🎬 (Netflix-Style MVP) — Kubernetes + GitOps

MiniFlix is a small “Netflix-style” web app (UI + Catalog API) deployed on Kubernetes using **GitOps with Argo CD**.

This repo is built in phases:

- **Phase 1:** Set up the GitOps platform (Argo CD + Ingress) and prove deployments work
- **Phase 2:** Deploy the MiniFlix MVP (branded UI + API) on AWS using lightweight Kubernetes (k3s)

---

## What you can do in the app

- Open a Netflix-style UI (rows + tiles)
- Search titles (simple search)
- Call the API: `/api/movies` returns movie data (JSON)

---

## Tech used (simple list)

- Kubernetes: **k3s**
- GitOps: **Argo CD**
- Ingress: **NGINX Ingress**
- Frontend: HTML + Tailwind (served by Nginx)
- Backend: FastAPI (Catalog API)

---

# Phase 1 — Platform Setup (GitOps Foundation)

## Goal

Make deployments automatic using GitOps:

✅ Push code/manifests to Git → Argo CD syncs → Kubernetes updates

## What was done

- Created a Kubernetes environment (started locally with Kind)
- Installed NGINX Ingress (gives the cluster a “front door”)
- Installed Argo CD (GitOps tool)
- Deployed a simple test app to confirm everything works end-to-end

## Phase 1 screenshots

Saved in:

- `docs/screenshots/phase-1/`

---

# Phase 2 — MiniFlix MVP (UI + API)

## Goal

Replace the Phase 1 test app with a real MVP:

- MiniFlix UI (branded with “by Adedoyin Ekong”)
- Catalog API (FastAPI)
- Ingress routes:
  - `/` → frontend
  - `/api/*` → API

## Why Phase 2 runs on AWS

Local laptop resources (8GB RAM) struggled with Kind + Docker + ArgoCD, so Phase 2 runs on AWS using:

- **1 EC2 instance**
- **k3s (lightweight Kubernetes)**

This keeps Kubernetes real, stable, and cost-friendly compared to EKS.

---

## Quick checks (Phase 2)

### ArgoCD status

```bash
kubectl get app -n argocd miniflix-dev -o wide
````

### Pods

```bash
kubectl get pods -n miniflix
```

### Ingress

```bash
kubectl get ingress -n miniflix
```

### Ingress rewrite proof (shows `/api/*` → backend paths)

```bash
kubectl get ingress -n miniflix miniflix-ingress -o yaml | sed -n '1,80p'
```

### API

```bash
curl -s -H "Host: miniflix.local" http://127.0.0.1/api/movies | head
```

---

## Phase 2 screenshots

Saved in:

* `docs/screenshots/phase-2/`

Suggested file names:

* `01-argocd-synced-healthy-sha.png`
* `02-miniflix-pods-running.png`
* `03-ingress-routing.png`
* `04-ingress-rewrite-proof.png`
* `05-api-movies-json.png`
* `06-ui-hero-tiles-branded.png`
* `07-ec2-instance-details.png`
* `08-argocd-ui-tree.png`
* `09-full-app-details.png`

---

## Folder structure (quick guide)

* `apps/frontend/` → MiniFlix UI
* `apps/catalog-service/` → Catalog API
* `k8s/` → Kubernetes manifests (what ArgoCD deploys)
* `argocd/` → ArgoCD Application config
* `docs/screenshots/` → proof screenshots for each phase

---

# Next (Phase 3 ideas)

* “My List” / “Continue Watching” (stateful feature)
* Observability (Grafana / Prometheus or Loki)
* CI pipeline for linting + deployment checks

---

## Author

Built by **Adedoyin Ekong**

```
```


