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

Before starting, ensure you have the following installed:

| Tool | Version Used |
|------|-------------|
| Docker Desktop | 28.0.4 |
| minikube | v1.38.1 |
| kubectl | v1.36.0 |
| Helm | v4.1.4 |

## Step 1 — Start Your Kubernetes Cluster

```bash
minikube start --memory=4096 --cpus=2 --driver=docker
minikube status
kubectl get nodes