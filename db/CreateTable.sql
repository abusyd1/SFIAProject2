CREATE TABLE IF NOT EXISTS Player
             (
                          id         INTEGER NOT NULL,
                          Player_position VARCHAR(30) NOT NULL,
                          Player_nationality  VARCHAR(30) NOT NULL,
			  Player_profile VARCHAR(3000), NOT NULL,
                          PRIMARY KEY (id)
);
