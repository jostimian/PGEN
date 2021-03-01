import toml
import os
import sys

def readConfig(configFileName):
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    config = open(__location__+"\generator\\"+configFileName, 'r')
    configParsed = toml.load(config)
    print("options")
    print("openTerminal = {}".format(configParsed["options"]["openTerminal"]))
    print("openTerminal = {}".format(configParsed["options"]["openFileExp"]))
    print('\nFiles:')
    for index in range(len(configParsed["this"]["files"])): #? show files
        print("{}".format(configParsed["this"]["files"][index]["fileName"]))
    print("\nFolders:")
    for index in range(len(configParsed["this"]["folders"])): #? show folders
        print("{}".format(configParsed["this"]["folders"][index]["folderName"]))