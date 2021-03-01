import argparse
import readConfig
import generateProject
if (__name__ == "__main__"):
    # ? parser init
    parser = argparse.ArgumentParser(description="Project Generator CLI")
    parser.add_argument('--fp', dest="filePath", help="Generate template in the specified location")
    parser.add_argument('--l', dest="lang", help="Language to be used")
    parser.add_argument('--rg', dest="readConfig", help="Read config file for the specifed language")
    parser.add_argument('--opt', dest="openTerminal", help="Open terminal after the template is generated. this will override the open terminal option in the config file")
    parser.add_argument('--ope', dest="openExp", help="Open file explorer after the template is generated. this will override the open file explorer option in the config file")
    args = parser.parse_args();
    if (args.filePath != None and args.lang != None):
        generateProject.generate(args.filePath,args.lang,args.openTerminal,args.openExp)
    elif (args.readConfig != None):
        readConfig.readConfig(args.readConfig)