from fastapi import APIRouter

router = APIRouter(prefix="/invoices", tags=["invoices"])


@router.post("/upload")
async def upload_invoice():
    return {"invoice_id": "inv_001", "status": "uploaded"}


@router.get("/{invoice_id}/risk")
async def get_risk(invoice_id: str):
    return {"invoice_id": invoice_id, "risk_score": 0.42, "risk_level": "medium"}


@router.post("/{invoice_id}/approve")
async def approve_invoice(invoice_id: str):
    return {"invoice_id": invoice_id, "status": "approved"}