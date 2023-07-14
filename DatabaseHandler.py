import sqlite3


class DatabaseHandler:

    def __init__(self):
        self.db_file = "images.db"
        self.serverURL = "{YOURSERVERURL}"

    def setDBFile(self, file):
        self.db_file = file

    def setServerURL(self, serverURL):
        self.serverURL = serverURL

    def addEntry(self, filename, fileextension):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("INSERT INTO data (dataURL, dataExtension) VALUES (?, ?)", (str(self.serverURL + filename), fileextension))
        conn.commit()
        conn.close()
