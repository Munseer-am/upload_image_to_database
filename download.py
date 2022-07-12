import sqlite3

file = str(input("Enter file name: ")).strip()

conn = sqlite3.connect("images.db")
cur = conn.cursor()

cur.execute(f"SELECT Content FROM IMAGE WHERE FILENAME LIKE '%{file}%'")
images = cur.fetchall()
cur.execute(f"SELECT FILENAME FROM IMAGE WHERE FILENAME LIKE '%{file}%'")
filenames = cur.fetchall()

for filename, image in zip(filenames, images):
    filename = "".join(filename)
    for img in image:
        with open(f"downloads/{filename}", "wb") as f:
            f.write(img)
            f.close()
