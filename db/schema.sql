CREATE TABLE IF NOT EXISTS users (

    username VARCHAR ( 25 ) UNIQUE NOT NULL PRIMARY KEY,

    password VARCHAR ( 20 ) NOT NULL,

    statusmessage VARCHAR ( 50 )

);


CREATE TABLE IF NOT EXISTS cards (

    card_id serial UNIQUE NOT NULL PRIMARY KEY,

    card_name VARCHAR (255) NOT NULL,

    card_number VARCHAR (255),

    pokemon_type VARCHAR (255),

    pokemon_stage VARCHAR (255), 

    card_type VARCHAR (255) NOT NULL,

    release VARCHAR (255) NOT NULL,

    price VARCHAR (255) NOT NULL,

    rarity VARCHAR (255),

    image_name VARCHAR (255)

);

CREATE TABLE IF NOT EXISTS decks (

    username VARCHAR (255) NOT NULL,

    deck_id serial PRIMARY KEY UNIQUE NOT NULL,

    deck_name VARCHAR ( 255 ) NOT NULL,

    FOREIGN KEY (username) 
        REFERENCES users (username),
    
    deck_price VARCHAR ( 255 ) 
);

CREATE TABLE IF NOT EXISTS user_cards (
    
    username VARCHAR ( 255 ) NOT NULL,

    deck_id serial NOT NULL,

    card_id serial NOT NULL,

    FOREIGN KEY (username) 
        REFERENCES users (username),

    FOREIGN KEY (deck_id)
        REFERENCES decks (deck_id),

    FOREIGN KEY (card_id)
        REFERENCES cards (card_id)

);