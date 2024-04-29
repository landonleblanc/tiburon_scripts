import os
import sys
import random
import string
import re
import time

start_time = time.time()
file_count = 0

def rnd_str(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

try:
    dir = sys.argv[1]
    text = sys.argv[2]
except IndexError:
    print('Usage: python rename.py "<directory>" "<text to be replaced or --all>"')
    sys.exit(1)

if text == '--all':
    for file in os.listdir(dir):
        file_count += 1
        new_file = rnd_str(12)
        os.rename(file, new_file) 
        print(f'{file} renamed to {new_file}')

else:
    for file in dir:
        if text in file.lower():
            file_count += 1
            new_file = re.sub(text, rnd_str(), file, flags=re.IGNORECASE)
            os.rename(file, new_file)
            print(f'{file} renamed to {new_file}')
print(f'{file_count} files renamed in {time.time - start_time} seconds')
