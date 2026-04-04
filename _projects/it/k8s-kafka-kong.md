---
layout: page
title: Infrastruttura IoT su Kubernetes
description: Infrastruttura Kubernetes cloud-native per il monitoraggio IoT, basata su Apache Kafka KRaft, Kong API Gateway e MongoDB Time Series Collections.
subtitle: "Kubernetes · Kafka · Kong · A.A. 2025-2026"
img: assets/img/kubernetes.svg
importance: 1
category: University
page_id: k8s-kafka-kong
lang: it
permalink: /projects/k8s-kafka-kong/
pretty_table: true
toc:
  sidebar: left
---

Un'architettura a microservizi **event-driven** e cloud-native per il monitoraggio IoT industriale, progettata e distribuita su Kubernetes. Progetto per il corso di *Cloud Computing Technologies* (A.A. 2025/2026).

## Panoramica dell'Architettura

Il sistema è suddiviso in tre namespace logici - `kong`, `kafka` e `metrics` - seguendo il principio di **Separation of Concerns**. I dati transitano dai sensori edge attraverso un API Gateway, in uno strato di streaming persistente, fino a un database time-series ottimizzato.

Il design event-driven disaccoppia completamente l'ingestione dal processamento: se il consumer rallenta o va offline, i messaggi si accumulano durevolmente in Kafka e vengono elaborati al riavvio - con **zero data loss**.

## Componenti Principali

### Kong API Gateway - Sicurezza all'Edge

Kong funge da unico punto di ingresso per tutto il traffico dei sensori, implementando il pattern di **Gateway Offloading**:

- **Autenticazione:** validazione dell'API Key all'edge - le richieste non valide vengono bloccate prima di raggiungere qualsiasi servizio backend
- **Rate Limiting:** 5 richieste al secondo per client, con risposta `429 Too Many Requests` in caso di superamento
- **Load Balancing:** distribuzione round-robin tra le repliche del Producer

L'intera configurazione è **Infrastructure as Code** tramite CRD Kubernetes - nessuna UI manuale, completamente riproducibile.

### Apache Kafka - Streaming Affidabile

Kafka gira in modalità **KRaft** (senza ZooKeeper), riducendo la complessità operativa e la superficie di attacco. Due strategie di topic distinte gestiscono requisiti di QoS differenziati:

| Topic | Partizioni | Compressione | Retention | Garanzia |
|---|---|---|---|---|
| `sensor-telemetry` | 3 | LZ4 | 7 giorni | At-least-once |
| `sensor-alerts` | 2 | - | 30 giorni | Zero Data Loss (`min.insync.replicas: 2`) |

La compressione LZ4 riduce il traffico di rete JSON fino al 60% con un overhead CPU minimo.

### MongoDB - Storage Time Series

I dati vengono salvati utilizzando le **Time Series Collections** native di MongoDB, che offrono:

- **Compressione Zstd** automatica (~70% di risparmio su disco per i dati storici)
- **Indici clustered** sul campo `timestamp` per query su range temporali efficienti
- **TTL automatico** a 30 giorni (`expireAfterSeconds: 2592000`)

MongoDB è deployato come **StatefulSet** per garantire un'identità stabile al pod e la riacquisizione del volume persistente dopo un crash.

### Microservizi Python

Tre servizi gestiscono l'intera pipeline:

- **Producer** - Flask REST API stateless; arricchisce ogni messaggio con un UUID come idempotency token e instrada i dati sul topic Kafka corretto
- **Consumer** - Worker stateful (3 repliche, una per partizione); normalizza e persiste i dati su MongoDB
- **Metrics Service** - Espone 5 endpoint REST di analytics (media temperatura per zona, breakdown allarmi, trend attività 7 giorni, stato firmware)

## Proprietà Non Funzionali

| Proprietà | Implementazione |
|---|---|
| **Sicurezza** | TLS su porta 9093, SASL/SCRAM-SHA-512, Kubernetes Secrets (nessuna credenziale hardcoded) |
| **Fault Tolerance** | Kafka come buffer asincrono; crash del consumer → messaggi preservati → zero data loss al riavvio |
| **Self-Healing** | Kubernetes riavvia automaticamente i pod in crash |
| **Scalabilità** | HPA configurato con soglia CPU al 50%; scala il Producer da 1 a 4 repliche sotto carico |

[Vedi il codice su GitHub](https://github.com/eneamanzi/k8s-kafka-kong)