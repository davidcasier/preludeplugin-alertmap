from prewikka.database import SQLScript

print("SQLSCRIPT found!")

class SQLUpdate(SQLScript):
    type = "install" 
    version = "0" 

    def run(self):
        self.query(""" 
DROP TABLE IF EXISTS Alerts;
DROP TABLE IF EXISTS Countries;

CREATE TABLE Countries(
    Code TEXT NOT NULL,
    Name TEXT NULL
);

CREATE TABLE Alerts (
    id INT NOT NULL AUTO_INCREMENT,
    address TEXT NULL,
    name TEXT NULL,
    severity TEXT NULL,
    lat  FLOAT NULL,
    lng  FLOAT NULL,
    country TEXT NULL,
    code_country TEXT NULL,
    count_severity  INT NULL,
    PRIMARY KEY (id)
);
""")
