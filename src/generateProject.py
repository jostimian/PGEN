import toml
import os
from colorama import Back, init
import subprocess
import sys
import time
import threading

init(autoreset=True)
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
def generate(folderPath,language, openTerminal, openExp):
    timerStart = time.time()
    getConfig = open(__location__+"\generator\\"+language+'.toml','r');
    configParsed = toml.load(getConfig)
    threading.Thread(target=genFolders, args=(configParsed,folderPath,)).start()
    threading.Thread(target=genFiles, args=(configParsed,folderPath,)).start()
    threading.Thread(target=ope, args=(openExp,folderPath,configParsed,)).start()
    threading.Thread(target=opt, args=(openTerminal,folderPath,configParsed,)).start()
    timerEnd = time.time()
    print("{}".format(timerEnd-timerStart))


def genFolders(configParsed, folderPath):
    #? Generate Folders
    print("Generating folders in {}".format(folderPath))
    for index in range(len(configParsed["this"]["folders"])):
        if (os.path.exists(folderPath + "\\" +configParsed["this"]["folders"][index]["parentFolder"] + "\\" +
            configParsed["this"]["folders"][index]["folderName"]) == False):

            os.mkdir(folderPath + "\\" +configParsed["this"]["folders"][index]["parentFolder"] + "\\" +
                configParsed["this"]["folders"][index]["folderName"])
            print("{} folder is created".format(configParsed["this"]["folders"][index]["folderName"]))
        else:
            print("{} is already in {} make sure it is empty. skipping".format(configParsed["this"]["folders"][index]["folderName"],folderPath))

def genFiles(configParsed, folderPath):
    #? Generate Files
    print("\nGenerating Files. \n" + Back.RED + "Files with the same name will be overwriten")
    for index in range(len(configParsed["this"]["files"])):
        newfile = open(folderPath + "\\" + configParsed["this"]["files"][index]["filePath"] + "\\" + configParsed["this"]["files"][index]["fileName"],"w")
        newfile.write(configParsed["this"]["files"][index]["fileContent"])
        print("{} is created".format(configParsed["this"]["files"][index]["fileName"]))

def opt(openTerminal,folderPath,configParsed):
    #? Open Terminal
    if(openTerminal != None):
        print(openTerminal)
        if(openTerminal == True):
            os.system("start cmd /k cd {}".format(folderPath))
        else:
            pass
    else:
        if(configParsed["options"]["openTerminal"] == True):
            print("toml".format(configParsed["options"]["openTerminal"]))
            os.system("start cmd /k cd {}".format(folderPath))
        else:
            pass

def ope(openExp,folderPath,configParsed):
    #? Open Folder
    if(openExp != None):
        if(openExp == True):
            subprocess.Popen(r'explorer /select,"{}"'.format(folderPath))
        else:
            pass
    else:
        if(configParsed["options"]["openFileExp"] == True):
            subprocess.Popen(r'explorer /select,"{}"'.format(folderPath))
        else:
            pass