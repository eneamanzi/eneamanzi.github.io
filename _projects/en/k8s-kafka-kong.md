---
layout: page
title: IoT Infrastructure on Kubernetes
description: Cloud-native Kubernetes infrastructure for IoT monitoring, built with Apache Kafka KRaft, Kong API Gateway, and MongoDB Time Series Collections.
subtitle: "Kubernetes · Kafka · Kong · A.Y. 2025-2026"
img: assets/img/kubernetes.svg
importance: 1
category: University
page_id: k8s-kafka-kong
lang: en
permalink: /projects/k8s-kafka-kong/
pretty_table: true
toc:
  sidebar: left
---

A cloud-native, event-driven microservices architecture for industrial IoT monitoring, built and deployed on Kubernetes. Course project for *Cloud Computing Technologies* (A.Y. 2025/2026).

## Architecture Overview

The system is organized into three logical namespaces - `kong`, `kafka`, and `metrics` - following a strict **Separation of Concerns** principle. Data flows from edge sensors through an API Gateway, into a persistent streaming layer, and finally into an optimized time-series database.

The event-driven design fully decouples ingestion from processing: if the consumer slows down or goes offline, messages accumulate durably in Kafka and are processed upon recovery - with **zero data loss**.

## Key Components

### Kong API Gateway - Edge Security

Kong acts as the single entry point for all sensor traffic, implementing the **Gateway Offloading** pattern:

- **Authentication:** API Key validation at the edge - invalid requests are rejected before reaching any backend service
- **Rate Limiting:** 5 requests/second per client, returning `429 Too Many Requests` on excess
- **Load Balancing:** Round-robin distribution across Producer replicas

The entire configuration is **Infrastructure as Code** via Kubernetes CRDs - no manual UI, fully reproducible.

### Apache Kafka - Reliable Streaming

Kafka runs in **KRaft mode** (no ZooKeeper), reducing operational complexity and attack surface. Two dedicated topic strategies handle different QoS requirements:

| Topic | Partitions | Compression | Retention | Guarantee |
|---|---|---|---|---|
| `sensor-telemetry` | 3 | LZ4 | 7 days | At-least-once |
| `sensor-alerts` | 2 | - | 30 days | Zero Data Loss (`min.insync.replicas: 2`) |

LZ4 compression reduces JSON network traffic by up to 60% with minimal CPU overhead.

### MongoDB - Time Series Storage

Data is stored using MongoDB's native **Time Series Collections**, which provide:

- Automatic **Zstd compression** (~70% storage reduction on historical data)
- **Clustered indexes** on `timestamp` for efficient range queries
- **TTL auto-expiry** at 30 days (`expireAfterSeconds: 2592000`)

MongoDB is deployed as a **StatefulSet** to ensure stable pod identity and persistent volume reattachment across crashes.

### Python Microservices

Three stateless/stateful services handle the full pipeline:

- **Producer** - Flask REST API; enriches each message with a UUID idempotency token and Kafka topic routing
- **Consumer** - Stateful worker (3 replicas, one per partition); normalizes and persists data to MongoDB
- **Metrics Service** - Exposes 5 REST analytics endpoints (temperature averages by zone, alert breakdown, 7-day activity trend, firmware status)

## Non-Functional Properties

| Property | Implementation |
|---|---|
| **Security** | TLS on port 9093, SASL/SCRAM-SHA-512, Kubernetes Secrets (no hardcoded credentials) |
| **Fault Tolerance** | Kafka as async buffer; consumer crash → messages preserved → zero data loss on recovery |
| **Self-Healing** | Kubernetes restarts crashed pods automatically |
| **Scalability** | HPA configured at 50% CPU threshold; scales Producer 1→4 replicas under load |

[View on GitHub](https://github.com/eneamanzi/k8s-kafka-kong)