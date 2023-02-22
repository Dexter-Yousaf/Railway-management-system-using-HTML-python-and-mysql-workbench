use dexter;
CREATE TABLE Schedule (
  Schedule_ID INT NOT NULL UNIQUE PRIMARY KEY auto_increment,
  train_ID INT,
  station_ID INT,
  dep_time TIME,
  arival_time TIME,
  FOREIGN KEY (train_ID) REFERENCES train (train_ID),
  FOREIGN KEY (station_ID) REFERENCES Station (station_ID)
);
