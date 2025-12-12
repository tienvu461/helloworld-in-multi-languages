from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pathlib import Path
import json

app = FastAPI(title="HelloWorld FastAPI Example")

HEALTH_FILE = Path(__file__).with_name("health.json")


@app.get("/health")
async def health():
    if not HEALTH_FILE.exists():
        raise HTTPException(status_code=404, detail="health.json not found")
    try:
        with HEALTH_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        # If JSON parsing fails, return 500 with a helpful message
        raise HTTPException(status_code=500, detail=f"Unable to read health.json: {e}")


if __name__ == "__main__":
    # Allow running locally with `python server.py` for quick testing
    import uvicorn

    uvicorn.run("server:app", host="0.0.0.0", port=8080, log_level="info")
