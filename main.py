# Part One
import pathlib
import os
from pathlib import Path


file_path = pathlib.Path.cwd() / "log.txt"

dates = []
file = []
ips = []

with file_path.open() as my_file:
  for line in my_file.readlines():
    line = line.replace(" ","*")
    if "*" in line and "GET" in line:
      line_split = line.split("*")
      if "/index.html" in line_split or "/mobile/index.html" in line_split or "/mobile/services.html" in line_split or "/mobile/index.html" in line_split or "/mobile/how-we-work.html" in line_split or "/mobile/contact.html" in line_split:
        dates.append(line_split[0])
        file.append(line_split[5])
        ips.append(line_split[3])
      else:
        line = ""
    else:
      line = ""

loop_over = len(dates)
for x in range(loop_over):
  print(f"{dates[x]} {file[x]} {ips[x]}")

print("")
print("")
print("")



# Part Two

path = pathlib.Path.cwd() / "All logs"
os.chdir(path)

current_dir = Path.cwd()

logs_path = Path.home() / "All logs"
if logs_path.is_dir():  
  print("This path is a directory")

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

for file in os.listdir():
    if file.endswith(".log"):
        file_path = f"{path}\{file}"
  
        read_text_file(file_path)