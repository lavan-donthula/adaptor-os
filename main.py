from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import uuid

app = FastAPI(title="ONDC Enterprise FMCG Adapter")

class ONDCSearchPayload(BaseModel):
    bap_id: str
    search_term: str

@app.get("/")
def home():
    return {"status": "AdapterOS Engine Online", "location": "New Zealand to India Rails"}

@app.post("/search")
async def handle_ondc_search(payload: ONDCSearchPayload, background_tasks: BackgroundTasks):
    return {
        "status": "ACK",
        "transaction_id": str(uuid.uuid4()),
        "message": f"Search for '{payload.search_term}' parsed via cloud memory cache layer successfully."
    }
