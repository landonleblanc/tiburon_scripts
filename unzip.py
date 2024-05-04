import zipfile
import os
import glob
import sys
import time

def unzip(zip_file, dest_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

#Handle cmd line arguments
try:
    dir = sys.argv[1]
    os.isdir(dir)
except IndexError:
    print("Usage: unzip.py <directory>")
    sys.exit(1)
except FileNotFoundError:
    print(f"Directory {dir} not found")
    sys.exit(1)
start_time = time.time()
#Find all zip files in the directory
zip_files = glob.glob(f'{dir}/*.zip')
print(f'Found {len(zip_files)} zip files')

#Unzip each file
for zip_file in zip_files:
    try:
        dest_dir = os.path.splitext(zip_file)[0]
        print(f'Unzipping {zip_file} to {dest_dir}')
        unzip(zip_file, dest_dir)
        print('Done!')
    except Exception as e:
        print(f'Error unzipping {zip_file}: {e}')
print(f'Unzipped {len(zip_files)} files in {time.time() - start_time:.2f} seconds')