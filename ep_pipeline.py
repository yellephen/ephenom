import ep_templater
import os

def ProcessHTA(jscriptContent,out):
    print("process hta running")
    contentFileName = "templates/hta.txt"
    try:   
        with open(contentFileName, "r") as contentFile:
            content = contentFile.read()
    except FileNotFoundError:
        print(f"Content file not found: {contentFileName}. Exiting")
        exit()

    content = content.replace("[[[[jscript]]]]",jscriptContent)
    if os.path.exists(out):
        print(f"{out} already exists. Deleting.")
        os.remove(f"{out}")
    with open(f"{out}", 'w') as file:
        file.write(content)
        print(f"HTA written to {out}")
    
def ProcessWordMacro(macroContent,out,wordDocOut):
    contentFileName = "templates/psgenwordmacro.txt"
    try:   
        with open(contentFileName, "r") as contentFile:
            content = contentFile.read()
    except FileNotFoundError:
        print(f"Content file not found: {contentFileName}. Exiting")
        exit()
    content = content.replace("[[[[macro]]]]",macroContent)
    content = content.replace("[[[[wordDocOut]]]]",wordDocOut)
    if os.path.exists(out):
        print(f"{out} already exists. Deleting.")
        os.remove(f"{out}")
    with open(f"{out}", 'w') as file:
        file.write(content)
        print(f"File written to {out}")
    print("Finished generating script.")