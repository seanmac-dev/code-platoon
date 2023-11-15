\COPY UserAccounts(username, user_password, last_login_date) FROM './users.csv' CSV HEADER

\COPY UserProfiles(user_id, profile_photo_url, about_me, personal_quote) FROM './profiles.csv' DELIMITER ';' CSV HEADER