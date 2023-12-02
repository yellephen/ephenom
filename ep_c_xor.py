import re

def run(shellCode,templateValues):

    
    shellCode = shellCode.replace("unsigned char buf[] = ","")
    shellCode = shellCode.replace("\"","")
    shellCode = shellCode.replace("\n","")
    shellCode = shellCode.replace(";","")

    xor_value = ord(templateValues["xorChar"])
    print(shellCode)
    shell_bytes = bytes.fromhex(shellCode.replace('\\x', ''))
    
    output_string = bytes(x ^ xor_value for x in shell_bytes)
    output_string = ''.join(f'{b:02x}' for b in output_string)
    output_string  = ''.join('\\x'+output_string[i:i+2] for i in range(0, len(output_string ), 2))

                    
    return "unsigned char buf[] =\"" + output_string + "\";"