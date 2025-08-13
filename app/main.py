from fastapi import FastAPI

app = FastAPI(title="GovPay Gateway")

@app.get("/")
async def root():
    return {"message": "Welcome to GovPay Gateway"}