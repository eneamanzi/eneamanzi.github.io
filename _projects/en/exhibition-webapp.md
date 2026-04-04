---
layout: page
title: Art Gallery Exhibition Web App
description: Full-stack web app for managing and showcasing artworks. Node.js/Express backend, MongoDB storage, and a protected admin panel with authentication.
subtitle: "Node.js · MongoDB · A.Y. 2021-2022"
img: assets/img/exhibition-webapp.png
importance: 5
category: University
page_id: exhibition-webapp
lang: en
permalink: /projects/exhibition-webapp/
toc:
  sidebar: left
---

A full-stack web app for managing and displaying a catalog of artworks, developed for the **Web and Mobile Programming** course (A.Y. 2021-2022). The application supports two user roles: a visitor who browses the public gallery, and an admin who manages content through a protected panel.

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