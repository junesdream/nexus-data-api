# 🤖 nexus-data-api

A modern, type-safe Data Access Layer built with FastAPI and Prisma ORM. This project demonstrates professional database orchestration and schema management.

## ✨ Features

| Feature | Description |
|---|---|
| ⚡ **FastAPI** | High-performance asynchronous API framework. |
| 🔌 **Prisma ORM** | Next-generation Node.js and TypeScript ORM (Python Client) for type-safe database access. |
| 🗄️ **SQLite** | Lightweight relational database for efficient data persistence. |
| ✅ **Pydantic** | Strict data validation and settings management using Python type annotations. |

## 🛠️ Tech Stack

- 🐍 Python 3.14+
- 🚀 FastAPI
- 🔷 Prisma Client Python
- 🦄 Uvicorn
- ✅ Pydantic

## 🚀 Getting Started

### Prerequisites

- Python installed
- Virtual environment activated

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nexus-data-api.git
   cd nexus-data-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Initialize Prisma and sync database:
   ```bash
   prisma db push
   ```

## ▶️ Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

Navigate to 👉 `http://127.0.0.1:8000/docs`

## 👥 Contributors

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.