# Imports
import os
import re
import datetime
from dataclasses import dataclass
from utils.io import get_files_by_extension, read_text_file, write_text_file
from utils.datetime import (
    time_total_seconds,
    time_from_seconds,
    strftime_hmsmilli
)

# Logging
import logging
logger = logging.getLogger(__name__)

# Constants
EXTENSION = '.srt'
## Regex
REGEX_EXTRACT = re.compile(
    r"(\d+)\n(\d+\:\d+\:\d+,\d+) --> (\d+\:\d+\:\d+,\d+)\n((?:[^\n]+\n?)+)\n*"
)

# Functions
def load_srt_file(path):
    srt_text = ''.join(read_text_file(path))
    for index, start, end, text in REGEX_EXTRACT.findall(srt_text):
        yield Subtitle(
            index,
            datetime.time.fromisoformat(start),
            datetime.time.fromisoformat(end),
            text
        )

def write_srt_file(subtitles:list, path):
    logger.info(f"Writing {path}")
    text = '\n'.join(map(str, subtitles))
    write_text_file(path, text)


def modify_srt_file(path, fps_source, fps_output):
    logger.info(f"Processing '{path}'")
    subtitles = tuple(load_srt_file(path))

    # Multipy start and end times by conversion factor
    factor = fps_source / fps_output
    logger.info(f"Scale timing by {factor}")
    for subtitle in subtitles:
        subtitle.start = time_from_seconds(
            time_total_seconds(subtitle.start) * factor
        )
        subtitle.end = time_from_seconds(
            time_total_seconds(subtitle.end) * factor
        )

    # Save subtitles
    root, filename = os.path.split(path)
    filename = list(filename.split('.'))
    filename.insert(2 if filename[0].strip() == '' else 1, f"fps{fps_output}")
    write_srt_file(
        subtitles,
        os.path.join(root, '.'.join(filename))
    )


    

def modify_srt_files(source, file_filter, fps_source, fps_output):
    # scan for files
    processed_indicator = f".fps{str(fps_output)}"
    srt_files = tuple(
        file
        for file in get_files_by_extension(source, EXTENSION, file_filter)
        if processed_indicator not in file
    )
    # remove files 
    logger.info('Found files: \n - ' + '\n - '.join(srt_files))

    # process files
    for file in srt_files:
        modify_srt_file(file, fps_source, fps_output)

# Classes
@dataclass
class Subtitle:
    index:int
    start:datetime.time
    end:datetime.time
    text:str

    def __str__(self) -> str:
        return '\n'.join((
            str(self.index),
            strftime_hmsmilli(self.start) + ' --> ' + 
            strftime_hmsmilli(self.end),
            self.text
        ))
    
    
