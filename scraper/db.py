import psycopg2
from datetime import datetime


def get_connection():
    return psycopg2.connect(
        dbname="yc_intelligence",
        user="postgres",
        password="postgres123",
        host="localhost",
        port="5432"
    )


def insert_company(conn, yc_id, name, domain):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO companies
        (yc_company_id, name, domain, first_seen_at, last_seen_at, is_active)
        VALUES (%s, %s, %s, %s, %s, true)
        RETURNING id
    """, (
        yc_id,
        name,
        domain,
        datetime.utcnow(),
        datetime.utcnow(),
    ))
    return cur.fetchone()[0]
