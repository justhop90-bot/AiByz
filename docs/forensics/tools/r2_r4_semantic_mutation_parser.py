import os, json
from collections import Counter
ROOT=r"C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai"
PROM=os.path.join(ROOT,"Promisory")
ALL=[os.path.join(ROOT,"AI (HD version).per")]+[os.path.join(PROM,f) for f in sorted(os.listdir(PROM)) if f.endswith(".per")]
ACTIVE={"AI (HD version).per","Promisory/defaultConstants.per","Promisory/finalingConstants.per","Promisory/finaling.per"}
MUT={"set-goal":"GOAL","up-modify-goal":"GOAL","set-strategic-number":"SN","up-modify-sn":"SN","enable-timer":"TIMER","disable-timer":"TIMER","up-set-timer":"TIMER","up-modify-flag":"FLAG","up-modify-group-flag":"GROUP_FLAG"}
def strip_comments(text):
    out=[]; in_str=False; esc=False
    for line in text.splitlines(True):
        b=[]
        for ch in line:
            if in_str:
                b.append(ch)
                if esc: esc=False
                elif ch=='\\': esc=True
                elif ch=='"': in_str=False
            else:
                if ch=='"': in_str=True; b.append(ch)
                elif ch==';': b.append('\n'); break
                else: b.append(ch)
        out.append(''.join(b))
    return ''.join(out)
def tokenize(text):
    t=[]; i=0; ln=1; col=1
    while i<len(text):
        c=text[i]
        if c.isspace():
            if c=='\n': ln+=1; col=1
            else: col+=1
            i+=1; continue
        if c in '()': t.append((c,ln,col)); i+=1; col+=1; continue
        if c=='"':
            sl,sc=ln,col; j=i+1; esc=False
            while j<len(text):
                ch=text[j]
                if esc: esc=False
                elif ch=='\\': esc=True
                elif ch=='"': j+=1; col+=j-i; break
                if ch=='\n': ln+=1; col=0
                j+=1; col+=1
            t.append((text[i:j],sl,sc)); i=j; continue
        sl,sc=ln,col; j=i
        while j<len(text) and not text[j].isspace() and text[j] not in '()': j+=1
        t.append((text[i:j],sl,sc)); col+=j-i; i=j
    return t
def forms(t):
    stack=[]; fs=[]; parent={}
    for i,x in enumerate(t):
        if x[0]=='(':
            if stack: parent[i]=stack[-1]
            stack.append(i)
        elif x[0]==')' and stack: fs.append((stack.pop(),i))
    return sorted(fs),parent
def direct_args(t,s,e):
    a=[]; i=s+2
    while i<e:
        if t[i][0]=='(':
            d=1; j=i+1
            while j<e and d:
                if t[j][0]=='(': d+=1
                elif t[j][0]==')': d-=1
                j+=1
            a.append((i,j-1)); i=j
        else: a.append((i,i)); i+=1
    return a
def span(t,r): return ' '.join(x[0] for x in t[r[0]:r[1]+1])
rows=[]
for p in ALL:
    rel=os.path.relpath(p,ROOT).replace('\\','/')
    text=strip_comments(open(p,encoding='utf-8-sig',errors='replace').read()); t=tokenize(text); fs,pm=forms(t); idx={s:i for i,(s,e) in enumerate(fs)}; info={i:(t[s+1][0] if s+1<e else None,direct_args(t,s,e),s,e) for i,(s,e) in enumerate(fs)}
    for i,(s,e) in enumerate(fs):
        h,args,_,_=info[i]
        if h not in MUT: continue
        pidx=idx.get(pm.get(s)); rule=None; phase=None
        while pidx is not None:
            ph,pa,ps,pe=info[pidx]
            if ph=='defrule':
                rule=f'{rel}:{t[ps][1]}'
                seen=False
                for ar in pa:
                    if ar[0]==ar[1] and t[ar[0]][0]=='=>': seen=True
                    if ar[0]>s: break
                phase='ACTION' if seen else 'CONDITION'; break
            pidx=idx.get(pm.get(fs[pidx][0]))
        target=span(t,args[0]) if args else None; rhs=[span(t,a) for a in args[1:]]
        rows.append({'file':rel,'line':t[s][1],'head':h,'kind':MUT[h],'target':target,'args':rhs,'rule':rule,'phase':phase,'raw':span(t,(s,e))})
print('CORPUS_FILES',len(ALL)); print('CORPUS_MUTATIONS',len(rows)); print('CORPUS_HEADS',json.dumps(dict(Counter(r['head'] for r in rows)),sort_keys=True)); print('CORPUS_PHASES',json.dumps({str(k):v for k,v in Counter(r['phase'] for r in rows).items()},sort_keys=True)); print('ACTIVE4_MUTATIONS',sum(r['file'] in ACTIVE for r in rows)); print('ACTIVE4_BY_HEAD',json.dumps(dict(Counter(r['head'] for r in rows if r['file'] in ACTIVE)),sort_keys=True))
for target in ['sn-cavalry-threat','retreat-now-goal','attack-status-goal','restart-attack-goal','temporary-goal2','cavarchers']:
    rs=[r for r in rows if r['target']==target]; print('TARGET',target,'COUNT',len(rs)); [print(r['file'],r['line'],r['phase'],r['head'],r['args'],r['rule']) for r in rs[:80]]
