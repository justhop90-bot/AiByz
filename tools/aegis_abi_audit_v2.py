#!/usr/bin/env python3
"""Channel-aware deterministic AEGIS .per namespace audit."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

LOAD_RE = re.compile(r'\(load\s+"([^"]+)"\)', re.I)
DEFCONST_RE = re.compile(r'\(defconst\s+([^\s()]+)\s+([^\s()]+)', re.I)
NUM_RE = re.compile(r"-?\d+$")
GOAL_OP_RE = re.compile(r'\((set-goal|goal|up-modify-goal|up-compare-goal)\s+([^\s()]+)', re.I)

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def closure(root: Path, entry: Path):
    found={}; stack=[entry]
    while stack:
        p=stack.pop(); rel=p.relative_to(root).as_posix()
        if rel in found: continue
        found[rel]=p
        for raw in LOAD_RE.findall(p.read_text(encoding='utf-8',errors='replace')):
            q=root/raw.replace('\\','/')
            if not q.suffix: q=q.with_suffix('.per')
            if q.exists(): stack.append(q)
    return [found[k] for k in sorted(found)]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--ai-root',required=True,type=Path); ap.add_argument('--entrypoint',default='AI (HD version).per'); ap.add_argument('--out',required=True,type=Path); a=ap.parse_args()
    root=a.ai_root.resolve(); files=closure(root,(root/a.entrypoint).resolve()); defs={}; decl=[]
    for p in files:
        text=p.read_text(encoding='utf-8',errors='replace'); digest=sha256(p)
        for n,line in enumerate(text.splitlines(),1):
            m=DEFCONST_RE.search(line)
            if m:
                row={'symbol':m.group(1),'value':m.group(2),'file':p.relative_to(root).as_posix(),'line':n,'sha256':digest}
                decl.append(row); defs.setdefault(row['symbol'],[]).append(row)
    goal_refs=[]
    for p in files:
        for n,line in enumerate(p.read_text(encoding='utf-8',errors='replace').splitlines(),1):
            m=GOAL_OP_RE.search(line)
            if not m: continue
            goal_refs.append({'op':m.group(1),'operand':m.group(2),'file':p.relative_to(root).as_posix(),'line':n})
    resolved=[]
    for ref in goal_refs:
        vals=defs.get(ref['operand'],[])
        if vals:
            for d in vals:
                if NUM_RE.fullmatch(d['value']): resolved.append({**ref,'numeric_id':int(d['value']),'definition':d})
        elif NUM_RE.fullmatch(ref['operand']): resolved.append({**ref,'numeric_id':int(ref['operand']),'definition':None})
    high=[r for r in resolved if 512<=r['numeric_id']<=16000]
    a.out.mkdir(parents=True,exist_ok=True)
    manifest={'entrypoint':a.entrypoint,'file_count':len(files),'declaration_rows':len(decl),'unique_symbols':len(defs),'numeric_declarations':sum(bool(NUM_RE.fullmatch(d['value'])) for d in decl),'resolved_goal_operands':len(resolved),'resolved_high_goal_operands':len(high),'closure':[{'path':p.relative_to(root).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p)} for p in files]}
    (a.out/'snapshot_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding='utf-8')
    (a.out/'symbol_inventory.jsonl').write_text(''.join(json.dumps(d,sort_keys=True)+'\n' for d in decl),encoding='utf-8')
    (a.out/'goal_reference_inventory.jsonl').write_text(''.join(json.dumps(r,sort_keys=True)+'\n' for r in resolved),encoding='utf-8')
    (a.out/'import_closure.json').write_text(json.dumps([p.relative_to(root).as_posix() for p in files],indent=2),encoding='utf-8')
    report=['# AEGIS Channel-Aware ABI Audit v2','',f"Closure files: **{len(files)}**",f"Declaration rows: **{len(decl)}**",f"Unique symbols: **{len(defs)}**",f"Resolved goal operands: **{len(resolved)}**",f"Resolved high goal operands (512–16000): **{len(high)}**",'','## Critical rule','','Numeric defconst values are not automatically goal-channel occupancy. A value such as `heavy-wood=10000` is a constant value and becomes a goal identifier only when used in a goal-typed parameter position.','']
    if high: report += ['## Resolved high goal operands']+[f"- `{r['numeric_id']}` via `{r['operand']}` at `{r['file']}:{r['line']}`" for r in high]
    else: report += ['## Resolved high goal operands','','**None found in the exact HD closure.**']
    report += ['','Numeric ABI remains unresolved until validator, build-specific legality, ownership, generation, and publication gates pass.']
    (a.out/'audit_report.md').write_text('\n'.join(report)+'\n',encoding='utf-8')
    outputs=sorted(a.out.glob('*')); (a.out/'RUN_MANIFEST.sha256').write_text('\n'.join(f"{sha256(p)}  {p.name}" for p in outputs)+'\n',encoding='utf-8')
    print(json.dumps(manifest,indent=2,sort_keys=True)); return 0

if __name__=='__main__': raise SystemExit(main())
