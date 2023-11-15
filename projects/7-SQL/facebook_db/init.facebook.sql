create database facebook_db;

\connect facebook_db

CREATE TABLE UserAccounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    user_password VARCHAR(255),
    last_login_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE UserProfiles (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES UserAccounts(id) UNIQUE,
    profile_photo_url VARCHAR(255),
    about_me TEXT,
    personal_quote TEXT
);

CREATE TABLE Posts (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INT REFERENCES UserAccounts(id)
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    content TEXT,
    user_id INT REFERENCES UserAccounts(id),
    post_id INT REFERENCES Posts(id)
);

CREATE TABLE ReactionTypes (
    id SERIAL PRIMARY KEY,
    type VARCHAR(255)
);

CREATE TABLE PostReactions (
    id SERIAL PRIMARY KEY,
    post_id INT REFERENCES Posts(id),
    reaction_id INT REFERENCES ReactionTypes(id),
    user_id INT REFERENCES UserAccounts(id),
    UNIQUE(post_id, user_id) 
);

-- \COPY UserAccounts (id, username, user_password, last_login_date)
-- FROM './users.csv' CSV HEADER