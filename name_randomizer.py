import os
import sys
import random
import string
import re
import time

start_time = time.time()
file_count = 0

def rnd_str(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

try:
    dir = sys.argv[1]
    text = sys.argv[2]
    assert os.path.isdir(dir)
    assert type(text) == str
except IndexError:
    print('Usage: python rename.py "<directory>" "<text to be replaced or --all>"')
    sys.exit(1)
except AssertionError:
    print('Invalid directory or text')
    sys.exit(1)

if text == '--all':
    for file in os.listdir(dir):
        try:
            file_count += 1
            extension = os.path.splitext(file)[1]
            new_file = rnd_str(12) + extension
            os.rename(os.path.join(dir, file), os.path.join(dir, new_file))
            print(f'{file} renamed to {new_file}')
        except Exception as e:
            print(f'Error renaming {file}: {e}')

else:
    print(f'---Scanning {dir} for filenames containing: {text}---')
    for file in os.listdir(dir):
        try:
            if re.search(text, file, flags=re.IGNORECASE):
                file_count += 1
                new_file = re.sub(text, rnd_str(), file, flags=re.IGNORECASE)
                os.rename(os.path.join(dir, file), os.path.join(dir, new_file))
                print(f'{file} renamed to {new_file}')
        except Exception as e:
            print(f'Error renaming {file}: {e}')
print(f'---{file_count} files renamed in {time.time() - start_time} seconds---')
