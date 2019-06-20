import time
from scheduler import Scheduler
from sensors import CPUTemp
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
        db_handler.write_to_db(reading)
        print(f"Wrote CPU Temperature: {reading[1]} at {reading[0]}")

    schd = Scheduler(5, write_test_helper)
    schd.start()
    time.sleep(30)
    schd.stop()

if __name__ == "__main__":
    test_db_write()
