import json
from db import get_connection, insert_company


DATA_FILE = "scraper/data/yc_companies.json"


def main():
    conn = get_connection()
    cur = conn.cursor()

    with open(DATA_FILE, "r") as f:
        companies = json.load(f)

    for company in companies:
        try:
            insert_company(
                conn,
                company["yc_company_id"],
                company["name"],
                company["domain"],
            )
            conn.commit()
            print("Inserted:", company["name"])
        except Exception as e:
            print("Skipped:", company["name"], e)
            conn.rollback()


if __name__ == "__main__":
    main()
