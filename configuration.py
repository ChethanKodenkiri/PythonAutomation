import configparser

config=configparser.ConfigParser()
config.read('config/configuartion.properties')

baseUrl=config['DEFAULT']['base_urlone']