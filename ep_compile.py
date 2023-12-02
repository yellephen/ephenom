import subprocess
import os
import ep_gensc
import ep_pipeline

def compile(template,content):
    attributes = getAttributes(template)
    if template["compilationType"] == "csharp":
        if os.path.exists("temp.cs"):
            print("temp.cs already exists. Deleting.")
            os.remove("temp.cs")
        with open("temp.cs", 'w') as file:
            file.write(content)
        
        target = template["target"]
        arch = attributes["architecture"]
        out = attributes["saveAs"]

        command = f"mcs temp.cs -target:{target} -platform:{arch} -out:{out}"

        if "requiredAssemblies" in template:
            for dll in template["requiredAssemblies"]:
                command += f" -r:{dll}"     
                    
        process = subprocess.run(command, shell=True, universal_newlines=True)
        print(process)
        if process.returncode != 0:
            print("Compiling failed. Exiting.")
            exit()
        else:
            print("Compilation successful.")

    elif template["compilationType"] == "macro":
         print("Not implemented yet. Printing payload.")
         print(content);
    elif template["compilationType"] == "C":
        if os.path.exists("temp.c"):
            print("temp.c already exists. Deleting.")
            os.remove("temp.c")
        with open("temp.c", 'w') as file:
            file.write(content)

        out = attributes["saveAs"]
    
        command = f"gcc -static -o {out} temp.c -z execstack"

        process = subprocess.run(command, shell=True, universal_newlines=True)
        print(process)
        if process.returncode != 0:
            print("Compiling failed. Exiting.")
            exit()
        else:
            print("Compilation successful.")

    elif template["compilationType"] == "jscript":    
        if os.path.exists("temp.cs"):
            print("temp.cs already exists. Deleting.")
            os.remove("temp.cs")
        with open("temp.cs", 'w') as file:
            file.write(content)
        
        target = template["target"]
        arch = attributes["architecture"]
        out = attributes["saveAs"]
        jsout = attributes["saveJSAs"]
        command = f"mcs temp.cs -target:{target} -platform:{arch} -out:{out}"
  
        process = subprocess.run(command, shell=True, universal_newlines=True)
        print(process)

        if attributes["format"] == "js":
            command2 = f"mono DotNetToJScriptFixed4Mono.exe {out} --lang=Jscript --ver=v4 -o {jsout}"

            process2 = subprocess.run(command2,shell=True)
            print(process2)

        elif attributes["format"] == "hta":
            command2 = f"mono DotNetToJScriptFixed4Mono.exe {out} --lang=Jscript --ver=v4"
            jscriptContent = subprocess.check_output(command2,shell=True,text=True)
            jscriptContent = jscriptContent.replace("WARNING: The runtime version supported by this application is unavailable.","")
            jscriptContent = jscriptContent.replace("Using default runtime: v4.0.30319","")
            ep_pipeline.ProcessHTA(jscriptContent,jsout)

    else:
        print("Compilation type unknown, printing payload.")
        print(content)

def getAttributes(template):
    attributes = {}
    if "compilationAttributes" in template:
        for compAtt in template["compilationAttributes"]:
            name = compAtt["name"]
            description = compAtt["description"]
            defaultValue = compAtt["defaultValue"]
            print(f"Compilation attribute [{name}] must be populated. Default value is [{defaultValue}]. Enter value, press enter for default, or !describe! to print description.")
            choice = input("> ")
            if choice == "!describe!":
                print(description)
                print(f"Custom attribute [{name}] must be populated. Default value is [{defaultValue}]. Enter value, press enter for default.")
                choice = input("> ")           
            if choice == "":
                choice = defaultValue
            attributes[f"{name}"] = choice
    return attributes