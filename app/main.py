from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.routes import scan 
from app.core.exceptions import http_exception_handler, general_exception_handler


# ── 1. Create the app ──────────────────────────────────
app = FastAPI(title="QR Scanner API", version="1.0.0")


# ── 2. Add CORS Middleware ─────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── 3. Register the error handlers ────────────────────
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)


# ── 4. Connect the routes ──────────────────────────────
# app.include_router(scan_router)
app.include_router(scan.router, prefix="/scan", tags=["User"])