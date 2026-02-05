from fastapi import APIRouter
from ..db import get_connection

router = APIRouter()

@router.get("/{company_id}")
def get_company(company_id: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, name, domain
        FROM companies
        WHERE id = %s
    """, (company_id,))
    company = cur.fetchone()

    if not company:
        return {"error": "Company not found"}

    cur.execute("""
        SELECT batch, stage, location
        FROM company_snapshots
        WHERE company_id = %s
    """, (company_id,))
    snapshots = cur.fetchall()

    return {
        "company": {
            "id": company[0],
            "name": company[1],
            "domain": company[2],
        },
        "snapshots": [
            {"batch": s[0], "stage": s[1], "location": s[2]}
            for s in snapshots
        ]
    }
