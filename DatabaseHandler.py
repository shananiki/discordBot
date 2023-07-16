import sqlite3


class DatabaseHandler:

    def __init__(self):
        self.db_file = "images.db"
        self.serverURL = "http://82.165.55.139/images/"
        self.comment_table = """CREATE TABLE "comments" (
            "commentID"	INTEGER NOT NULL,
            "dataFK"	INTEGER NOT NULL,
            "username"	TEXT,
            "comment"	TEXT,
            PRIMARY KEY("commentID" AUTOINCREMENT)
            )"""
        self.data_table = """CREATE TABLE "data" (
            "dataID"	INTEGER NOT NULL,
            "dataURL"	TEXT,
            "dataExtension"	TEXT,
            PRIMARY KEY("dataID" AUTOINCREMENT)
            )"""
        self.checkTables()

    def setDBFile(self, file):
        self.db_file = file

    def setServerURL(self, serverURL):
        self.serverURL = serverURL

    def addEntry(self, filename, fileextension):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        c.execute("INSERT INTO data (dataID, dataURL, dataExtension) VALUES (?, ?, ?)",
                  (filename, str(self.serverURL + filename), fileextension))
        conn.commit()
        conn.close()

    def createTable(self, table_name):
        conn = sqlite3.connect(self.db_file)
        c = conn.cursor()
        if table_name == "comments":
            c.execute(self.comment_table)
        elif table_name == "data":
            c.execute(self.data_table)
        conn.commit()
        conn.close()

    def checkTables(self):
        if not self.table_exists("comments"):
            self.createTable("comments")
        if not self.table_exists("data"):
            self.createTable("data")

    def table_exists(self, table_name):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))

        table_exists = len(cursor.fetchall()) > 0

        cursor.close()
        conn.close()
        return table_exists


if __name__ == '__main__':
    db = DatabaseHandler()
