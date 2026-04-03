---
layout: page
title: IoT Infrastructure on Kubernetes
description: Cloud-native architecture with Kafka, Kong, and MongoDB for IoT monitoring.
img: assets/img/kubernetes.svg
importance: 1
category: University
---

Development of a cloud-native Kubernetes infrastructure for IoT ingestion and monitoring, with a particular focus on non-functional properties such as scalability, fault tolerance, and edge-to-core security. Course Project (A.Y. 2025/2026).

### Key Features:
* **Microservices Architecture:** Based on **Apache Kafka** in **KRaft** mode (ZooKeeper-less) for asynchronous decoupling and reliable message handling (Zero Data Loss).
* **Edge Security & Gateway:** Integration of **Kong API Gateway** to implement the Gateway Offloading pattern, centralizing Authentication (API Key), Rate Limiting, and Load Balancing at the edge.
* **Optimized Storage:** Storage layer based on **MongoDB** using *Time Series Collections* and hybrid compression (LZ4/Zstd) to maximize storage efficiency and analytical performance.
* **Full Orchestration:** Managed via **Helm**, featuring automatic scalability (**HPA**) and advanced security (Secrets, TLS/SASL).

[View on GitHub](https://github.com/eneamanzi/k8s-kafka-kong)