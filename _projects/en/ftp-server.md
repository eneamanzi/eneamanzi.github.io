---
layout: page
title: FTP Client & Server
description: TODO Developed a multi-threaded FTP-compliant client-server application in C for file transfer, fully interoperable with FileZilla.
img: assets/img/12.jpg
importance: 1
category: University
---
TODO 

This project involved the design and implementation of a concurrent **FTP Server** and **Client** strictly following the **RFC 959** standard.

### Key Features
* **Architecture:** Developed entirely in **C** using system calls for network communication.
* **Concurrency:** The server is designed to handle multiple clients simultaneously using a **multi-process architecture** (fork).
* **Protocol:** Implements the core commands of the File Transfer Protocol (FTP) as defined in RFC 959.
* **Functionality:** Supports authentication, directory navigation, and file transfer (upload/download).

### Technical Details
The implementation focuses on low-level socket programming, managing TCP connections for both control and data channels, and ensuring robust error handling during file transfers.
