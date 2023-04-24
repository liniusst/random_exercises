import sqlite3

conn = sqlite3.connect("databases/task_two_database.db")
c = conn.cursor()

# with conn:
#     c.execute("DROP TABLE paskaitos")

with conn:
    c.execute(
        """CREATE TABLE IF NOT EXISTS
    paskaitos (
    pavadinimas text,
    destytojas text,
    trukme integer
    )"""
    )

# with conn:
#     c.execute(
#         "INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80), ('Java', 'Tomas', 80)"
#     )

with conn:
    c.execute("SELECT pavadinimas from paskaitos WHERE trukme > 50")
    for paskaita in c.fetchall():
        for name in paskaita:
            print(name)

with conn:
    c.execute(
        "UPDATE paskaitos SET pavadinimas = 'Python programavimas' where pavadinimas = 'Python'"
    )

with conn:
    c.execute("SELECT pavadinimas FROM paskaitos where destytojas = 'Tomas'")
    for paskaita in c.fetchall():
        for paskaitos_pavadinimas in paskaita:
            print(f"Tomas moko: {paskaitos_pavadinimas}")

with conn:
    c.execute("SELECT * FROM paskaitos")
    print(c.fetchall())
