---
layout: page
title: FTP Client – Compatible with FileZilla Server
description: FTP client written in C implementing the core FTP protocol commands to interact with FileZilla Server. University computer networks project.
subtitle: "C · Computer Networks · A.Y. 2022-2023"
img: assets/img/ftp-client.png
importance: 2
category: University
page_id: ftp-client
lang: en
permalink: /projects/ftp-client/
pretty_table: true
toc:
  sidebar: left
---

An FTP client written in C, designed to communicate with **FileZilla Server** following the FTP protocol specification. Built as a university project for a Computer Networks course (A.Y. 2022-2023), it implements the essential commands for managing sessions, files, and directories in a standard-compliant way.

## Supported Commands

The client covers the core operations of an FTP session, from authentication to remote filesystem management.

### Session and Authentication

| Command | Function |
|---------|----------|
| `USER` | Send username |
| `PASS` | Send password |
| `QUIT` | Close the connection |

### Transfer Modes

| Command | Function |
|---------|----------|
| `PORT` | Active mode - specifies the client-side data port |
| `PASV` | Passive mode - the server opens the data port |
| `TYPE` | Transfer type (ASCII `A` / Binary `I`) |

### File and Directory Operations

| Command | Function |
|---------|----------|
| `LIST` | List contents of the current directory |
| `PWD` | Print working directory |
| `CWD` | Change directory |
| `RETR` | Download a file from the server |
| `STOR` | Upload a file to the server |
| `DELE` | Delete a file |
| `MKD` | Create a new directory |
| `RMD` | Remove a directory |

## Technical Highlights

**Socket programming** - communication is handled through low-level TCP socket connections, managing both the control channel (commands) and the data channel (file transfer) separately, as required by the FTP protocol.

**Active and passive modes** - both transfer modes are natively supported: in active mode (PORT) the client opens the data port; in passive mode (PASV) the server does, making the client compatible with different network configurations.

**Multi-threaded execution** - the architecture supports concurrent session management, allowing reliable file transfer without blocking the control connection.

## Tech Stack

- **Language:** C
- **Environment:** Unix-like (Linux / macOS)
- **Build:** GCC + Makefile
- **Protocol:** FTP - RFC 959

[View on GitHub](https://github.com/eneamanzi/FTP-Filezilla-Client)