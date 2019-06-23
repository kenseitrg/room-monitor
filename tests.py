import time
from scheduler import Scheduler
from sensors import CPUTemp, AirQ, TempHum
from db import DatabaseHandler

def test_scheduler() -> None:    
    def simple_schd_test() -> None:
        print(f"Scheduler is running")
    
    schd = Scheduler(5, simple_schd_test)
    schd.start()
    time.sleep(30)
    schd.stop()

def test_cpu_temp() -> None:
    cpu_mon = CPUTemp(f"/sys/class/thermal/thermal_zone0/temp")
    
    def print_cpu_temp() -> None:
        time, value = cpu_mon.get_reading()
        print(f"CPU Temperature is {value} at {time}")
    
    schd = Scheduler(5, print_cpu_temp)
    schd.start()
    time.sleep(30)
    schd.stop()

def test_db_write() -> None:
    cpu_mon = CPUTemp(f"/sys/class/thermal/thermal_zone0/temp")
    db_handler = DatabaseHandler("test01")
    
    def write_test_helper() -> None:
        reading = cpu_mon.get_reading()
        db_handler.write_to_db("CPU-Temp",reading)
        print(f"Wrote CPU Temperature: {reading[1]} at {reading[0]}")

    schd = Scheduler(5, write_test_helper)
    schd.start()
    time.sleep(30)
    schd.stop()

def test_sensors() -> None:
    cpu_mon = CPUTemp(f"/sys/class/thermal/thermal_zone0/temp")
    airq = AirQ(1)
    temphum = TempHum(2)
    db_handler = DatabaseHandler("test01")

    def write_test_helper() -> None:
        cpu_reading = cpu_mon.get_reading()
        db_handler.write_to_db("CPU-Temp",cpu_reading)
        print(f"Wrote CPU Temperature: {cpu_reading[1]} at {cpu_reading[0]}")
        aq_reading = airq.get_reading()
        db_handler.write_to_db("AirQ",aq_reading)
        print(f"Wrote Air Quality: {aq_reading[1]} at {aq_reading[0]}")
        rtemp_hum = temphum.get_reading("temperature")
        rtemp = (rtemp_hum[0],rtemp_hum[1][0])
        db_handler.write_to_db("Room_Temp",rtemp)
        print(f"Wrote Room Temperature: {rtemp[1]} at {rtemp[0]}")
        rhum = (rtemp_hum[0],rtemp_hum[1][1])
        db_handler.write_to_db("Room_Hum",rhum)
        print(f"Wrote Room Humidity: {rhum[1]} at {rhum[0]}")

    schd = Scheduler(5, write_test_helper)
    schd.start()
    time.sleep(30)
    schd.stop()

if __name__ == "__main__":
    test_sensors()
