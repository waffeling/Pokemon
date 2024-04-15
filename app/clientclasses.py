from pydantic import BaseModel

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
