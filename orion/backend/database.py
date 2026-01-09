
from pathlib import Path
import sqlite3


def database_init():    
  try:
    conn = sqlite3.connect('data/profiles.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profile (
            profileId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            description TEXT    
        )
''')
    
    conn.commit()
    conn.close()
  except Exception as e:
        print("Database error: {e}")
        raise


# def createProfile():

# def deleteProfile():
