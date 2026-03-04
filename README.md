<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
</p>

<h1 align="center">🕌 Islamina Radio Backend</h1>

<p align="center">
  A FastAPI backend that powers the Quran Radio feature in 
  <a href="https://github.com/Omarsalama2001/islamina_app">Islamina App</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/API-Live-success?style=for-the-badge&logo=vercel"/>
</p>

---

## 📋 Overview

This is the backend service for **Islamina App** 📱
It provides a REST API to fetch and stream **Quran Radio Stations**
from various Islamic channels around the world.

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Get all radio stations |

### Response Example
```json
[
  {
    "name": "إذاعة القرآن الكريم",
    "country": "Egypt 🇪🇬",
    "url": "stream_url"
  },
  {
    "name": "إذاعة القرآن الكريم",
    "country": "Saudi Arabia 🇸🇦",
    "url": "stream_url"
  }
]
```

---

## 🛠️ Tech Stack

| Technology | Usage |
|-----------|-------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) | Programming Language |
| ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white) | REST API Framework |
| ![Uvicorn](https://img.shields.io/badge/Uvicorn-009688?style=flat&logo=gunicorn&logoColor=white) | ASGI Server |
| ![Vercel](https://img.shields.io/badge/Vercel-000000?style=flat&logo=vercel&logoColor=white) | Deployment Platform |

---

## ⚙️ Run Locally

**Step 1:** Clone the repo
```bash
git clone https://github.com/Omarsalama2001/islamina_radio_backend
cd islamina_radio_backend
```

**Step 2:** Install dependencies
```bash
pip install -r requirements.txt
```

**Step 3:** Run the server
```bash
uvicorn main:app --reload
```

**Step 4:** Open in browser
```
http://localhost:8000
```

---

## 📁 Project Structure

```
📦 islamina_radio_backend
 ├── 📄 main.py
 ├── 📄 radio_backend.py
 ├── 📄 requirements.txt
 └── 📄 vercel.json
```

---

## 🔗 Related

> 📱 **Islamina Flutter App:** [islamina_app](https://github.com/Omarsalama2001/islamina_app)

---

## 👨‍💻 Developer

<p align="center">
  <a href="https://github.com/Omarsalama2001">
    <img src="https://img.shields.io/badge/GitHub-Omar_Salama-181717?style=for-the-badge&logo=github"/>
  </a>
</p>
