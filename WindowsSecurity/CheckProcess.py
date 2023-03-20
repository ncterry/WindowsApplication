#    Check if a process is running:
import psutil

process_name = "chrome.exe"

for process in psutil.process_iter():
    try:
        if process.name() == process_name:
            print(f"{process_name} is running.")
            break
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
else:
    print(f"{process_name} is not running.")
