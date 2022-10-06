from parse_it import ParseIt
import json
from pathlib import Path

cfgFile = 'test.ini'
configDirectory = 'config'

# config = ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(configDirectory).joinpath(cfgFile)
# config = ParseIt(config_location='/Users/d.sherstiuk/Downloads/TESTS/pytest-tests_pytest/tests_pytest/config/my_config.json', recurse=True)
config = ParseIt(config_location='/Users/d.sherstiuk/Downloads/TESTS/pytest-tests_pytest/tests_pytest/config/test.ini', recurse=True)

print(type(config.read_configuration_variable('gmail')))


def getMailURL():
    value = config.read_configuration_variable('gmail')
    return value['url1']


print(getMailURL())
