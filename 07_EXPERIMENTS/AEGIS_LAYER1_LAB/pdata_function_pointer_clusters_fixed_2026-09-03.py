import pefile,struct
EXE=r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\AoE2DE_s.exe'; BASE=0x140000000
p=pefile.PE(EXE,fast_load=True); raw=open(EXE,'rb').read(); d=p.OPTIONAL_HEADER.DATA_DIRECTORY[3]; ps=next(s for s in p.sections if s.Name.rstrip(b'\0')==b'.pdata')
starts=set()
for i in range(0,d.Size,12):
 a,b,_=struct.unpack_from('<III',raw,ps.PointerToRawData+i)
 if a and b and a<b: starts.add(a)
clusters=[]
for s in p.sections:
 name=s.Name.rstrip(b'\0').decode('latin1')
 if name not in ('.rdata','.data'): continue
 lo=s.PointerToRawData; hi=lo+s.SizeOfRawData; o=lo
 while o+8<=hi:
  q=struct.unpack_from('<Q',raw,o)[0]; r=q-BASE
  if r in starts:
   st=o; vals=[]
   while o+8<=hi:
    q=struct.unpack_from('<Q',raw,o)[0]
    if q-BASE not in starts: break
    vals.append(q); o+=8
   if len(vals)>=4: clusters.append((len(vals),name,BASE+s.VirtualAddress+(st-s.PointerToRawData),vals))
  else: o+=8
clusters.sort(key=lambda x:(-x[0],x[1],x[2]))
print('BUILD=6378CA6F1FBD2F230B5B7F2CD048198331848AF70F44B5CD13CEB89420A321A4')
print('PDataStarts=%d Clusters>=4=%d'%(len(starts),len(clusters)))
for n,sec,va,vals in clusters[:80]: print('%3d %s VA=%016X targets=%s'%(n,sec,va,','.join('%016X'%x for x in vals[:8])))
print('AI_REGION_CLUSTERS')
for n,sec,va,vals in clusters:
    if 0x1431C0000 <= va < 0x1431D0000:
        print('%3d %s VA=%016X targets=%s'%(n,sec,va,','.join('%016X'%x for x in vals[:16])))
