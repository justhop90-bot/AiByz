import pefile, struct
from capstone import Cs, CS_ARCH_X86, CS_MODE_64
EXE = r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe'
BASE = 0x140000000
TARGETS = [0x140BCEB00,0x140BCEB10,0x140BCEB20,0x140BCEBA0,0x140BCEBB0,0x140BCEBC0]
pe = pefile.PE(EXE, fast_load=True); raw=open(EXE,'rb').read()
pdata=next(s for s in pe.sections if s.Name.rstrip(b'\0')==b'.pdata'); ranges=[]
for i in range(0,pdata.SizeOfRawData-11,12):
 a,b,_=struct.unpack_from('<III',raw,pdata.PointerToRawData+i)
 if a and b and a<b:ranges.append((BASE+a,BASE+b))
def fn(va): return next(((a,b) for a,b in ranges if a<=va<b),None)
md=Cs(CS_ARCH_X86,CS_MODE_64)
for va in TARGETS:
 f=fn(va); print('\nFUNCTION %016X' % va)
 if not f: print('NO_PDATA'); continue
 print('RANGE %016X-%016X SIZE=%d'%(f[0],f[1],f[1]-f[0]))
 s=next(s for s in pe.sections if s.VirtualAddress <= f[0]-BASE < s.VirtualAddress+s.SizeOfRawData)
 o=s.PointerToRawData+(f[0]-BASE-s.VirtualAddress)
 for ins in md.disasm(raw[o:o+(f[1]-f[0])],f[0]): print('%016X %-7s %s'%(ins.address,ins.mnemonic,ins.op_str))
