from fastapi import APIRouter, UploadFile, File,HTTPException
from app.services.qr_decode import qr_decode_
from app.services.url_service import resolve_url
from app.services.validation import validate_and_process_image

router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/scan-frame")
async def scan_frame(file: UploadFile = File(...)):
    
    # Person 2 will add image validation here
    img=await validate_and_process_image(file)
    # Person 3 will add QR detection here
    massage= await qr_decode_(img)
    if not massage:
        raise HTTPException(status_code=402, detail="data in qr not found")
    return {"data": massage}

@router.post("/scan_url_verification_or_search")
async def scan_frameV2(file: UploadFile = File(...)):

 # Person 2 will add image validation here   
    img=await validate_and_process_image(file)
    # Person 3 will add QR detection here
    massage= await qr_decode_(img)
    if not massage:
        raise HTTPException(status_code=402, detail="data in qr not found")
    # Person 4 will add URL resolution and DB saving here

    urlstr=resolve_url(massage)
    return{"url":urlstr}