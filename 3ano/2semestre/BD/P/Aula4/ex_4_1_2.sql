CREATE TABLE FlightManager_Flight (
    Number INT NOT NULL,
    Airline VARCHAR(256) NOT NULL,
    PRIMARY KEY (Number)
)
GO

CREATE TABLE FlightManager_Flight_Weekdays (
    Number INT NOT NULL REFERENCES FlightManager_Flight(Number),
    Weekday VARCHAR(16) NOT NULL,
    PRIMARY KEY (Number, Weekday)
)
GO

CREATE TABLE FlightManager_Airport (
    Code VARCHAR(256) NOT NULL,
    City VARCHAR(32) NOT NULL,
    State VARCHAR(32) NOT NULL,
    Name VARCHAR(64) NOT NULL,
    PRIMARY KEY (Code)
)
GO

CREATE TABLE FlightManager_Airplane_Type (
    TypeName VARCHAR(128) NOT NULL,
    MaxSeats INT NOT NULL,
    Company VARCHAR(64) NOT NULL,
    PRIMARY KEY (TypeName)
)
GO

CREATE TABLE FlightManager_Can_Land (
    Code VARCHAR(256) NOT NULL REFERENCES FlightManager_Airport(Code),
    TypeName VARCHAR(128) NOT NULL REFERENCES FlightManager_Airplane_Type(TypeName),
    PRIMARY KEY (Code, TypeName)
)
GO

CREATE TABLE FlightManager_Airplane (
    ID INT NOT NULL,
    TypeName VARCHAR(128) NOT NULL REFERENCES FlightManager_Airplane_Type(TypeName),
    Total_no_of_seats INT NOT NULL,
    PRIMARY KEY (ID)
)
GO

CREATE TABLE FlightManager_Fare (
    Number INT NOT NULL REFERENCES FlightManager_Flight(Number),
    Code VARCHAR(256) NOT NULL,
    Amount INT NOT NULL,
    Restrictions VARCHAR(512) NOT NULL,
    PRIMARY KEY (Number, Code)
)
GO

CREATE TABLE FlightManager_Flight_Leg (
    Number INT NOT NULL REFERENCES FlightManager_Flight(Number),
    Leg_no INT NOT NULL,
    Scheduled_dep_time DATETIME NOT NULL,
    Scheduled_arr_time DATETIME NOT NULL,
    Dep_airport_code VARCHAR(256) NOT NULL REFERENCES FlightManager_Airport(Code),
    Arr_airport_code VARCHAR(256) NOT NULL REFERENCES FlightManager_Airport(Code),
    PRIMARY KEY (Number, Leg_no)
)
GO

CREATE TABLE FlightManager_Leg_Instance (
    Number INT NOT NULL,
    Leg_no INT NOT NULL,
    Date DATE NOT NULL,
    DepTime DATETIME NOT NULL,
    ArrTime DATETIME NOT NULL,
    No_of_avail_seats INT NOT NULL,
    ID INT NOT NULL REFERENCES FlightManager_Airplane(ID),
    PRIMARY KEY (Number, Leg_no, Date),
    FOREIGN KEY (Number, Leg_no) REFERENCES FlightManager_Flight_Leg(Number, Leg_no)
)
GO

CREATE TABLE FlightManager_Reservation (
    Number INT NOT NULL,
    Leg_no INT NOT NULL,
    Date DATE NOT NULL,
    CustomerName VARCHAR(256) NOT NULL,
    CPhone VARCHAR(32) NOT NULL,
    PRIMARY KEY (Number, Leg_no, Date, CustomerName, CPhone),
    FOREIGN KEY (Number, Leg_no, Date) REFERENCES FlightManager_Leg_Instance(Number, Leg_no, Date)
)
GO

CREATE TABLE FlightManager_Seat (
    Number INT NOT NULL,
    Leg_no INT NOT NULL,
    Date DATE NOT NULL,
    Seat_no VARCHAR(16) NOT NULL,
    PRIMARY KEY (Number, Leg_no, Date, Seat_no),
    FOREIGN KEY (Number, Leg_no, Date) REFERENCES FlightManager_Leg_Instance(Number, Leg_no, Date)
)
GO