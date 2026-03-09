import httpx
from bs4 import BeautifulSoup
import time
from typing import Dict, Any

async def extract_web_data(url: str) -> Dict[str, Any]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    start_fetch = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
    except Exception as e:
        return {"status": "failed", "error": f"Network Error: {str(e)}"}
        
    fetch_time = time.perf_counter() - start_fetch
    start_parse = time.perf_counter()
    
    try:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string.strip() if soup.title and soup.title.string else "No Title"
        # Mengambil 5 paragraf pertama sebagai data inti
        paragraphs = [p.get_text().strip() for p in soup.find_all("p") if p.get_text().strip()]
        
        extracted_data = {
            "title": title,
            "content_preview": " ".join(paragraphs[:5]) if paragraphs else "No Content Found"
        }
    except Exception as e:
        return {"status": "failed", "error": f"Parsing Error: {str(e)}"}

    parse_time = time.perf_counter() - start_parse
    return {
        "status": "success",
        "data": extracted_data,
        "telemetry": {
            "fetch_time_seconds": round(fetch_time, 4),
            "parse_time_seconds": round(parse_time, 4)
        }
    }