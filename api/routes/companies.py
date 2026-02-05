from fastapi import APIRouter, Query
from typing import Optional
from ..db import get_connection

router = APIRouter()

@router.get("/")
def list_companies(
    page: int = 1,
    limit: int = 10,
    search: Optional[str] = None,
    active: Optional[bool] = None,
):
    conn = get_connection()
    cur = conn.cursor()

    offset = (page - 1) * limit

    query = """
        SELECT id, yc_company_id, name, domain, is_active
        FROM companies
        WHERE 1=1
    """
    params = []

    if search:
        query += " AND (name ILIKE %s OR domain ILIKE %s)"
        params.extend([f"%{search}%", f"%{search}%"])

    if active is not None:
        query += " AND is_active = %s"
        params.append(active)

    query += " ORDER BY id LIMIT %s OFFSET %s"
    params.extend([limit, offset])

    cur.execute(query, params)
    rows = cur.fetchall()

    data = [
        {
            "id": r[0],
            "yc_company_id": r[1],
            "name": r[2],
            "domain": r[3],
            "is_active": r[4],
        }
        for r in rows
    ]

    return {
        "page": page,
        "limit": limit,
        "count": len(data),
        "data": data,
    }
