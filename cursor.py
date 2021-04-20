import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("create table people (name, age)")
who = "Analia"
age = 12
# This is the qmark style:
cur.execute("insert into people values (?, ?)",
            (who, age))
# And this is the named style:
cur.execute("select * from people where name=:who and age=:age",
            {"who": who, "age": age})  # the keys correspond to the placeholders in SQL
print(cur.fetchone())
