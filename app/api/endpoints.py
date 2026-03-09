from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from app.services.scraper import extract_web_data

# Membuat router untuk mengelompokkan jalur API
router = APIRouter()

# Schema Validasi Pydantic: Memaksa klien mengirim format yang benar
class ExtractRequest(BaseModel):
    url: HttpUrl  # Ini sihir FastAPI. Jika klien mengirim teks biasa (bukan link web), akan otomatis ditolak!

@router.post("/extract")
async def extract_data(payload: ExtractRequest):
    """
    Endpoint utama untuk mengekstrak data dari URL yang diberikan.
    """
    # Mengubah tipe data HttpUrl kembali menjadi string agar bisa dibaca httpx
    target_url = str(payload.url)
    
    # Menjalankan mesin scraper asynchronous kita
    result = await extract_web_data(target_url)
    
    # Jika gagal (misal web target down atau error)
    if result.get("status") == "failed":
        # Kembalikan HTTP status 400 (Bad Request) beserta pesan errornya
        raise HTTPException(status_code=400, detail=result.get("error"))
        
    # Jika sukses, kembalikan hasil JSON utuh
    return result