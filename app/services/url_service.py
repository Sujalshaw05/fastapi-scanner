# app/services/url_service.py

import re

URL_REGEX = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)

def resolve_url(raw: str) -> str:
    raw = raw.strip()

    if URL_REGEX.match(raw):
        return raw

    encoded = raw.replace(" ", "+")
    return f"https://www.google.com/search?q={encoded}"