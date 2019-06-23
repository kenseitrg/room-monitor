from datetime import datetime
from typing import Tuple
import grovepi

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

class AirQ():
    def __init__(self, port:int) -> None:
        self.port = port
        grovepi.pinMode(self.port,"INPUT")

    def get_reading(self) -> Tuple[str, float]:
        try:
            aq = grovepi.analogRead(self.port)
        except:
            aq = -9999.
        return (datetime.utcnow(), aq)
    
class TempHum():
    def __init__(self, port:int) -> None:
        self.port = port

    def get_reading(self, rtype:str) -> Tuple[str, float]:
        try:
            [temp, humidity] = grovepi.dht(self.port, 1)
        except:
            [temp, humidity] = [-9999.0, -9999.0]
            
        return (datetime.utcnow(), [temp, humidity])
