---
layout: page
title: FTP Client and Server
description: Developed a multi-threaded FTP-compliant client-server application in C for file transfer, fully interoperable with FileZilla.
img:
importance: 30
category: Academic
permalink: /projects/ftp-client-server/
cv_id: ftp-client-server
toc:
  sidebar: left
---

<!-- Scaffolded from the CV's data (single source of truth) - expand with the
     full write-up below the Summary section. -->

## Summary (from CV)

*Computer Networks Course Project (A.Y. 2022-2023)*

- Architecture: Multi-threaded server based on **Socket Programming** for concurrent session management.
- Data Modes: Native support for both Active (PORT) and Passive (PASV) data transfer modes.
- Protocol Management: Implemented essential *FTP commands* (e.g., USER, PASS, LIST, RETR, STOR, CWD...)
- **Key skills:** **C**, **socket programming**, **multithreading**, **network protocols**, **FTP**, **Git**.

## Server

A fully functional FTP server, built to be compatible with the FileZilla client.

### Architecture

The project is split into separate modules to keep the codebase readable and maintainable.

```
ftpServer.c   →  entry point, socket setup, accept loop
handlers.c    →  FTP command logic
myLib.c       →  utilities: I/O, parsing, socket wrappers
```

**Concurrency** - the server uses a **multi-process architecture** (`fork`) to handle multiple clients simultaneously: each accepted connection spawns a dedicated child process, keeping sessions fully isolated.

**Dual TCP channels** - following the FTP protocol, the implementation manages two separate TCP connections per session: the control channel (commands and responses) and the data channel (file content and directory listings).

**Error handling** - response codes follow the FTP standard (`2xx`, `3xx`, `4xx`, `5xx`), ensuring compatibility with any RFC-compliant client and providing meaningful feedback during failed transfers or invalid operations.

### Supported Commands

| Command         | Function                           |
| --------------- | ------------------------------------ |
| `USER` / `PASS` | User authentication                |
| `PORT` / `PASV` | Transfer mode selection            |
| `LIST`          | List files and directories         |
| `PWD` / `CWD`   | Filesystem navigation              |
| `RETR` / `STOR` | File download and upload           |
| `MKD` / `RMD`   | Create and remove directories      |
| `DELE`          | Delete a file                      |
| `TYPE`          | Set transfer type (ASCII / Binary) |
| `QUIT`          | Terminate the session              |

## Client

An FTP client designed to communicate with **FileZilla Server** following the FTP protocol specification.

### Supported Commands

The client covers the core operations of an FTP session, from authentication to remote filesystem management.

**Session and Authentication**

| Command | Function             |
| ------- | --------------------- |
| `USER`  | Send username         |
| `PASS`  | Send password         |
| `QUIT`  | Close the connection  |

**Transfer Modes**

| Command | Function                                          |
| ------- | -------------------------------------------------- |
| `PORT`  | Active mode - specifies the client-side data port  |
| `PASV`  | Passive mode - the server opens the data port      |
| `TYPE`  | Transfer type (ASCII `A` / Binary `I`)             |

**File and Directory Operations**

| Command | Function                               |
| ------- | ------------------------------------------ |
| `LIST`  | List contents of the current directory |
| `PWD`   | Print working directory                |
| `CWD`   | Change directory                       |
| `RETR`  | Download a file from the server        |
| `STOR`  | Upload a file to the server             |
| `DELE`  | Delete a file                           |
| `MKD`   | Create a new directory                  |
| `RMD`   | Remove a directory                      |

### Technical Highlights

**Socket programming** - communication is handled through low-level TCP socket connections, managing both the control channel (commands) and the data channel (file transfer) separately, as required by the FTP protocol.

**Active and passive modes** - both transfer modes are natively supported: in active mode (PORT) the client opens the data port; in passive mode (PASV) the server does, making the client compatible with different network configurations.

**Multi-threaded execution** - the architecture supports concurrent session management, allowing reliable file transfer without blocking the control connection.

## Tech Stack

- **Language:** C
- **Environment:** Unix-like (Linux / macOS)
- **Build:** GCC + Makefile
- **Protocol:** FTP - RFC 959

## Repositories

- [FTP Server on GitHub](https://github.com/eneamanzi/FTP-Filezilla)
- [FTP Client on GitHub](https://github.com/eneamanzi/FTP-Filezilla-Client)
