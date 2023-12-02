import os
import json

# Get the current directory
current_directory = os.getcwd()
# List all JSON files in the current directory
json_files = [file for file in os.listdir(current_directory+"/templates") if file.endswith('.json')]
# Iterate through each JSON file and print the filename and content of "contentFile"

for file_name in json_files:
    print(f"File Name: {file_name}")
    try:
        with open("./templates/"+file_name, 'r') as json_file:
            data = json.load(json_file)
            if "contentFile" in data:
                content = data["contentFile"]
                exists = "[x]Content File does not exist."
                if os.path.exists("./templates/"+content):
                    exists = "Content File exists."         
                print(f"contentFile: {content}")
                print(exists)
                if content.replace(".txt","") != file_name.replace(".json",""):
                    print("[w]Content File name mismatched.")
                print("\n")
    except:
        print("\n")
        print("[x]File " + file_name + " failed to load. Might be empty.")
        print("\n")
