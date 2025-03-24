import configparser
config = configparser.ConfigParser()
config.read("config.ini")
print("Value:", config["DEFAULT"]["key"])