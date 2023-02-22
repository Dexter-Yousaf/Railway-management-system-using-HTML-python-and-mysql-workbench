use dexter;
CREATE TABLE train (
  train_Id int NOT NULL PRIMARY KEY auto_increment,
  name VARCHAR(20) NOT NULL UNIQUE,
  no_ofSeats INTEGER NOT NULL DEFAULT 100
);
