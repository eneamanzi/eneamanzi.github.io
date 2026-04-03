---
layout: page
title: FTP Client in C
description: Client multi-threaded conforme al protocollo FTP, interoperabile con FileZilla.
img: assets/img/ftp-client.png
importance: 2
category: University
---

Sviluppo di un'applicazione client conforme allo standard **FTP** realizzata interamente in **C**. Il progetto si focalizza sulla robustezza della comunicazione socket e sulla gestione della concorrenza.

### Caratteristiche Tecniche:
* **Socket Programming:** Gestione diretta delle connessioni TCP per il canale comandi e il canale dati.
* **Modalità Dati:** Supporto nativo sia per la modalità **Attiva (PORT)** che **Passiva (PASV)**.
* **Interoperabilità:** Pienamente compatibile con server standard come FileZilla Server.
* **Multithreading:** Gestione efficiente delle sessioni e dei trasferimenti file in background.

[Vedi il codice su GitHub](https://github.com/eneamanzi/FTP-Filezilla-Client)