import toml
import os
from colorama import Back, init
import subprocess
import sys
import time

init(autoreset=True)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def generate(filePath,language, openTerminal, openExp):
    timerStart = time.time()
    getConfig = open(__location__+"\generator\\"+language+'.toml','r');
    configParsed = toml.load(getConfig)

    #? Generate Folders
    print("Generating folders in {}".format(filePath))
    for index in range(len(configParsed["this"]["folders"])):
        if (os.path.exists(filePath + "\\" +configParsed["this"]["folders"][index]["parentFolder"] + "\\" +
            configParsed["this"]["folders"][index]["folderName"]) == False):

            os.mkdir(filePath + "\\" +configParsed["this"]["folders"][index]["parentFolder"] + "\\" +
                configParsed["this"]["folders"][index]["folderName"])
            print("{} folder is created".format(configParsed["this"]["folders"][index]["folderName"]))
        else:
            print("{} is already in {} make sure it is empty. skipping".format(configParsed["this"]["folders"][index]["folderName"],filePath))
    
    #? Generate Files
    print("\nGenerating Files. \n" + Back.RED + "Files with the same name will be overwriten")
    for index in range(len(configParsed["this"]["files"])):
        newfile = open(filePath + "\\" + configParsed["this"]["files"][index]["filePath"] + "\\" + configParsed["this"]["files"][index]["fileName"],"w")
        newfile.write(configParsed["this"]["files"][index]["fileContent"])
        print("{} is created".format(configParsed["this"]["files"][index]["fileName"]))
    
    #? Open Terminal
    if(openTerminal != None):
        print(openTerminal)
        if(openTerminal == True):
            os.system("start cmd /k cd {}".format(filePath))
        else:
            pass
    else:
        if(configParsed["options"]["openTerminal"] == True):
            print("toml".format(configParsed["options"]["openTerminal"]))
            os.system("start cmd /k cd {}".format(filePath))
        else:
            pass
    
    #? Open Folder
    if(openExp != None):
        if(openExp == True):
            subprocess.Popen(r'explorer /select,"{}"'.format(filePath))
        else:
            pass
    else:
        if(configParsed["options"]["openFileExp"] == True):
            subprocess.Popen(r'explorer /select,"{}"'.format(filePath))
        else:
            pass
    timerEnd = time.time()
    print("{}".format(timerEnd-timerStart))