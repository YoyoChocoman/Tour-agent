from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from typing import Dict, Any
import uvicorn

from app.tools import TOOL_RESISTRY
from app.core.config import settings

app = FastAPI()
app.mount("/downloads", StaticFiles(directory=settings.OUTPUT_DIR), name="downloads")

@app.post("/tools/{tool_name}")
async def execute(tool_name: str, payload: Dict[str, Any] = Body(...)):
    try:
        tool = TOOL_RESISTRY[tool_name]
        args = payload.get("arguments", {})

        result = tool(**args)
        print(f"DEBUG: Returning response for '{tool_name}':  {"result": result}")
        return {"result": result}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host = "0.0.0.0", port = 8000, reload=True)