# 🧾 Secure OCR-Based REST API Deployment using FastAPI, Docker & NGINX

This project demonstrates a **production-ready deployment pipeline** for a **secure OCR-based REST API** built with **FastAPI**, containerized with **Docker**, and deployed on a **remote Ubuntu Linux server** behind an **NGINX reverse proxy** with **SSL (HTTPS) encryption**.

The system enables users to upload PDFs or image files and automatically extract structured codes or text using Optical Character Recognition (OCR).  
It was designed for **enterprise-grade reliability, security, and maintainability**.

---

## 🚀 Project Overview

### 🔍 Objective
To build and deploy a **secure, scalable, and isolated backend API** that performs OCR-based data extraction and makes it accessible to authorized clients over HTTPS.

### 💡 Core Features
- **OCR-based REST API** built with FastAPI for speed and modularity.  
- **Secure HTTPS communication** using NGINX reverse proxy and Let’s Encrypt SSL certificates.  
- **Dockerized backend** for portability, easy deployment, and environment consistency.  
- **API key authentication** to control and monitor access to the API.  
- **Firewall (UFW)** configuration for network-level protection.  
- **Automated SSL renewal** using Certbot for long-term stability.  
- **Server and container monitoring** to ensure uptime and reliability.  
- **Migration-ready Docker image** hosted under the organization’s Docker Hub for independent management.

---

## 🧠 System Architecture

Client → NGINX Reverse Proxy (443/HTTPS)
↓
FastAPI Docker Container (Port 3000)
↓
OCR Engine
↓
Extracted Data (JSON Response)


- **NGINX** acts as the **entry point** for all external traffic.  
- Requests are securely routed over **HTTPS** to the FastAPI container.  
- The **FastAPI app** handles OCR extraction and returns results.  
- The setup ensures **port isolation**, **security**, and **high availability**.

---

## ⚙️ Tech Stack

| Component | Technology | Purpose |
|------------|-------------|----------|
| **Backend Framework** | FastAPI | High-performance asynchronous API development |
| **Containerization** | Docker | Isolates the app, ensuring reproducibility and portability |
| **Web Server / Proxy** | NGINX | Handles HTTPS, reverse proxy routing, and load management |
| **SSL / HTTPS** | Certbot + Let’s Encrypt | Provides secure encrypted connections |
| **Firewall** | UFW (Uncomplicated Firewall) | Restricts open ports and hardens network access |
| **Operating System** | Ubuntu Linux | Stable and secure production environment |
| **Registry** | Docker Hub | Stores and manages Docker images |
| **OCR Engine** | Tesseract / Custom Parser | Extracts structured data from images/PDFs |

---

## 🧩 Why Each Tool Was Used

### 🐍 **FastAPI**
Chosen for its **speed**, **built-in validation**, and **async support**. Perfect for REST APIs that handle heavy I/O tasks like OCR.

### 🐳 **Docker**
Containerized the backend to:
- Ensure **consistency** across environments.  
- Simplify deployment (no manual dependency setup).  
- Enable **quick migration** and **scaling** via images.

### 🌐 **NGINX Reverse Proxy**
Used to:
- Forward external HTTPS requests to the FastAPI container.  
- Hide internal container ports (e.g., 3000).  
- Serve as a **single secure gateway** to the application.

### 🔒 **HTTPS with Certbot**
Implemented SSL via **Let’s Encrypt (Certbot)** to:
- Encrypt all data in transit.  
- Build client trust and comply with security best practices.  
- Automate certificate renewals using cron jobs.

### 🧱 **UFW Firewall**
Configured to:
- Allow only essential traffic (Ports 22, 80, 443).  
- Block unauthorized access attempts.  
- Strengthen server-side security.

### 📦 **Docker Hub**
Initially, the image was hosted under a personal account, later migrated to the **organization’s Docker Hub** for:
- Ownership independence.  
- Future scalability and accountability.  
- Elimination of personal account dependency.

---

## 🔑 API Security

* Implemented **API key-based authentication** within FastAPI middleware.
* Each request must include a valid API key in headers:

  ```bash
  Authorization: Bearer <API_KEY>
  ```
* Unauthorized or missing keys trigger a **403 Forbidden** response.
* Keys can be rotated or revoked without redeploying the container.

---

## 🧍‍♂️ Ownership and Sustainability

To ensure **full organizational control**:

* Docker images were migrated from a **personal** to a **company** account.
* The deployed container runs on the **server’s local Docker environment**, so even if external accounts are removed, the service remains unaffected.
* This makes the system **self-sustained** and **independent** of developer credentials.

---

## 🛡️ Security Layers Summary

| Layer                    | Implementation          | Purpose                                           |
| ------------------------ | ----------------------- | ------------------------------------------------- |
| **Network Security**     | UFW Firewall            | Restrict unwanted traffic                         |
| **Application Security** | API Key Validation      | Prevent unauthorized API usage                    |
| **Transport Security**   | SSL (HTTPS via Certbot) | Encrypt client-server communication               |
| **Container Security**   | Docker Isolation        | Limit access to OS-level resources                |
| **Reverse Proxy**        | NGINX                   | Hide internal infrastructure from public exposure |

---

* **Automated SSL renewal** ensures HTTPS uptime.
* **Manual restarts and log inspections** maintain reliability.

---

## 🧰 Skills & Concepts Demonstrated

* REST API design and deployment (FastAPI)
* Containerization (Docker)
* DevOps fundamentals (CI/CD readiness, server management)
* Linux administration (Ubuntu)
* Reverse proxy configuration (NGINX)
* Network security (UFW Firewall)
* HTTPS and SSL management (Certbot)
* Cloud deployment and scalability principles
* API authentication and access control
* System monitoring and maintenance

---

## 🏁 Conclusion

This project represents a **real-world production-grade deployment** where backend engineering meets DevOps.
It emphasizes **security**, **automation**, and **maintainability**, ensuring the system remains robust even if the original developer’s credentials or Docker account are no longer available.

> 🔹 The result: A self-sustained, secure, and scalable OCR-based REST API ready for enterprise use.
Further technical and architectural details are confidential as per client policy.

---

## 🧩 Author

**Sakshi Karande, [Ayush Mayekar](https://linkedin.com/in/ayush-mayekar-b9b883284), Afnan Pathan**

---
