#    Check if a file or directory exists and has appropriate permissions:
import os

# Example file
file_path = "C:/Program Files/SomeFolder/SomeFile.txt"

if os.path.exists(file_path):
    if os.access(file_path, os.R_OK):
        print(f"{file_path} exists and is readable.")
    else:
        print(f"{file_path} exists, but is not readable.")
else:
    print(f"{file_path} does not exist.")
