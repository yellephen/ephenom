import re

def xor(shellCode,xorInt):

    pattern = r'\{([^}]*)\}'
    match = re.search(pattern, shellCode)

    if match:
        shellCode = match.group(1)
        
    else:
        print("Error processing shell code in xor operation. Exiting.")
        exit()

    hex_bytes = shellCode.split(',')
    int_bytes = [int(byte, 16) for byte in hex_bytes]

    output = ""
    counter = 0

    for byte in int_bytes:
        counter = counter + 1
        output += (str(int(xorInt ^ byte)) + ", ")
        if counter % 50 == 0:
            output += "_ \r\n"
            
    return output[:-2]
