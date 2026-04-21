# 🤖 nexus-data-api

A modern, type-safe **Data Access Layer (DAL)** built with FastAPI and Prisma ORM. 
This service acts as the central state-management engine, providing structured and validated database access for distributed AI systems.

[![Python CI](https://github.com/junesdream/nexus-data-api/actions/workflows/ci.yml/badge.svg)](https://github.com/junesdream/nexus-data-api/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![Prisma](https://img.shields.io/badge/ORM-Prisma-2D3748)
![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688)

---

## 🧠 Overview

The Nexus-Data-API is designed to solve the challenge of data persistence in microservice environments. 
By leveraging **Prisma ORM**, it ensures that every database transaction is type-safe, reducing runtime errors and improving developer productivity. It serves as the "Source of Truth" for the entire AI ecosystem.

---

## ✨ Features
| Feature | Description |
|---|---|
| ⚡ **FastAPI Core** | Asynchronous CRUD operations for high-throughput data handling |
| 🔷 **Prisma ORM** | Next-generation type-safe database orchestration and auto-migrations |
| 🔒 **Schema Enforcement** | Strict Pydantic models for request/response validation |
| 🗄️ **Relational Persistence** | Efficient SQLite integration (easily swappable to PostgreSQL/MySQL) |
| 🐳 **Containerized** | Production-ready Docker configuration for seamless deployment |
| 🔁 **Automated CI/CD** | Full GitHub Actions pipeline for linting and deployment checks |

---

## 🛠️ Tech Stack

- 🐍 Python 3.14+
- 🚀 FastAPI
- 🔷 Prisma Client Python
- 🦄 Uvicorn
- ✅ Pydantic

## 🏗️ Architecture

```
[ AI Services ] --> ( REST API )
            ↓
Nexus-Data-API (FastAPI)
            ↓
Prisma Engine (ORM)
            ↓
[ SQLite Database ]
```

- **Type-Safe Layer:** Every query is validated against the Prisma schema.
- **Independence:** The database layer is decoupled from the business logic.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
  pip install -r requirements.txt
```

### 2. Database Synchronization

#### Sync your Prisma schema with the local database:
```
prisma db push
```

### 3. Start the application

```
uvicorn main:app --reload
```

## 📦 Deployment
Docker (recommended)

```
docker build -t nexus-data-api .
docker run -p 8000:8000 nexus-data-api
```
---

## ⚡ Strategic Use Cases

- **Centralized Persistence:** Unified data storage for multiple AI microservices.
- **Rapid Prototyping:** Quick schema iterations with Prisma's declarative language. 
- **Enterprise Readiness:** Clean separation between API logic and database management.

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-idea`)
3. Commit your changes (`git commit -m 'feat: add your idea'`)
4. Push to the branch (`git push origin feature/your-idea`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

JuNe aka RainbowDev (@junesdream)
AI Systems • Software Development • Electronic Music