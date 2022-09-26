import json as JSON
import os
import sys
from time import time

def get_size(json: str):
    size_list = []
    with open(json, 'r') as artifacts_file:
        name, ext = os.path.splitext(json)
        with open(name+'-only-size'+ext, 'w') as result_file:
            for line in artifacts_file.readlines():
                size_list.append(JSON.loads(line).get("size"))
            #TODO optimize the sort (currently takes ~59s with 2.7GB of input file)
            size_list.sort(reverse=True)
            for size in size_list:
                result_file.write(str(size)+'\n')

if len(sys.argv) > 2:
     print("Too many arguments")
     exit

#TODO Add check (if output file exists: ...)

json = sys.argv[1]

start_time = time()
get_size(json)
end_time = time()
diff_time = end_time - start_time
print("Script took ", diff_time, "seconds")
