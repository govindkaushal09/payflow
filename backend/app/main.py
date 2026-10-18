from fastapi import FastAPI

from app.routers import invoices, payouts

app = FastAPI(title="PayFlow")

app.include_router(invoices.router)
app.include_router(payouts.router)


@app.get("/health")
async def health():
    return {"status": "ok"}