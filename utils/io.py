# Imports
import os
from typing import Iterable

# Logging
import logging
logger = logging.getLogger(__name__)

# Functions
def get_files_by_extension(directory:str, extension:str, file_filter:str='') -> Iterable[str]:
    extension = extension.lower()
    logger.debug(
        f"Scanning '{directory}' for files containing '{file_filter}' " +
        f"and {extension}-extension"
    )
    for file in os.listdir(directory):
        if os.path.splitext(file)[-1].lower() == extension:
            if file_filter in file:
                yield os.path.join(directory, file)

def read_text_file(path:str) -> str:
    with open(path, mode='r') as file:
        logger.debug(f"Reading lines from '{path}'")
        return ''.join(file.readlines())

def write_text_file(path:str, text:str) -> None:
    with open(path, mode='w+') as file:
        logger.debug(f"opened '{path}' for writing")
        file.write(text)