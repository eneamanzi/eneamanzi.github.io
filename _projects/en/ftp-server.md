---
layout: page
title: FTP Server in C – FileZilla Compatible
description: FTP server written in C with active and passive mode support, user authentication, and directory management. University computer networks project.
img: assets/img/ftp.png
importance: 2
category: University
page_id: ftp-server
lang: en
permalink: /projects/ftp-server/
---


# FTP Server in C

A fully functional FTP server written in C, built to be compatible with the **FileZilla** client. Developed as part of a Computer Networks course project (A.Y. 2022-2023), it covers the core FTP protocol operations defined in [RFC 959](https://www.rfc-editor.org/rfc/rfc959).

## Key Features

The server handles the full lifecycle of an FTP session: from user authentication to file transfer and remote filesystem navigation.

### Data Transfer

Both standard protocol transfer modes are supported:

- **Active mode (PORT)** - the client opens the data port and the server connects to it
- **Passive mode (PASV)** - the server opens the data port and waits for the client connection

### Supported Commands

| Command | Function |
|---------|----------|
| `USER` / `PASS` | User authentication |
| `PORT` / `PASV` | Transfer mode selection |
| `LIST` | List files and directories |
| `PWD` / `CWD` | Filesystem navigation |
| `RETR` / `STOR` | File download and upload |
| `MKD` / `RMD` | Create and remove directories |
| `DELE` | Delete a file |
| `TYPE` | Set transfer type (ASCII / Binary) |
| `QUIT` | Terminate the session |

## Architecture

The project is split into separate modules to keep the codebase readable and maintainable.

```
ftpServer.c   →  entry point, socket setup, accept loop
handlers.c    →  FTP command logic
myLib.c       →  utilities: I/O, parsing, socket wrappers
```

**Concurrency** - the server uses a **multi-process architecture** (`fork`) to handle multiple clients simultaneously: each accepted connection spawns a dedicated child process, keeping sessions fully isolated.

**Dual TCP channels** - following the FTP protocol, the implementation manages two separate TCP connections per session: the control channel (commands and responses) and the data channel (file content and directory listings).

**Error handling** - response codes follow the FTP standard (`2xx`, `3xx`, `4xx`, `5xx`), ensuring compatibility with any RFC-compliant client and providing meaningful feedback during failed transfers or invalid operations.

## Tech Stack

- **Language:** C
- **Environment:** Unix-like (Linux / macOS)
- **Build:** GCC + Makefile
- **Protocol:** FTP - RFC 959

[View on GitHub](https://github.com/eneamanzi/FTP-Filezilla)