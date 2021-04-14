# Script to populate vehicle registration database
# April 2021, jenr@kea.dk

USE Tjekbil;

INSERT INTO Licenseplate (Number)
    VALUES
    ('AB12345'),
    ('LL56522'),
    ('BD44507'),
    ('BD75631')
;

INSERT INTO Vehicle
(
	LicenseCurrent, Make, Model, Year, Kind
)
VALUES
	('CS15059', 'Vespa', 'Gran luxe', '1961', 'Motorcykel'),
    ('BD44507', 'Kawasaki', 'ER6', '2009', 'Motorcykel'),
	('BD75631', 'VW', 'Golf Sportsvan 1.4 TSI BMT 125 DSG7', '2016', 'Personbil, stationcar, 5 døre'),
	('AB12345', 'Renault', 'Captur dCi 90', '2013', 'Personbil, hatchback, 4 døre')