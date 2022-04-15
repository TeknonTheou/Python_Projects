import sqlite3

connection = sqlite3.connect (':memory:')
c=connection.cursor()
c.execute("CREATE TABLE Roster (Name TEXT, Species TEXT, IQ INT)")
c.execute("INSERT INTO Roster Values('Jean-Baptiste Zorg', 'Human', 122)")
rosterValues = (('Korben Dallas', 'Meat Popsicle', 100), ('Ak\'not', 'Mangalore', -5))
c.executemany("INSERT INTO Roster VALUES(?,?,?)", rosterValues)
c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",('Human','Korben Dallas',100))
connection.commit()
c.execute("SELECT Name, IQ FROM Roster WHERE Species=='Human'")
while True:
        row = c.fetchone()
        if row is None:
                break
        print(row)
connection.close()
