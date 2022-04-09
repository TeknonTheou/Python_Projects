import sqlite3

fileList = ('information.docx', 'Hello.txt','myImage.png', \
	    'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#create database
conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
#create table and columns
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName TEXT)")
    for myfile in fileList:
#Find items in fileList with extension '.txt'
        if myfile.endswith('.txt'):
#add '.txt' items to database
            cur.execute("INSERT INTO tbl_files(col_fileName) VALUES ('{}')".format(myfile))
#commit the changes to the database
    conn.commit()

with conn:
    cur = conn.cursor()
#select fileName column
    cur.execute("SELECT col_fileName FROM tbl_files")
#retrieve all info from the column
    varFiles = cur.fetchall()
#print info in format requested
    for x in varFiles:
        msg = "File Name: {}\n".format(x)
        print(msg)
conn.close()
