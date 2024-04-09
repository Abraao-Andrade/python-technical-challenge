from fastapi import APIRouter, HTTPException, Depends
from typing import Union, List
from pydantic import BaseModel

from src.question2 import Orders

orders_instance = Orders()

router = APIRouter(prefix="/orders")


class Request(BaseModel):
    requests: List[int]
    n_max: int


@router.post("/combine_orders", status_code=200)
async def combine_orders(request: Request):
    try:
        num_trips = orders_instance.combine_orders(
            request.requests, request.n_max)
        return {"num_trips": num_trips}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
