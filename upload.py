import sqlite3
import os

pwd = os.getcwd()
path = "/usr/share/wallpapers/garuda-wallpapers"
os.chdir(path)
files = []

for file in os.listdir():
    files.append(file)

os.chdir(pwd)
conn = sqlite3.connect("images.db")
cur = conn.cursor()

insertQuery = "INSERT INTO Image VALUES (?, ?)"

for file in files:
    with open(f"{path}/{file}", "rb") as f:
        content = f.read()
        f.close()
    cur.execute(insertQuery, (file, content))

conn.commit()
conn.close()
