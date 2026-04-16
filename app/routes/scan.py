from fastapi import APIRouter, UploadFile, File
from app.services.qr_decode import qr_decode_

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/scan-frame")
async def scan_frame(file: UploadFile = File(...)):
    
    # Person 2 will add image validation here
    # Person 3 will add QR detection here
    massage= await qr_decode_(file)
    return massage
    # Person 4 will add URL resolution and DB saving here