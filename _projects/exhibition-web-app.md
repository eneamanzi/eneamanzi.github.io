---
layout: page
title: Exhibition Web App
description: Built a dynamic web application serving as a digital portfolio for displaying multimedia content.
img:
importance: 40
category: Academic
permalink: /projects/exhibition-web-app/
cv_id: exhibition-web-app
toc:
  sidebar: left
---

<!-- Scaffolded from the CV's data (single source of truth) - expand with the
     full write-up below the Summary section. -->

## Summary (from CV)

*Web and Mobile Programming Course Project (A.Y. 2021-2022)*

- Developed the backend with *Node.js/Express* and the frontend with *HTML5*, *CSS3*, *JavaScript/jQuery*.
- Integrated *MongoDB* for document-oriented storage and *AJAX* for asynchronous client-server communication (GET, POST, DELETE).
- Managed source code and collaboration using **Git** and **GitHub**.
- **Key skills:** *Node.js*, *Express*, *MongoDB*, *AJAX*, *REST APIs*, *jQuery*, **Git**.

## Two Roles, Two Experiences

### Visitor (public)

Can browse the painting gallery, open the detail view of each artwork with a full photo and description, and navigate between sections via a shared navigation bar.

### Admin (protected)

Logs in via bcrypt-hashed password authentication and manages artworks directly from the browser: adding new paintings with image upload, editing titles and descriptions, and deleting works with a confirmation prompt. All operations happen without page reload, through asynchronous **AJAX** calls to the server.

## Architecture

The backend is a **Node.js/Express** server that exposes REST routes (GET, POST, PUT, DELETE) and manages user sessions. Painting data - title, description, date, and image path - is stored in **MongoDB** through **Mongoose** schemas. The frontend communicates with the server exclusively via AJAX, building the DOM dynamically from the received data.

```
Browser  →  AJAX GET /getList  →  Express  →  MongoDB  →  JSON response  →  DOM update
```

Image uploads are handled by **Multer**, which saves files on the server and stores the corresponding path in the MongoDB document.

## Technical Highlights

**Authentication and sessions** - login verifies the password using bcrypt and maintains admin state via `express-session`. Admin routes are protected: without an active session, every request is rejected.

**Shared components** - the navbar and footer are separate HTML files, dynamically loaded via jQuery across all pages, avoiding code duplication.

**Performance** - static images are compressed up to 75% of their original size, and scripts are placed at the bottom of the body to avoid blocking rendering. All pages are validated through the W3C Validator.

## Tech Stack

- **Backend:** Node.js, Express, express-session, Multer, bcrypt, Mongoose
- **Database:** MongoDB
- **Frontend:** HTML5, CSS3, JavaScript, AJAX, jQuery, Bootstrap
- **Version control:** Git / GitHub
