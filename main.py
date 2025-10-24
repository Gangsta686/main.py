import sqlite3

conn = sqlite3.connect(":memory:")  # База в оперативной памяти (не сохраняется после выхода)
conn.execute("""
    CREATE TABLE g (id INTEGER PRIMARY KEY, s TEXT, subj TEXT, gr TEXT)
""")

while True:
    print("\n1-Добавить 2-Показать 3-Изменить 4-Удалить 0-Выход")
    c = input("→ ")

    if c == "1":
        conn.execute("INSERT INTO g (s, subj, gr) VALUES (?,?,?)",
                     (input("ФИО: "), input("Предмет: "), input("Оценка: ")))
        conn.commit()
    elif c == "2":
        for r in conn.execute("SELECT * FROM g"): print(r)
    elif c == "3":
        i = input("ID: "); g = input("Новая оценка: ")
        conn.execute("UPDATE g SET gr=? WHERE id=?", (g, i))
        conn.commit()
    elif c == "4":
        conn.execute("DELETE FROM g WHERE id=?", (input("ID: "),))
        conn.commit()
    elif c == "0":
        break