import pefile,struct
EXE=r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe'; BASE=0x140000000; TARGETS=[0x140BCEB00,0x140BCEB10,0x140BCEB20,0x140BCEBA0,0x140BCEBB0,0x140BCEBC0]
p=pefile.PE(EXE,fast_load=True); raw=open(EXE,'rb').read(); mm=p.get_memory_mapped_image(); d=p.OPTIONAL_HEADER.DATA_DIRECTORY[3]; sec=next(s for s in p.sections if s.Name.rstrip(b'\0')==b'.pdata')
def starts(buf,off,n):
 out=set()
 for i in range(0,n-11,12):
  a,b,u=struct.unpack_from('<III',buf,off+i)
  if a and b and a<b: out.add(a)
 return out
A=starts(raw,sec.PointerToRawData,d.Size); B=starts(mm,d.VirtualAddress,d.Size)
print('DIRECTORY',hex(d.VirtualAddress),hex(d.Size),'SECTION_RAW',hex(sec.PointerToRawData),hex(sec.SizeOfRawData))
print('COUNTS raw=%d mapped=%d equal=%s'%(len(A),len(B),A==B))
for va in TARGETS:
 r=va-BASE; print('%016X raw=%s mapped=%s'%(va,r in A,r in B))
