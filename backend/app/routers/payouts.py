from fastapi import APIRouter

router = APIRouter(prefix="/payouts", tags=["payouts"])


@router.get("/{payout_id}/status")
async def get_payout_status(payout_id: str):
    return {"payout_id": payout_id, "status": "pending"}