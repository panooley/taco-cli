__version__ = "0.0.1 (224-10-08)"
__app_name__ = 'Taco'
__repos_url__ = "https://www.github.io/panooley/taco"
__description__ = 'A simple task tracker tool for the command line.'
__author__ = 'panooley'

import sys, platformdirs, pathlib, yaml
from utils import print_bold, usage_message

class Config:
    def __init__(self, app_data_dir):
        self.config_file = open(app_data_dir + '/config.yaml').read()
        self.dict_data = yaml.safe_load(self.config_file)

def show_help(args):
    if len(args) == 0:
        usage_message(__description__)


def args_valid(args):
    if len(args) == 0:
        return False
    if args[0] not in ['add','list','update','delete','search','stats','timer','export','import', '--version']:
        return False
    return True

def main(args):
    app_data_dir = platformdirs.user_data_dir(__app_name__, __author__)
    pathlib.Path(app_data_dir).mkdir(parents=True, exist_ok=True)
    config = Config(app_data_dir)

    if args_valid(args):
        match args[0]:
            case "--version":
                print(f'taco version {__version__}')
    else:
        show_help(args)
    return -1

err_code: int = main(sys.argv[1:])
sys.exit(err_code)

