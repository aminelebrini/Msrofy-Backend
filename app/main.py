from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.group import router as group_router
app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(group_router, prefix="/groups", tags=["Groups"])

@app.get("/")
def read_root():
    return {"message": "Msrofy API"}

