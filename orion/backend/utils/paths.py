from pathlib import Path
import sys


def createCsvDirectory():
    folder_path = Path("orion/data")
    folder_path.mkdir(parents=True, exist_ok=True)
    print(f"Folder '{folder_path}' created or already exists.")