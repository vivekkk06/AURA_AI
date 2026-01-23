from fastapi import APIRouter, Depends, Body
from core.dependencies import get_current_user
from .service import search_memory, get_dashboard_data

router = APIRouter(prefix="/memory", tags=["Memory"])


@router.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return get_dashboard_data(user["sub"])


@router.post("/search")
def search(
    data: dict = Body(...),
    user=Depends(get_current_user)
):
    query = data.get("query", "")
    results = search_memory(user["sub"], query)
    return {"results": results}
