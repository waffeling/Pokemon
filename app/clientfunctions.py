import psycopg2

def createconn():
    return psycopg2.connect("dbname=postgres user=postgres password=pass123 host=postgres")

def execute_select_many(query:str):
    conn = createconn()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

    if cur.rowcount != 0:
        response = cur.fetchall()
        cur.close()
        conn.close()
        return response
    
    cur.close()
    conn.close()
    return None

def execute_select_one(query:str):
    conn = createconn()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    
    if cur.rowcount != 0:
        response = cur.fetchone()
        cur.close()
        conn.close()
        return response
    
    cur.close()
    conn.close()
    return None

def execute_ins_upd(query:str):
    conn = createconn()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()

def get_token_by_user(user:str):
    sqlcommand = "SELECT token FROM tokens WHERE username = '{username}'"
    return execute_select_one(sqlcommand.format(username = user))

def token_auth(user:str, token:str):
    tokenval = get_token_by_user(user)
    if tokenval is None:
        return False
    if tokenval[0] != token:
        return False
    
    return True