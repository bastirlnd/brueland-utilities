import subprocess
import re
import decimal

def get_remaining_capacity() -> decimal.Decimal:
    decimal.getcontext().prec = 4
    system_profiler_call = "system_profiler SPStorageDataType"
    process_result = subprocess.run(system_profiler_call, text=True, shell=True, capture_output=True)
    stdout_result = process_result.stdout

    match_capacity = re.search('(?<=Capacity:)(.*)(?=GB)', stdout_result)
    match_free_pattern = re.search('(?<=Free:)(.*)(?=GB)', stdout_result)
    
    capacity = None
    free = None

    if match_capacity:
        capacity = match_capacity.group(1).strip(" ,\n").replace(",", ".")
    if match_free_pattern:
        free = match_free_pattern.group(1).strip(" ,\n").replace(",", ".")
    
    percent_full = (decimal.Decimal(free)/decimal.Decimal(capacity))*100
    return percent_full

def print_percent_bar(percent: decimal.Decimal):
    fill = "█"
    prefix = "Remaining Storage:"
    suffix = "Full"
    length = 100
    percent_int = int(percent)
    bar = fill * percent_int + ("-" * (length-percent_int))
    print(f'\r{prefix} |{bar}| {percent}% {suffix}\r')

print_percent_bar(get_remaining_capacity())
