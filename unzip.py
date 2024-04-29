import zipfile
import os
import glob

def unzip(zip_file, dest_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(dest_dir)

def main():
    zip_files = glob.glob('*.zip')
    print(f'Found {len(zip_files)} zip files')
    for zip_file in zip_files:
        dest_dir = os.path.splitext(zip_file)[0]
        print(f'Unzipping {zip_file} to {dest_dir}')
        unzip(zip_file, dest_dir)
        print('Done!')

if __name__ == "__main__":
    main()
