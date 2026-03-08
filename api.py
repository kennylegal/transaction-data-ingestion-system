import requests
import json
import time


url = "https://randomuser.me/api/"
count = 0

def populate_table(cur, conn):
    for i in range(1,20):
        response = requests.get(url)
        result = json.loads(response.text)
        gender = result["results"][0]["gender"]
        username = result["results"][0]["login"]["username"]
        email = result["results"][0]["email"]
        phone = result["results"][0]["phone"]
        age = result["results"][0]["dob"]["age"]
        cur.execute("""
        INSERT INTO users(username, email, phone, gender, age)
        VALUES(%s, %s, %s, %s, %s);
        """, (username, email, phone, gender, age,)
        )
        conn.commit()
        print(f"Done inserting {i} of 20")
        time.sleep(2)