use dexter;
CREATE TABLE Passenger (
  passenger_ID INT NOT NULL PRIMARY KEY auto_increment,
  Name VARCHAR(50) NOT NULL,
  CNIC VARCHAR(13) NOT NULL,
  age INT NOT NULL CHECK (age >= 0 AND age <= 150),
  gender VARCHAR(1) NOT NULL CHECK (gender IN ('M', 'F')),
  phone VARCHAR(11) NOT NULL UNIQUE
);
-- alter table Passenger 
-- add unique (phone);