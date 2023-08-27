import psycopg2
wds_wt = [['To abolish', 'Відміняти, знищувати'],
          ['To approve','Утвердити, одобрити'],
          ['To boast','Гордитися, хвастатись'],
          ['To deliver','Доставляти, поставляти, приносити'],
          ['To descend','Спуститися, сходити'],
          ['To concentrate','Зосередитися'],
          ['To abandon', 'Відмовитись від'],
          ['To escape', 'Покинути, залишити'],
          ['To elaborate', 'Розробляти'],
          ['To construct', 'Будувати, побудувати'],
          ['To distract','Відволікати, відволікати'],
          ['To confuse','Путати, запутати, збити з толку'],
          ['To distribute', 'Розповсюджувати, розподіляти'],
          ['To contribute','Жертвувати, вносити свій вклад'],
          ['To torture','Мучити']]
connection = psycopg2.connect(
    host="localhost",
    database="users",
    user="postgres",
    password="60171320Oleg")
cursor = connection.cursor()
for k in wds_wt:
    postgres_insert_query = """ INSERT INTO my_wds (word, translate) VALUES (%s,%s)"""
    record_to_insert = (k[0], k[1])
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print(count)
    print(count, "Record inserted successfully into mobile table")
    print("Print each row and it's columns values")

connection.close()
cursor.close()

