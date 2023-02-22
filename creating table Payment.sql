 use dexter;
 CREATE TABLE Payment (
  Payment_ID INT PRIMARY KEY auto_increment,
  station_ID INT,
  passenger_ID INT,
  source_ID INT,
  train_ID INT,
  Seat_no INT NOT NULL,
  fare INT,
  payment_status VARCHAR(100),
  ticket_generated timestamp default CURRENT_TIMESTAMP,
  FOREIGN KEY (station_ID) REFERENCES Station (station_ID),
  FOREIGN KEY (passenger_ID) REFERENCES Passenger (passenger_ID),
  FOREIGN KEY (train_ID) REFERENCES train (train_ID)
);
