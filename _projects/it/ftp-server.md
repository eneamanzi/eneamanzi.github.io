---
layout: page
title: Server FTP in C compatibile con FileZilla
description: Server FTP scritto in C con supporto alle modalità attiva e passiva, autenticazione utente e gestione directory. Progetto universitario di reti.
img: assets/img/ftp.png
importance: 2
category: University
page_id: ftp-server
lang: it
permalink: /projects/ftp-server/
---

# Server FTP in C

Server FTP funzionante scritto in C, progettato per essere pienamente compatibile con il client **FileZilla**. Realizzato come progetto per il corso di Reti di Calcolatori (A.A. 2022-2023), copre i fondamentali del protocollo FTP definiti nell'[RFC 959](https://www.rfc-editor.org/rfc/rfc959).

## Funzionalità principali

Il server gestisce l'intero ciclo di vita di una sessione FTP: dall'autenticazione al trasferimento file, passando per la navigazione del filesystem remoto.

### Trasferimento dati

Supporta entrambe le modalità previste dal protocollo:

- **Modalità attiva (PORT)** - il client apre la porta dati e il server si connette ad essa
- **Modalità passiva (PASV)** - il server apre la porta dati e attende la connessione del client

### Comandi supportati

| Comando | Funzione |
|---------|----------|
| `USER` / `PASS` | Autenticazione utente |
| `PORT` / `PASV` | Selezione modalità di trasferimento |
| `LIST` | Elenco file e directory |
| `PWD` / `CWD` | Navigazione del filesystem |
| `RETR` / `STOR` | Download e upload di file |
| `MKD` / `RMD` | Creazione e rimozione directory |
| `DELE` | Eliminazione file |
| `TYPE` | Selezione tipo di trasferimento (ASCII / Binario) |
| `QUIT` | Chiusura sessione |

## Architettura

Il progetto è strutturato in moduli separati per mantenere il codice leggibile e manutenibile.

```
ftpServer.c   →  entry point, socket, accept loop
handlers.c    →  logica dei comandi FTP
myLib.c       →  utilità: I/O, parsing, wrapper socket
```

**Concorrenza** - il server adotta un'**architettura multi-processo** (`fork`): ogni connessione accettata genera un processo figlio dedicato, mantenendo le sessioni completamente isolate tra loro.

**Doppio canale TCP** - seguendo le specifiche del protocollo FTP, l'implementazione gestisce due connessioni TCP distinte per sessione: il canale di controllo (comandi e risposte) e il canale dati (contenuto dei file e listing delle directory).

**Gestione degli errori** - i codici di risposta seguono lo standard FTP (`2xx`, `3xx`, `4xx`, `5xx`), garantendo la compatibilità con qualsiasi client conforme all'RFC e fornendo feedback significativo in caso di trasferimenti falliti o operazioni non valide.

## Stack tecnologico

- **Linguaggio:** C
- **Ambiente:** Unix-like (Linux / macOS)
- **Compilazione:** GCC + Makefile
- **Protocollo:** FTP - RFC 959

[Vedi su GitHub](https://github.com/eneamanzi/FTP-Filezilla)