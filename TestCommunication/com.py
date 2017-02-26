import subprocess
import json

location_paths = {}

with open('locationPaths.json', 'r') as fp:
    location_paths = json.load(fp)

current_path = location_paths['Martinsville']['Adobe Reader']
print(current_path)

subprocess.run("com.ahk " + current_path,
                shell=True)
print("Call to run com.ahk has been made.")
input("Press any key to exit.")
