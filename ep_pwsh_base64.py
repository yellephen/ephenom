import base64
import subprocess

def run(content):
    command = f"./ep_b64.ps1 -content \"" + content + "\""
    process = subprocess.run(command, shell=True, universal_newlines=True,stdout=subprocess.PIPE)
     
    if process.returncode == 0:
        print("b64 ran successfully.")
        print("powershell -enc " +process.stdout)
        return ""
    else:
        print("b64 failed. exiting")
        exit() 