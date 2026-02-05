import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="yc_intelligence",
        user="postgres",
        password="postgres123",
        host="localhost",
        port="5432"
    )
