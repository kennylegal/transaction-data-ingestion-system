import psycopg2
from main import create_db
from data import updated_trigger
from api import populate_table

if __name__ == "__main__":
    conn = psycopg2.connect(
        database="wallet_project",
        user="admin",
        password="mydbs",
        host="localhost",
        port="5435"
    )
    cur = conn.cursor()
    create_db(cur, conn)
    print("db cREATED")
    populate_table(cur, conn)

    cur.close()
    conn.close()