from fastapi import APIRouter, UploadFile, File


router = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "ok"}


@router.post("/scan-frame")
async def scan_frame(file: UploadFile = File(...)):
    # Person 2 will add image validation here
    # Person 3 will add QR detection here
    # Person 4 will add URL resolution and DB saving here
    pass