from fastapi import APIRouter, Response, status, Request
from fastapi.middleware.cors import CORSMiddleware
import app.clientfunctions as clientfunctions
import app.clientclasses as clientclasses


router=APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello!!"}

@router.post("/add_user_card")
async def add_user_card(user_card: clientclasses.user_card, request:Request, response:Response):

    sqlcommand = "INSERT INTO user_cards(username, card_id, deck_id) VALUES('{username}', '{card_id}', '{deck_id}')"
    clientfunctions.execute_ins_upd(sqlcommand.format(username = user_card.username, card_id = user_card.card_id, deck_id = user_card.deck_id))
    return "ok"

@router.post("/create-user")
async def createuse(user: clientclasses.user):
    sqlcommand = "INSERT INTO users(username, password, statusmessage) VALUES('{user}', '{password}', '{statusmessage}')"
    clientfunctions.execute_ins_upd(sqlcommand.format(user = user.username, password = user.password, statusmessage = user.statusmessage))
    return "ok"
