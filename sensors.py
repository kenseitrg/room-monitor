from datetime import datetime
from typing import Tuple

class CPUTemp():
    def __init__(self, tfile_path: str) -> None:
        self.file_path = tfile_path

    def get_reading(self) -> Tuple[str, float]:
        with open(self.file_path, 'r') as f:
            try:
                temp = float(f.readline()) / 1000.
            except:
                temp = -9999.
        return (datetime.utcnow(), temp)