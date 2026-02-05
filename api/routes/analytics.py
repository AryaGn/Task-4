from fastapi import APIRouter
from ..db import get_connection

router = APIRouter()

@router.get("/")
def analytics():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT batch, COUNT(*)
        FROM company_snapshots
        GROUP BY batch
    """)

    rows = cur.fetchall()

    return {
        "companies_per_batch": [
            {"batch": r[0], "count": r[1]}
            for r in rows
        ]
    }
