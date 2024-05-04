# tiburon_scripts
Various scripts used on my NAS server
---
## unzip.py
Takes a directory as an arg and extracts all .zip files present in the directory
Usage:
`python3 unzip.py <path_to_dir>`

## name_randomizer.py
Takes a directory and a string to replace with random characters as args.
Alternatively `--all` can be used to replace the entire file name
Usage:
`python3 name_randomizer.py <path_to_dir> <"string">`
`python3 name_randomizer.py <path_to_dir> --all`


## yt_episode_num.py
Take a directory as an arg and adds "Episode #" to the beginning of any file containing and episode name
Usage:
`python3 yt_episode_num.py <path_to_dir>`
