import configparser

config=configparser.ConfigParser()
config.read('configuartion.config')

baseUrl=config['DEFAULT']['base_url']