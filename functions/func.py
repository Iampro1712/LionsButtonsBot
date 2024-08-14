import sqlite3
from config import path_db, path_db_ky

def mk_queries(query):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    #conn.commit()
    conn.close()
    
    return rows

def validacion_input(channel_id, link_channel, name_channel, caption):
    
    ch_id = mk_queries(f"SELECT channel_id FROM UsersBotonera WHERE channel_id = {channel_id}")
    if ch_id:
        print("Ya existe un registro con este channel_id.")
        return False
    
    link_ch = mk_queries(f"SELECT * FROM UsersBotonera WHERE link_channel = '{link_channel}'")
    if link_ch:
        print("Ya existe un registro con este link_channel.")
        return False
    
    name_ch = mk_queries(f"SELECT * FROM UsersBotonera WHERE name_channel = '{name_channel}'")
    if name_ch:
        print("Ya existe un registro con este name_channel.")
        return False
    
    cap = mk_queries(f"SELECT * FROM UsersBotonera WHERE caption = '{caption}'")
    if cap:
        print("Ya existe un registro con este caption.")
        return False
    
    return True

def insert_user(owner_id, channel_id, link_channel, name_channel, caption, suscribers, fecha_reg):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO UsersBotonera (owner_id, channel_id, link_channel, name_channel, caption, suscribers, fecha_reg)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (owner_id, channel_id, link_channel, name_channel, caption, suscribers, fecha_reg))
    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UsersBotonera (
            owner_id INTEGER,
            channel_id INTEGER,
            link_channel TEXT,
            name_channel TEXT,
            caption TEXT,
            suscribers INTEGER,
            fecha_reg TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_table_ky():
    conn = connect_db2()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ConfigBotonera (
            img_link TEXT,
            caption TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_info_db():
    try:
    # Conectar a la base de datos
        cnx = sqlite3.connect(path_db)

        # Crear un cursor
        cursor = cnx.cursor()
        # # Deshabilitar la restriccion de llave primaria
        # cursor.execute("SET @@sql_require_primary_key = 0")
        # Almacena y ejecuta la query
        #query_insert = """INSERT INTO Users (username, first_name, usos_bin, id_tlg) VALUES (%s, %s, %s, %s);"""
        #query_insertVAl=("OneGuy", "551658596","OneGuy","0" )

        #cursor.execute(query_insert, query_insertVAl)
        #cnx.commit()

        query = """SELECT * FROM UsersBotonera;"""
        cursor.execute(query)

        # Recupera los resultados
        rows = cursor.fetchall()

        # Procesa las filas
        # for row in rows:
        #     print(row)
        #     #print("2")
        # Cerrar el cursor y la conexion
        cursor.close()
        cnx.close()

    except sqlite3.Error as e:
        print("Error al conectar a la base de datos", e)

    return rows

def connect_db():
    return sqlite3.connect(path_db)

def connect_db2():
    return sqlite3.connect(path_db_ky)