---
layout: page
title: Infrastruttura IoT su Kubernetes
description: Architettura Cloud-Native con Kafka, Kong e MongoDB per il monitoraggio IoT.
img: assets/img/kubernetes.svg
importance: 1
category: University
---

Sviluppo di un'infrastruttura **Kubernetes** cloud-native per l'ingestion e il monitoraggio di dati IoT, con un focus estremo sulla scalabilità e la sicurezza edge-to-core. Progetto realizzato per il corso di *Cloud Computing Technologies* (A.A. 2025/2026).

### Punti Chiave:
* **Architettura a Microservizi:** Basata su **Apache Kafka** in modalità **KRaft** (ZooKeeper-less) per garantire un disaccoppiamento asincrono e "Zero Data Loss".
* **Edge Security & Gateway:** Integrazione di **Kong API Gateway** per centralizzare Autenticazione (API Key), Rate Limiting e Load Balancing.
* **Storage Ottimizzato:** Layer basato su **MongoDB** utilizzando *Time Series Collections* e compressione ibrida (LZ4/Zstd) per massimizzare le performance analitiche.
* **Orchestrazione:** Gestione completa tramite **Helm**, con scalabilità automatica (**HPA**) e gestione avanzata dei segreti (TLS/SASL).

[Vedi il codice su GitHub](https://github.com/eneamanzi/k8s-kafka-kong)