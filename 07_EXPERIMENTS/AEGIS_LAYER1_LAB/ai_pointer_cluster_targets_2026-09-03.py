import pefile, struct
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
EXE = r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe'
BASE = 0x140000000
TARGETS = [0x1431CBE18, 0x1431CC6B0]
pe = pefile.PE(EXE, fast_load=True)
raw = open(EXE, 'rb').read()
pdata = next(s for s in pe.sections if s.Name.rstrip(b'\0') == b'.pdata')
ranges = []
for i in range(0, pdata.SizeOfRawData - 11, 12):
    a, b, _ = struct.unpack_from('<III', raw, pdata.PointerToRawData + i)
    if a and b and a < b:
        ranges.append((BASE+a, BASE+b))
starts = {a for a, _ in ranges}
def fn_for(va):
    for a,b in ranges:
        if a <= va < b: return a,b
    return None
rdata = next(s for s in pe.sections if s.Name.rstrip(b'\0') == b'.rdata')
for t in TARGETS:
    off = rdata.PointerToRawData + (t-BASE-rdata.VirtualAddress)
    print('\nTARGET %016X' % t)
    for j in range(-8,9):
        o=off+j*8; q=struct.unpack_from('<Q',raw,o)[0]
        print('%016X  %016X' % (t+j*8,q))
    q=struct.unpack_from('<Q',raw,off)[0]
    f=fn_for(q)
    if f:
        print('FUNCTION %016X-%016X SIZE=%d' % (f[0],f[1],f[1]-f[0]))
        sec=next(s for s in pe.sections if s.VirtualAddress <= f[0]-BASE < s.VirtualAddress+s.SizeOfRawData)
        ro=sec.PointerToRawData+(f[0]-BASE-sec.VirtualAddress)
        md=Cs(CS_ARCH_X86,CS_MODE_64)
        for ins in md.disasm(raw[ro:ro+(f[1]-f[0])],f[0]):
            print('  %016X %-7s %s' % (ins.address,ins.mnemonic,ins.op_str))
