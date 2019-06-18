class CPUTemp():
    def __init__(self, tfile_path: str) -> None:
        self.file_path = tfile_path

    def get_reading(self) -> float:
        with open(self.file_path, 'r') as f:
            try:
                temp = float(f.readline()) / 1000.
            except:
                temp = -9999.
        return temp