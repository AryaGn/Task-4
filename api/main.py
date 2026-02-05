from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes.companies import router as companies_router
from api.routes.company_detail import router as detail_router
from api.routes.analytics import router as analytics_router

app = FastAPI(title="YC Companies Intelligence API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(companies_router, prefix="/api/companies")
app.include_router(detail_router, prefix="/api/companies")
app.include_router(analytics_router, prefix="/api/analytics")


@app.get("/")
def root():
    return {"status": "API running"}
