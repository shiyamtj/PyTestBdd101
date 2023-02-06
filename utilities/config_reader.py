from configparser import ConfigParser

def read_config(section, key):
    CONFIG_LOCATION: str = '../configurations/config.ini'
    config = ConfigParser()
    config.read(CONFIG_LOCATION)
    return_value = str(config.get(section, key))
    return return_value
