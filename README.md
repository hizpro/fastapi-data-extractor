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

## 📊 Production Benchmarks & Telemetry

This extraction engine utilizes a 100% asynchronous architecture (FastAPI + HTTPX) to eliminate I/O blocking and maximize concurrency. 

**Local Hardware Stress Test (50 Concurrent Extraction Tasks):**
* **Success Rate:** 100.0% (Zero dropped connections)
* **Throughput:** ~2.20 Requests/Sec
* **Average Latency:** 7.37 sec/request
* **Base Network Ping:** ~2,105 ms (High-latency residential ISP)

> 💡 **Architect's Note on Scalability:**
> *The benchmark above was executed on local consumer hardware, strictly bottlenecked by a 50 Mbps network with a severe >2,000ms base latency to the target server. Despite this extreme network constraint, the asynchronous engine maintained a **100% success rate** without any CPU blocking.* > 
> *The current limitation is strictly **Network I/O Bound**. When deployed to a standard production cloud environment (e.g., AWS/GCP with a 1 Gbps+ backbone and sub-50ms latency), the throughput is projected to scale linearly, unlocking its true Enterprise-grade RPS potential.*

---
🇮🇩 [Baca Dokumentasi dalam Bahasa Indonesia di sini](./README.ID.md)
