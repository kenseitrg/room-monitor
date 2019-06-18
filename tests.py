import time
from scheduler import Scheduler
from sensors import CPUTemp

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
        value = cpu_mon.get_reading()
        print(f"CPU Temperature is {value}")
    
    schd = Scheduler(5, print_cpu_temp)
    schd.start()
    time.sleep(30)
    schd.stop()

if __name__ == "__main__":
    test_cpu_temp()
