# Imports
import os
from typing import Iterable

# Logging
import logging
logger = logging.getLogger(__name__)

# Functions
def get_files_by_extension(directory:str, extension:str) -> Iterable[str]:
    extension = extension.lower()
    for file in os.listdir(directory):
        if os.path.splitext(file)[-1].lower() == extension:
            yield os.path.join(directory, file)

def read_text_file(path:str) -> str:
    with open(path, mode='r') as file:
        return ''.join(file.readlines())

def write_text_file(path:str, text:str) -> None:
    with open(path, mode='w+') as file:
         file.write(text)