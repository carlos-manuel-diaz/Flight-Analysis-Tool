
from pathlib import Path
import sqlite3


def database_init(): 
  """ Creates database """ 
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


def createDefaultProfile() -> bool:
  """ Create default, starting profile"""
  try:
      with sqlite3.connect('data/profiles.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS (SELECT 1 FROM profile)") # 0 if profile list is empty, else 1
        check = cursor.fetchone()  
        if not check:
           cursor.execute(
                "INSERT OR REPLACE INTO profile (name, description) VALUES (?, ?)",
                ("Default", "Default profile created at app startup"),
            )
           conn.commit()
           return True
        return False

  except Exception as e:
      print(f"Error createing default profile: {e}")
      raise  
         
         
def loadProfileNames():
    try:
      with sqlite3.connect('data/profiles.db') as conn:   
         cursor = conn.cursor() 
         cursor.execute("SELECT name FROM profile")  
         profileNames = cursor.fetchall()  

         print("Profiles loaded")
         return profileNames
    except Exception as e:
      print(f"Error fetching profile names: {e}")
      raise  


# def createProfile():

# def deleteProfile():
