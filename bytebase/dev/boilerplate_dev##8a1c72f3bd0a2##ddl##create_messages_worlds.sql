BEGIN;

-- Running upgrade  -> 8a1c72f3bd0a

CREATE TABLE messages (
    id SERIAL NOT NULL, 
    text VARCHAR(255) NOT NULL, 
    PRIMARY KEY (id)
);

CREATE TABLE worlds (
    world_id VARCHAR(50) NOT NULL, 
    name VARCHAR(50) NOT NULL, 
    PRIMARY KEY (world_id)
);
