# 🚀 Enterprise Data Extractor API

A high-performance, production-ready REST API built with **FastAPI** and **HTTPX**. Designed for developers who need fast, reliable, and asynchronous web data extraction with built-in performance telemetry.



## 🌟 Key Features
* **Asynchronous Engine:** Built on `httpx` and `FastAPI` for non-blocking I/O operations.
* **Performance Telemetry:** Every request returns precise `fetch_time` and `parse_time` headers.
* **Clean Architecture:** Separated concerns (API, Services, Core) for high maintainability.
* **Auto-Documentation:** Interactive Swagger UI and Redoc included out-of-the-box.
* **Defensive Programming:** Robust error handling to prevent 500 Internal Server Errors.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastAPI
* **Parsing:** BeautifulSoup4
* **Client:** HTTPX (Async)
* **Validation:** Pydantic v2

## 🚀 Quick Start
1. Clone the repo: `git clone https://github.com/hizpro/fastapi-data-extractor.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the engine: `uvicorn app.main:app --reload`
4. Access documentation: `http://127.0.0.1:8000/docs`

---
🇮🇩 [Baca Dokumentasi dalam Bahasa Indonesia di sini](./README.ID.md)
