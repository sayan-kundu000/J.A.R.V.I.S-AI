import psutil
import platform

def get_system_metrics():
    # Basic specs
    system_info = {
        "os": platform.system(),
        "release": platform.release(),
        "processor": platform.processor(),
    }
    
    # CPU
    cpu_percent = psutil.cpu_percent(interval=0.1)
    
    # Memory
    mem = psutil.virtual_memory()
    memory_percent = mem.percent
    memory_total = round(mem.total / (1024 ** 3), 2)  # GB
    memory_used = round(mem.used / (1024 ** 3), 2)  # GB
    
    # Storage
    disk = psutil.disk_usage('/')
    storage_percent = disk.percent
    storage_total = round(disk.total / (1024 ** 3), 2)
    storage_used = round(disk.used / (1024 ** 3), 2)
    
    # Battery
    battery_info = "Desktop / No Battery"
    battery_percent = 100
    if hasattr(psutil, 'sensors_battery'):
        battery = psutil.sensors_battery()
        if battery:
            battery_percent = round(battery.percent, 1)
            battery_info = "Charging" if battery.power_plugged else "Discharging"
            
    # Temperature
    temperature = 45.0 # Mock average operating temp in Celsius for Windows without Admin
    try:
        if hasattr(psutil, 'sensors_temperatures'):
            temps = psutil.sensors_temperatures()
            if temps and 'coretemp' in temps:
                temperature = round(temps['coretemp'][0].current, 1)
    except Exception:
        pass
        
    return {
        "info": system_info,
        "cpu": cpu_percent,
        "memory": {
            "percent": memory_percent,
            "total_gb": memory_total,
            "used_gb": memory_used
        },
        "storage": {
            "percent": storage_percent,
            "total_gb": storage_total,
            "used_gb": storage_used
        },
        "battery": {
            "percent": battery_percent,
            "status": battery_info
        },
        "temperature_c": temperature
    }
