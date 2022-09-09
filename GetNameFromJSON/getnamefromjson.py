import json
import os
import sys
from time import time

def get_names(json: str):
    name_list = []
    with open(json, 'r') as artifacts_file:
        name, ext = os.path.splitext(json)
        with open(name+'-only-names'+ext, 'w') as filenames_file:
            for line in artifacts_file.readlines():
                filenames_file.write(json.loads(line).get("name")+'\n')

if len(sys.argv) > 2:
    print("Too many arguments")
    exit

json = sys.argv[1]

if os.path.exists(json):
    print("Output file already exists!")
    exit

start_time = time()
get_names(json)
end_time = time()
diff_time = end_time - start_time
print("Script took ", diff_time, "seconds")

