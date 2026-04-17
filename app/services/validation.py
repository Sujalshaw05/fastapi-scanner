from fastapi import UploadFile,HTTPException
import numpy as np
import cv2

# Max size = 10MB
MAX_FILE_SIZE = 10 * 1024 * 1024


async def validate_and_process_image(file: UploadFile):
    # 1 Check file type
    acceptable_type=["image/jpeg","image/jpg","image/png"]
    if file.content_type not in acceptable_type:
        raise HTTPException(status_code=401, detail="please put jpg,png or jpeg")

    # 2 Read file 
    contents = await file.read()

    # 3 Check file size
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=401, detail=f"File size must be lower than {(MAX_FILE_SIZE/1024)/1024} MB")

    # 4 Convert bytes -> numpy array
    np_arr = np.frombuffer(contents, np.uint8)

    # 5 Decode -> OpenCV image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # 6 Check corrupted image
    if img is None:
        raise HTTPException(status_code=401, detail="file may be couruupted")

    # 7 Check image size
    height, width = img.shape[:2]
    if height < 5 or width < 5:
        raise HTTPException(status_code=401, detail="file size too small")

    # Valid image -> return to next stage
    return img

