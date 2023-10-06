import sqlite3
import uuid

from pprint import pprint

DATA_FILE = "data/data.SAMPLE_343.expression.tsv"
sample_id = DATA_FILE.split(".")[1]


def import_data(cursor):
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if i == 0:
            continue
        row = line.strip().split("\t")
        type = row[0].split("-")[0]
        cursor.execute(
            "INSERT INTO rna (id, sample_id, license_plate, type, read_counts) VALUES (?,?,?,?,?)",
            (str(uuid.uuid4()), sample_id, row[0], type, row[2]),
        )


conn = sqlite3.connect("rna.db")
cursor = conn.cursor()

print("\nCheck if table exists")
query = """PRAGMA table_info(rna);"""
cursor.execute(query)
pprint(cursor.fetchall())

import_data(cursor)
print("\nCheck if data is inserted")
query = """SELECT * FROM rna LIMIT 10;"""
cursor.execute(query)
pprint(cursor.fetchall())

conn.commit()
conn.close()
