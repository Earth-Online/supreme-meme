from lief import PE

a   = "tinyPE\0"
code = [
        0x6A, 0x00,                         # push 0 uExitCode
        0xFF, 0x15, 0x4C, 0x30, 0x40, 0x00  # call ExitProcess
]

data =  list(map(ord, a))

binary32 = PE.Binary("testpe", PE.PE_TYPE.PE32)

section_text                 = PE.Section(".text")
section_text.content         = code
section_text.virtual_address = 0x1000

section_data                 = PE.Section(".data")
section_data.content         = data
section_data.virtual_address = 0x2000

section_text = binary32.add_section(section_text, PE.SECTION_TYPES.TEXT)
section_data = binary32.add_section(section_data, PE.SECTION_TYPES.DATA)

binary32.optional_header.addressof_entrypoint = section_text.virtual_address

#
kernel32 = binary32.add_library("kernel32.dll")
kernel32.add_entry("ExitProcess")
ExitProcess_addr = binary32.predict_function_rva("kernel32.dll", "ExitProcess")
#

builder = PE.Builder(binary32)
builder.build_imports(True)
builder.build()
builder.write("testper0.exe")