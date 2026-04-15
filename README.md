# QR Scanner Backend

A FastAPI backend that receives live camera frames and scans them for QR codes.

## Project Structure

- `app/main.py` — App entry point
- `app/routes/scan.py` — API routes
- `app/core/config.py` — Environment settings
- `app/core/exceptions.py` — Global error handling
- `app/services/` — Image validation, QR detection, URL resolution
- `app/db/` — Database models and connection

## Setup Instructions

### 1. Clone the repository
git clone <your-repo-link>
cd qr-scanner-backend

### 2. Install dependencies
pip install -r requirements.txt

### 3. Create your .env file
Copy the .env file and fill in the values

### 4. Run the server
uvicorn app.main:app --reload

## API Routes

| Method | Route         | Description                        |
|--------|---------------|------------------------------------|
| GET    | /health       | Check if server is running         |
| POST   | /scan-frame   | Send a JPEG frame to scan for QR   |

## Testing

Once the server is running, visit:
http://127.0.0.1:8000/docs