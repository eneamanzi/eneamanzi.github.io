---
layout: page
title: Client FTP compatibile con FileZilla Server
description: Client FTP scritto in C che implementa i principali comandi del protocollo FTP per interagire con FileZilla Server. Progetto universitario di reti.
img: assets/img/ftp-client.png
importance: 2
category: University
page_id: ftp-client
lang: it
permalink: /projects/ftp-client/
---

# Client FTP in C

Client FTP scritto in C, progettato per comunicare con **FileZilla Server** seguendo le specifiche del protocollo FTP. Realizzato come progetto universitario per il corso di Reti di Calcolatori (A.A. 2022-2023), implementa i comandi fondamentali per gestire sessioni, file e directory in modo conforme allo standard.

## Comandi supportati

Il client copre le operazioni essenziali di una sessione FTP, dall'autenticazione alla gestione del filesystem remoto.

### Sessione e autenticazione

| Comando | Funzione |
|---------|----------|
| `USER` | Invio username |
| `PASS` | Invio password |
| `QUIT` | Chiusura della connessione |

### Modalità di trasferimento

| Comando | Funzione |
|---------|----------|
| `PORT` | Modalità attiva - specifica la porta dati lato client |
| `PASV` | Modalità passiva - il server apre la porta dati |
| `TYPE` | Tipo di trasferimento (ASCII `A` / Binario `I`) |

### Operazioni su file e directory

| Comando | Funzione |
|---------|----------|
| `LIST` | Elenco contenuto della directory corrente |
| `PWD` | Visualizza la directory di lavoro |
| `CWD` | Cambia directory |
| `RETR` | Scarica un file dal server |
| `STOR` | Carica un file sul server |
| `DELE` | Elimina un file |
| `MKD` | Crea una nuova directory |
| `RMD` | Rimuove una directory |

## Aspetti tecnici rilevanti

**Socket programming** - la comunicazione avviene tramite connessioni TCP a basso livello, gestendo separatamente il canale di controllo (comandi) e il canale dati (trasferimento file), come richiesto dal protocollo FTP.

**Modalità attiva e passiva** - entrambe le modalità di trasferimento sono supportate nativamente: in modalità attiva (PORT) il client apre la porta dati; in modalità passiva (PASV) lo fa il server, rendendo il client compatibile con diverse configurazioni di rete.

**Esecuzione multi-thread** - l'architettura supporta la gestione concorrente delle sessioni, garantendo un trasferimento file affidabile senza bloccare la connessione di controllo.

## Stack tecnologico

- **Linguaggio:** C
- **Ambiente:** Unix-like (Linux / macOS)
- **Compilazione:** GCC + Makefile
- **Protocollo:** FTP - RFC 959

[Vedi su GitHub](https://github.com/eneamanzi/FTP-Filezilla-Client)