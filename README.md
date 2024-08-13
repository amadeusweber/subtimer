# subtimer
Alter the timing of subtitles based on playback speed

## Setup
Developed and tested for Python 3.11.7

## Usage
```bash
python3 main.py -fs 23.976 -fo 25 -f .ger --directory path/to/subtitles/
```


**Command line arguments**
| Argument | Description |
|:---:|:---|
| -c, --conf | Path to config (not used) |
| -fs, --fps-source | Subtitle frame rate |
| -fo, --fps-output | Output frame rate |
| -f. --filter | filter for file names (name must contain filter) |
| --directory | Directory to search for subtitle files in |