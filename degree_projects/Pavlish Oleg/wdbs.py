import psycopg2

def insert_wdb(wordd, tran):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="users",
            user="postgres",
            password="60171320Oleg")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO my_wds (word, translate) VALUES (%s,%s)"""
        record_to_insert = (f'{wordd}', f'{tran}')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except Exception as e:
        (print(e))
    else:
        print(f"PAIR: {wordd} - {tran} was added.")
    finally:
        connection.close()

def insert_udb(id, name, myall_st=0, myall_end=0):
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="users",
            user="postgres",
            password="60171320Oleg")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO users_data (id, name, myall_start, myall_end) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (f'{id}', f'{name}', f'{myall_st}', f'{myall_end}')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except Exception as e:
        (print(e))
    else:
        print(f"PAIR: {id}, {name}, {myall_st}, {myall_end} was added.")
    finally:
        connection.close()

def selector(table='my_wds', id_st=None,id_end=None, username=None, users_id=None, act=None, word_foradd=None):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="60171320Oleg",
                                    host="localhost",
                                    port="5432",
                                    database="users")
        cursor = connection.cursor()
        match table:
            case 'my_wds':
                if act=='add':
                    postgreSQL_select_Query = f"SELECT * FROM {table} WHERE word='{word_foradd}'"
                else:
                    postgreSQL_select_Query = f"SELECT * FROM {table} WHERE id>{id_st} AND id<={id_end}"
            case 'users_data':
                postgreSQL_select_Query = f"SELECT * FROM {table} WHERE id={users_id}"
        cursor.execute(postgreSQL_select_Query)
        words = cursor.fetchall()
    except psycopg2.errors.UndefinedColumn:
        words=[]
        return words
    except Exception as e:
        print(e)
    else:
        return words
    finally:
        connection.close()

def updater(table, id=None, what=None, data=None):
    try:
        connection = psycopg2.connect(user="postgres",
                                    password="60171320Oleg",
                                    host="localhost",
                                    port="5432",
                                    database="users")
        sql = f""" UPDATE {table}
                SET {what} = %s
                WHERE id = %s"""
        cur = connection.cursor()
        cur.execute(sql, (data,id))
        connection.commit()
    except Exception as e:
        (print(e))
    else:
        print(f"Good!")
    finally:
        connection.close()
        cur.close()
#insert_udb(12423511, 'Oleg')
#selector('my_wds', id_st=0, id_end=5)
#updater('users_data',1241, 'name','Vasyl')
