import os,json
from collections import Counter
ROOT=r"C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai"
PROM=os.path.join(ROOT,"Promisory")
FILES=[os.path.join(ROOT,"AI (HD version).per")]+[os.path.join(PROM,f) for f in sorted(os.listdir(PROM)) if f.endswith(".per")]
MUT={"set-goal":"GOAL","up-modify-goal":"GOAL","set-strategic-number":"SN","up-modify-sn":"SN","enable-timer":"TIMER","disable-timer":"TIMER","up-set-timer":"TIMER","up-modify-flag":"FLAG","up-modify-group-flag":"GROUP_FLAG"}

def strip_comments(text):
    out=[];ins=False;esc=False
    for line in text.splitlines(True):
        b=[]
        for c in line:
            if ins:
                b.append(c)
                if esc: esc=False
                elif c=='\\': esc=True
                elif c=='"': ins=False
            elif c=='"': ins=True;b.append(c)
            elif c==';': b.append('\n');break
            else:b.append(c)
        out.append(''.join(b))
    return ''.join(out)

def tokenize(text):
    t=[];i=0;ln=1;col=1
    while i<len(text):
        c=text[i]
        if c.isspace():
            if c=='\n':ln+=1;col=1
            else:col+=1
            i+=1;continue
        if c in '()':t.append((c,ln,col));i+=1;col+=1;continue
        if c=='"':
            sl,sc=ln,col;j=i+1;esc=False
            while j<len(text):
                ch=text[j]
                if esc:esc=False
                elif ch=='\\':esc=True
                elif ch=='"':j+=1;break
                if ch=='\n':ln+=1;col=0
                j+=1;col+=1
            t.append((text[i:j],sl,sc));col+=j-i;i=j;continue
        sl,sc=ln,col;j=i
        while j<len(text) and not text[j].isspace() and text[j] not in '()':j+=1
        t.append((text[i:j],sl,sc));col+=j-i;i=j
    return t

def forms(t):
    stack=[];fs=[];parent={}
    for i,x in enumerate(t):
        if x[0]=='(':
            if stack:parent[i]=stack[-1]
            stack.append(i)
        elif x[0]==')' and stack:fs.append((stack.pop(),i))
    return fs,parent

def args(t,s,e):
    out=[];i=s+1
    while i<e:
        if t[i][0]=='(':
            d=1;j=i+1
            while j<e and d:
                if t[j][0]=='(':d+=1
                elif t[j][0]==')':d-=1
                j+=1
            out.append((i,j));i=j
        else:out.append((i,i+1));i+=1
    return out

def text(t,a,b):return ' '.join(x[0] for x in t[a:b])

def main():
    rows=[]
    for p in FILES:
        rel=os.path.relpath(p,ROOT).replace('\\','/')
        t=tokenize(strip_comments(open(p,encoding='utf-8-sig',errors='replace').read()))
        fs,par=forms(t); by_start={s:(s,e) for s,e in fs}
        info={s:(t[s+1][0] if s+1<e else None,args(t,s,e),s,e) for s,e in fs}
        for s,e in fs:
            h,aa,_,_=info[s]
            if h not in MUT:continue
            cur=par.get(s);rule=None
            while cur is not None:
                ph,pa,ps,pe=info[cur]
                if ph=='defrule':
                    rule=f'{rel}:{t[ps][1]}'
                    parts=[text(t,a[0],a[1]) for a in pa]
                    try:k=parts.index('=>')
                    except ValueError:k=len(parts)
                    cond=parts[:k];act=parts[k+1:] if k<len(parts) else []
                    break
                cur=par.get(cur)
            aa=args(t,s,e)
            rows.append({'file':rel,'line':t[s][1],'head':h,'kind':MUT[h],
                         'target':text(t,aa[1][0],aa[1][1]) if len(aa)>1 else None,
                         'rhs':[text(t,a[0],a[1]) for a in aa[2:]],
                         'rule':rule,'conditions':cond if rule else [],
                         'action_context':act if rule else [],
                         'raw':text(t,s,e)})
    out=r'C:\Users\justh\Desktop\AEGIS-AI-LAB\R2_R4_JOIN_WORK\semantic_mutation_rule_scope.jsonl'
    with open(out,'w',encoding='utf-8',newline='\n') as f:
        for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    print('ROWS',len(rows));print('RULES',len(set(r['rule'] for r in rows)));print('MISSING_RULE',sum(r['rule'] is None for r in rows));print('EMPTY_COND',sum(not r['conditions'] for r in rows))
    for target in ['sn-cavalry-threat','retreat-now-goal','attack-status-goal','restart-attack-goal','cavarchers','temporary-goal2']:
        q=[r for r in rows if r['target']==target];print('TARGET',target,'ROWS',len(q),'RULES',len(set(r['rule'] for r in q)))
        for r in q[:20]:print(r['file'],r['line'],r['head'],r['rule'])
if __name__=='__main__':main()
