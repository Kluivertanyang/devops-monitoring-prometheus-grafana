# Project 1: Monitoring & Alerting Stack

![Architecture Diagram](./screenshots/architecture.png)

## Problem Statement

Production applications with no observability leave engineering teams blind to failures.
Incidents get discovered by users before engineers. This project builds a complete
monitoring and alerting pipeline using Prometheus, Grafana, and AlertManager on
Kubernetes — so teams detect and respond to incidents before users are impacted.

## Tech Stack

| Tool | Purpose |
|------|---------|
| Flask | Sample application exposing /metrics endpoint |
| Docker | Containerize the Flask application |
| Kubernetes (minikube) | Container orchestration |
| Prometheus | Metrics scraping and storage |
| Grafana | Metrics visualization and dashboards |
| AlertManager | Alert routing and notifications |
| Helm | Kubernetes package manager |

## Prerequisites

| Tool | Version Used |
|------|-------------|
| Docker Desktop | 28.0.4 |
| minikube | v1.38.1 |
| kubectl | v1.36.0 |
| Helm | v4.1.4 |

---

## Step 1 — Start Your Kubernetes Cluster

Start minikube with enough memory and CPU to run the full monitoring stack:

\`\`\`bash
minikube start --memory=4096 --cpus=2 --driver=docker
minikube status
kubectl get nodes
\`\`\`

Expected output:

\`\`\`
NAME       STATUS   ROLES           AGE   VERSION
minikube   Ready    control-plane   2m    v1.35.1
\`\`\`

![Kubernetes cluster running](./screenshots/01-minikube-cluster-running.png)

---

## Step 2 — Clone This Repository

\`\`\`bash
git clone https://github.com/Kluivertanyang/devops-monitoring-prometheus-grafana.git
cd devops-monitoring-prometheus-grafana
\`\`\`

---

## Step 3 — The Flask Application

The Flask app exposes a /metrics endpoint using prometheus-flask-exporter.
Prometheus scrapes this endpoint every 15 seconds. The app includes these routes:

- / — returns app health status
- /api/data — simulates variable response times to generate interesting metrics
- /api/error — randomly returns 500 errors to trigger AlertManager alerts
- /health — used by Kubernetes liveness and readiness probes
- /metrics — scraped by Prometheus automatically

---

## Step 4 — Build and Push the Docker Image

The Dockerfile uses a non-root user for security and layer caching for faster builds.

\`\`\`bash
docker build -t kluivertanyang/flask-monitor-app:v1.0 ./app
docker push kluivertanyang/flask-monitor-app:v1.0
\`\`\`

Test the app runs correctly before deploying to Kubernetes:

\`\`\`bash
docker run -p 5001:5000 kluivertanyang/flask-monitor-app:v1.0
\`\`\`

Visit http://localhost:5001 — expected response:

\`\`\`json
{"service": "flask-monitor-app", "status": "healthy"}
\`\`\`

Visit http://localhost:5001/metrics to confirm Prometheus metrics are exposed.

![Flask app running](./screenshots/04-flask-app-running.png)

![Flask metrics endpoint](./screenshots/05-flask-metrics-endpoint.png)

![DockerHub image pushed](./screenshots/06-dockerhub-image-pushed.png)

---

## Step 5 — Deploy Flask App to Kubernetes
Coming next

## Step 6 — Install Prometheus and Grafana
Coming next

## Step 7 — View Grafana Dashboard
Coming next

## Step 8 — Trigger and View Alerts
Coming next

---

## Challenges and Solutions
To be filled as we encounter real issues

## What I Learned
To be filled at project completion
