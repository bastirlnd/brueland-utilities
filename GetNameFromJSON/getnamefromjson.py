import json
import os
import sys
from time import time

def get_names(input_file_name: str, output_file_name: str):
    with open(input_file_name, 'r') as artifacts_file:
        with open(output_file_name, 'w') as filenames_file:
            for line in artifacts_file.readlines():
                filenames_file.write(json.loads(line).get("name")+'\n')

if len(sys.argv) > 2:
    print("Too many arguments")
    exit

#TODO write --help page

#for example: list-of-json.txt
input_file_name = sys.argv[1]

file_name, extension = os.path.splitext(json)
output_file_name = name + '-only-names' + ext

if os.path.exists(output_file_name):
    print("Output file already exists!")
    exit

start_time = time()
get_names(input_file_name, output_file_name)
end_time = time()
diff_time = end_time - start_time
print("Script took ", diff_time, "seconds")

