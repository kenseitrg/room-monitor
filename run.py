import time
from scheduler import Scheduler
from sensors import CPUTemp, AirQ, TempHum
from db import DatabaseHandler

cpu_mon = CPUTemp(f"/sys/class/thermal/thermal_zone0/temp")
airq = AirQ(1)
temphum = TempHum(2)
db_handler = DatabaseHandler("test01")

def read_sensors() -> None:
    cpu_mon = CPUTemp(f"/sys/class/thermal/thermal_zone0/temp")
    airq = AirQ(1)
    temphum = TempHum(2)
    db_handler = DatabaseHandler("test01")

    def db_write_helper() -> None:
        cpu_reading = cpu_mon.get_reading()
        db_handler.write_to_db("CPU-Temp",cpu_reading)
        #print(f"Wrote CPU Temperature: {cpu_reading[1]} at {cpu_reading[0]}")
        aq_reading = airq.get_reading()
        db_handler.write_to_db("AirQ",aq_reading)
        #print(f"Wrote Air Quality: {aq_reading[1]} at {aq_reading[0]}")
        rtemp_hum = temphum.get_reading("temperature")
        rtemp = (rtemp_hum[0],rtemp_hum[1][0])
        db_handler.write_to_db("Room_Temp",rtemp)
        #print(f"Wrote Room Temperature: {rtemp[1]} at {rtemp[0]}")
        rhum = (rtemp_hum[0],rtemp_hum[1][1])
        db_handler.write_to_db("Room_Hum",rhum)
        #print(f"Wrote Room Humidity: {rhum[1]} at {rhum[0]}")

    schd = Scheduler(300, db_write_helper)
    schd.start()

if __name__ == "__main__":
    read_sensors()
