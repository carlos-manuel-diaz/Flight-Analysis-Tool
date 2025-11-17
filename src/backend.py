from PySide6.QtWidgets import QFileDialog
import pandas as pd

class TrackerEngine:
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.csvList = []
        self.df = None

    def getCsv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )

        if not file_path:
            return

        try:
            self.df = pd.read_csv(file_path)
        except Exception as e:
            print(f"Failed to read CSV: {e}")
            return

        print(f"Loaded CSV: {file_path}")
        print(f"Rows: {len(self.df)} Columns: {list(self.df.columns)}")
        return file_path
