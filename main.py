from fastapi import FastAPI
import uvicorn

from routers.orders import router as order_router
from routers.contracts import router as contract_router
from extensions.batching import enable_batching

app = FastAPI()
app.include_router(order_router)
app.include_router(contract_router)
enable_batching(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
