import pefile, struct
EXE = r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe'
BASE = 0x140000000
LO = 0x31C0000
HI = 0x31D0000
pe = pefile.PE(EXE, fast_load=True)
raw = open(EXE, 'rb').read()
pdata = next(s for s in pe.sections if s.Name.rstrip(b'\0') == b'.pdata')
starts = set()
for i in range(0, pdata.SizeOfRawData - 11, 12):
    a, b, _ = struct.unpack_from('<III', raw, pdata.PointerToRawData + i)
    if a and b and a < b:
        starts.add(a)
rdata = next(s for s in pe.sections if s.Name.rstrip(b'\0') == b'.rdata')
start_raw = rdata.PointerToRawData + (LO - rdata.VirtualAddress)
end_raw = rdata.PointerToRawData + (HI - rdata.VirtualAddress)
hits = []
for o in range(start_raw, end_raw - 7, 8):
    q = struct.unpack_from('<Q', raw, o)[0]
    rva = q - BASE
    if rva in starts:
        hits.append((BASE + (o - start_raw + LO), q))
print('BUILD=6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4')
print('RANGE=VA %016X-%016X' % (BASE + LO, BASE + HI))
print('POINTER_HITS=%d' % len(hits))
for where, target in hits:
    print('%016X -> %016X' % (where, target))

print('STRICT_TARGET_CHECK', 'BCEB00', (0x0BCEB00 in starts), 'BCEB20', (0x0BCEB20 in starts))
