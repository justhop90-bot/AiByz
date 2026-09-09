import json,re
from pathlib import Path
ROOT=Path(r'C:\Program Files (x86)\Steam\steamapps\common\AoE2DE\resources\_common\ai'); PROM=ROOT/'Promisory'
FILES=[ROOT/'AI (HD version).per']+sorted(PROM.glob('*.per'))
MUT={'set-goal':'GOAL','up-modify-goal':'GOAL','set-strategic-number':'SN','up-modify-sn':'SN','enable-timer':'TIMER','disable-timer':'TIMER','up-set-timer':'TIMER','up-modify-flag':'FLAG','up-modify-group-flag':'GROUP_FLAG'}
pat=re.compile(r'\((set-goal|up-modify-goal|set-strategic-number|up-modify-sn|enable-timer|disable-timer|up-set-timer|up-modify-flag|up-modify-group-flag)\s+([^\s()]+)((?:\s+[^()]*)*)\)')
def strip(line):
 q=[];quoted=False;esc=False
 for c in line:
  if quoted:
   q.append(c)
   if esc: esc=False
   elif c=='\\': esc=True
   elif c=='"': quoted=False
  elif c=='"': quoted=True;q.append(c)
  elif c==';': break
  else:q.append(c)
 return ''.join(q)
def main():
 rows=[]
 for p in FILES:
  rel=p.relative_to(ROOT).as_posix(); raw=p.read_text(encoding='utf-8-sig',errors='replace').splitlines()
  depth=0; rule=None; rule_start=None; rule_buf=[]; in_action=False
  for ln,orig in enumerate(raw,1):
   line=strip(orig); low=line.strip()
   if not line: continue
   if '(defrule' in line and rule is None:
    rule=f'{rel}:{ln}';rule_start=ln;rule_buf=[];in_action=False
   if rule is not None:
    rule_buf.append(line)
    if '=>' in line: in_action=True
    for m in pat.finditer(line):
     # Exclude occurrences after comment via strip(); nested mutation forms are retained.
     target=m.group(2); rhs=m.group(3).strip()
     rows.append({'file':rel,'line':ln,'head':m.group(1),'kind':MUT[m.group(1)],'target':target,'rhs':rhs,'rule':rule,'conditions':[] if in_action or '=>' in line and m.start()>line.find('=>') else list(rule_buf)})
   # lexical paren balance on code-only line; reset at completed rule
   depth += line.count('(')-line.count(')')
   if rule is not None and depth<=0 and '(defrule' in '\n'.join(rule_buf):
    # Attach exact condition text to rows belonging to this rule.
    cond=[]
    for x in rule_buf:
     if '=>' in x: cond.append(x.split('=>',1)[0].strip());break
     cond.append(x)
    for r in reversed(rows):
     if r['rule']==rule and not r['conditions']: r['conditions']=cond
     elif r['rule']!=rule: break
    rule=None;rule_start=None;rule_buf=[];in_action=False;depth=0
 out=Path(r'C:\Users\justh\Desktop\AEGIS-AI-LAB\R2_R4_JOIN_WORK');out.mkdir(exist_ok=True)
 fp=out/'semantic_mutation_rule_scope_fast.jsonl'
 with fp.open('w',encoding='utf-8',newline='\n') as f:
  for r in rows:f.write(json.dumps(r,ensure_ascii=False)+'\n')
 print('ROWS',len(rows));print('OUT',fp)
 for t in ['sn-cavalry-threat','retreat-now-goal','attack-status-goal','restart-attack-goal','cavarchers','temporary-goal2']:
  q=[r for r in rows if r['target']==t];print(t,len(q))
  for r in q[:20]:print(json.dumps(r,ensure_ascii=False))
if __name__=='__main__':main()
