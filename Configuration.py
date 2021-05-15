import json

global g_blockedMethods,Redirects
g_blockedMethods = []
Redirects = {}

global HOST,PORT,VERSION
HOST = "localhost"
PORT = 1300
VERSION = "0.1.1"


def read_AllConfig():
    for x in registeredConfigFiles.keys():
        registeredConfigFiles[x](read_ConfigFile(x))


def read_ConfigFile(filename : str):
    '''
    filename <- str
    return -> Dict
    '''
    try:
        with open(f"config/{filename}") as f:
            return json.loads(f.read())
    except:
        print("Failed to read Configuration File")
        return json.loads("{}")

def load_GlobalConfig(config : dict):
    global g_blockedMethods,Redirects
    g_blockedMethods = config["blockedMethods"]
    Redirects = config["Redirects"]

    global HOST,PORT
    HOST = config["SocketSettings"]["HOST"]
    PORT = config["SocketSettings"]["PORT"]


registeredConfigFiles = {
    "globalConfiguration.json" : load_GlobalConfig
}