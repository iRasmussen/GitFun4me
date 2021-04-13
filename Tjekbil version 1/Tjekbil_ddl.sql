# Script to create a vehicle registration database
# April 2021, jenr@kea.dk

CREATE DATABASE Tjekbil;
USE Tjekbil;

CREATE TABLE Licenseplate (
    ID INT NOT NULL AUTO_INCREMENT,
    Number VARCHAR(7),
    Status BOOLEAN,
    PRIMARY KEY (ID)
);

CREATE TABLE Vehicle (
    ID INT NOT NULL AUTO_INCREMENT,
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT(4),
    LicenseCurrent VARCHAR(7),
    PRIMARY KEY (ID)
)