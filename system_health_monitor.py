import psutil
import platform
import time

def get_system_info():
    print("System Health Monitor")
    print("---------------------")
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print()

while True:
    print("="*30)
    get_system_info()
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery: {battery.percent}% {'(Charging)' if battery.power_plugged else '(Not Charging)'}")
    else:
        print("Battery status not available.")
    print("="*30)
    
    time.sleep(10)  # Wait for 10 seconds before next reading