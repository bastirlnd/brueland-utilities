import jq
import json
import sys
import logging

from os import listdir
from os.path import isfile, join

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def get_files_in_dir(directory):
    logger.info("Getting files in directory: %s", directory)
    return [f for f in listdir(directory) if isfile(join(directory, f))]            

def filter_for_blobs(file_list: list[str], directory: str):
    list_of_blobs = []
    logger.info("Filtering for maxBlobSize from git-sizer files")
    for file in file_list:
        with open(join(directory, file), 'r') as f:
            data = json.load(f)
            # Use jq to filter the data
            blobs = jq.compile('.["maxBlobSize"].value').input(data).first()
            list_of_blobs.append(blobs)
    return list_of_blobs

def unique_sorted_blobs(blobs):
    # Remove duplicates and sort the list from highest to lowest
    unique_blobs = sorted(set(blobs), reverse=True)
    return unique_blobs

def bytes_to_mb(bytes):
    return bytes / (1000 * 1000)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python gsmbs.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    files = get_files_in_dir(directory)
    blobs = filter_for_blobs(files, directory)
    unique_blobs = unique_sorted_blobs(blobs)
    i = 0
    logger.info("10 biggest, unique sorted blobs (DESC):")
    for blob in unique_blobs:
        mb_value = bytes_to_mb(blob)
        print(f'{blob} bytes -> {mb_value:.2f} MB')
        i += 1
        if i == 10:
            break