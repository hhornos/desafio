"""
Main
"""
import os
import uvicorn
from app.main import build_api

app = build_api()

if __name__ == '__main__':
    port = int(os.getenv('API_PORT', '5000'))
    uvicorn.run(app, port=port, log_level="info")
