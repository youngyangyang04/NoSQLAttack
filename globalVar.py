class GlobalVar:
    optionSet = [False] * 9
    yes_tag = ['y', 'Y']
    no_tag = ['n', 'N']
    victim = "not set"
    webPort = "not set"
    url = "not set"
    httpMethod= "not set"
    platform = "not set"
    https = "not set"
    myIP = "not set"
    myPort = "not set"
    verb = "not set"
    scanNeedCreds = "not set"
    dbPort = 27017
def set_optionSet(i,value):
    GlobalVar.optionSet[i]=value
def get_optionSet(i):
    return GlobalVar.optionSet[i]

def get_yes_tag():
    return GlobalVar.yes_tag
def get_no_tag():
    return GlobalVar.no_tag

def set_victim(value):
    GlobalVar.victim = value
def get_victim():
    return GlobalVar.victim

def set_webPort(value):
    GlobalVar.webPort = value
def get_webPort():
    return GlobalVar.webPort

def set_url(value):
    GlobalVar.url = value
def get_url():
    return GlobalVar.url;

def set_httpMethod(value):
    GlobalVar.httpMethod = value
def get_httpMethod():
    return GlobalVar.httpMethod

def set_platform(value):
    GlobalVar.platform = value
def get_platform():
    return GlobalVar.platform

def set_myIP(value):
    GlobalVar.myIP = value
def get_myIP():
    return GlobalVar.myIP

def set_myPort(value):
    GlobalVar.myPort = value
def get_myPort():
    return GlobalVar.myPort

def set_dbPort(value):
    GlobalVar.dbPort = value
def get_dbPort():
    return GlobalVar.dbPort


https = "not set"
verb = "not set"
scanNeedCreds = "not set"