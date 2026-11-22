import psutil

def get_status():
    battery = psutil.sensors_battery()
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent

    if battery is None:
        battery_info = "No battery detected"
    else:
        plugged = "Plugged in" if battery.power_plugged else "On battery"
        battery_info = f"{battery.percent:.0f}% ({plugged})"

    return battery_info, cpu, ram

battery_info, cpu, ram = get_status()
print(f"Battery: {battery_info} | CPU: {cpu}% | RAM: {ram}%")