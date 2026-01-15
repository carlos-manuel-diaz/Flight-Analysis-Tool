
from pathlib import Path
import sqlite3


def database_init(): 
  """ Creates database """ 
  try:
    conn = sqlite3.connect('profiles.db')
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
      with sqlite3.connect('profiles.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS (SELECT 1 FROM profile)") # 0 if profile list is empty, else 1
        check = cursor.fetchone()  
        if check[0] == 0:
           cursor.execute(
                "INSERT INTO profile (name, description) VALUES (?, ?)",
                ("Default", "Default profile created at app startup."),
            )
           conn.commit()
           print("Default profile created!")
           

  except Exception as e:
      print(f"Error creating default profile: {e}")
      raise  
         
         
def loadProfileNames():
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM profile")
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching profile names: {e}")
        raise

def getProfileDescription(profileName):
    try:
       with sqlite3.connect('profiles.db') as conn:
          cursor = conn.cursor()
          cursor.execute("SELECT description FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          return row[0] if row else None
    except Exception as e:
        print(f"Error fetching profile description: {e}")
        raise
          


def createProfile(profileName, description):
    try:
       with sqlite3.connect('profiles.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO profile (name, description) VALUES (?, ?)",
                (profileName, description),
            )
        conn.commit()
        print(f"Profile: {profileName} created!" )
    except Exception as e:
        print(f"Error creating: {e}")
        raise    

# def deleteProfile():
