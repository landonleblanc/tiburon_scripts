import os
import sys
import re
import time

try:
    dir = sys.argv[1]
except IndexError:
    print("Usage: yt_episode_number.py <directory>")
    sys.exit(1)
start_time = time.time()
file_count = 0
print(f"Scanning {dir}")
for filename in os.listdir(dir):
    try:
        print(f"Checking {filename}")
        if re.match(r'^Episode [\d]+', filename) is not None:
            print(f"Skipping {filename}")
            continue
        pattern = r'[Ee][Pp][\.:\s]*[\d]+|[Ee][Pp][Ii][Ss][Oo][Dd][Ee][\s]*[\d]+'
        episode = re.search(pattern, filename)
        if episode is not None:
            episode_number = re.search(r'\d+', episode.group()).group()
            print(f"Found episode number: {episode_number}")
            new_filename = f"Episode {episode_number} {filename}"
            os.rename(os.path.join(dir, filename), os.path.join(dir, new_filename))
            print(f"Renamed {filename} to {new_filename}")
            file_count += 1
    except Exception as e:
        print(f"Error renaming {filename}: {e}")
end_time = time.time()
print(f"Renamed {file_count} files in {end_time - start_time:.2f} seconds")
sys.exit(0)
 