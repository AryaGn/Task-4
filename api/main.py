from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "backend working"}

@app.get("/api/companies/")
def companies():
    return {
        "data": [
            {"id": 1, "name": "Stripe"},
            {"id": 2, "name": "Airbnb"},
            {"id": 3, "name": "Coinbase"}
        ]
    }
