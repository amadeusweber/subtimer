# Imports
import argparse
import configparser
from modification import modify_srt_files

# Logging
import logging
logger = logging.getLogger(__name__)

# Constants
CONF = 'config.conf'
DIRECTORY = './examples/'
FPS_SOURCE = 23.976
FPS_OUTPUT = 25.0


# Program
def main(
        directory:str=DIRECTORY,
        fps_source:float=FPS_SOURCE,
        fps_output:float=FPS_OUTPUT,
        conf:str=CONF,
        *args, **kwargs):
    # loading config
    logging.basicConfig(level=logging.INFO)
    logger.info('Loading config from %s', conf)
    config = configparser.ConfigParser()
    config.read(conf)
    
    # logging setup
    logging.basicConfig(level=config['Logging']['level'])
    logger.info('Set log-level to %s', config['Logging']['level'])
    
    modify_srt_files(directory, fps_source, fps_output)

    return

# Entry point
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--conf', type=str, default=CONF)
    parser.add_argument('-fs', '--fps-source', type=float, default=FPS_SOURCE)
    parser.add_argument('-fo', '--fps-output', type=float, default=FPS_OUTPUT)
    parser.add_argument('--directory', type=str, default=DIRECTORY)
    
    exit(main(**vars(parser.parse_args())))