from fastapi import FastAPI
from endpoint.produto import router as produto_router
import uvicorn


api = FastAPI()

api.include_router(produto_router, prefix="/produto")

if __name__ == "__main__":
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)
