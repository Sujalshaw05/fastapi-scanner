from fastapi import UploadFile
import numpy as np
import cv2

# Max size = 2MB
MAX_FILE_SIZE = 2 * 1024 * 1024


async def validate_and_process_image(file: UploadFile):
    # 1 Check file type
    if file.content_type != "image/jpeg":
        return None

    # 2 Read file 
    contents = await file.read()

    # 3 Check file size
    if len(contents) > MAX_FILE_SIZE:
        return None

    # 4 Convert bytes -> numpy array
    np_arr = np.frombuffer(contents, np.uint8)

    # 5 Decode -> OpenCV image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # 6 Check corrupted image
    if img is None:
        return None

    # 7 Check image size
    height, width = img.shape[:2]
    if height < 50 or width < 50:
        return None

    # Valid image -> return to next stage
    return img

