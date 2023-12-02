import re

def run(shellCode,templateValues):

    xorInt = int(templateValues["xorByte"],16)

    pattern = r'byte\[\] buf = new byte\[(\d+)\]'
    match = re.search(pattern,shellCode)

    if match:
        scLength = match.group(1)
    else:
        print("Error processing shell code in xor operation. Exiting.")
        exit()

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

    for byte in int_bytes:
        result = xorInt ^ byte
        output += "0x{:02X}".format(result) + ","
                    
    return "byte[] buf = new byte[" + scLength + "] {" +output[:-1] + "};"