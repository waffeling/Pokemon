from fastapi import FastAPI, Response, status, Request
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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

class card(BaseModel):
    id: str
    name: str
    release:str

class user(BaseModel):
    username: str
    password: str
    statusmessage: str

class deck(BaseModel):
    name: str
    id: str
    user: str
    price: str

class user_card(BaseModel):
    username: str
    card_id: str
    deck_id: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!!"}

@app.post("/add_user_card")
async def add_user_card(user_card: user_card, request:Request, response:Response):

    sqlcommand = "INSERT INTO user_cards(username, card_id, deck_id) VALUES('{username}', '{card_id}', '{deck_id}')"
    execute_ins_upd(sqlcommand.format(username = user_card.username, card_id = user_card.card_id, deck_id = user_card.deck_id))
    return "ok"

@app.post("/create-user")
async def createuse(user: user):
    sqlcommand = "INSERT INTO users(username, password, statusmessage) VALUES('{user}', '{password}', '{statusmessage}')"
    execute_ins_upd(sqlcommand.format(user = user.username, password = user.password, statusmessage = user.statusmessage))
    return "ok"
