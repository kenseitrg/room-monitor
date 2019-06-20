from influxdb import InfluxDBClient
from typing import List, Tuple

class DatabaseHandler():
    def __init__(self, db_name:str) -> None:
        self.client = InfluxDBClient(host='localhost', port=8086)
        self.db_name = db_name

    def create_db(self, db_name:str) -> None:
        self.client.create_database(db_name)

    def print_db_list(self) -> None:
        dblist = self.client.get_list_database()
        print(dblist)

    def write_to_db(self, data:Tuple) -> None:
        self.client.switch_database(self.db_name)
        json_body = [
        {
            "measurement": "room-monitor",
            "tags": {
                "user": "amilekhin",
                "room": "Matvey's room"
            },
        "time": data[0],
        "fields": {
            "CPU-Temp": data[1]
            }
        }]
        self.client.write_points(json_body)

if __name__ == "__main__":
    db_handler = DatabaseHandler("test01")
    db_handler.print_db_list()