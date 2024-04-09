from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

from src.question1 import Contracts

contracts_instance = Contracts()

router = APIRouter(prefix="/contracts")


class OpenContract(BaseModel):
    id: int
    debt: float


class RenegotiatedContract(BaseModel):
    id: int


class BatchRequest(BaseModel):
    open_contracts: List[OpenContract]
    renegotiated_contracts: List[RenegotiatedContract]
    top_n: int


class BatchResponse(BaseModel):
    top_n_open_contracts: List[int]


@router.post("/get_top_n_open_contracts", response_model=BatchResponse)
async def get_top_n_open_contracts(batch_request: BatchRequest):
    try:
        top_n_open_contracts = contracts_instance.get_top_N_open_contracts(
            batch_request.open_contracts,
            [rc.id for rc in batch_request.renegotiated_contracts],
            batch_request.top_n
        )
        return {"top_n_open_contracts": top_n_open_contracts}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
