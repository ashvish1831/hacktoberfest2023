import psutil
import time

def log_cpu_memory_usage(interval_seconds):
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()

        print(f"CPU Usage: {cpu_percent}%")
        print(f"Memory Usage: {memory_info.percent}%")

        time.sleep(interval_seconds)


log_cpu_memory_usage(10)
