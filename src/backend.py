from PySide6.QtWidgets import QFileDialog
import pandas as pd

class TrackerEngine:
    
    def __init__(self):
        self.reset()

    def reset(self):
        self.csvList = []
        self.df = None

    def addCsv(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)"
        )

        if not file_path:
            return


        # print(f"Loaded CSV: {file_path}")
        # print(f"Rows: {len(self.df)} Columns: {list(self.df.columns)}")
        return file_path

    def extract(self, path):
        try:
            self.df = pd.read_csv(path)
        except Exception as e:
            print(f"Failed to read CSV: {e}")
            return None, None
        
        time_col = "time_elapsed"
        value_col = "acceleration_y"

        # __ over ___ function
        if time_col not in self.df.columns or value_col not in self.df.columns:
            print(f"Required columns not found: need '{time_col}' and '{value_col}'")
            return
        
        return self.df[time_col], self.df[value_col]