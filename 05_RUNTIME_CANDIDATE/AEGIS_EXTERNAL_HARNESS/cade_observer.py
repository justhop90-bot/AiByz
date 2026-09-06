import argparse,json,time,urllib.request,hashlib
from pathlib import Path
import websocket
def page():
    return next(x for x in json.load(urllib.request.urlopen('http://127.0.0.1:45678/json')) if x.get('type')=='page' and x.get('url','').startswith('cafile://'))
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('-o',required=True); ap.add_argument('-d',type=float,default=15); ap.add_argument('--interval',type=float,default=.02); a=ap.parse_args()
    t=page(); w=websocket.create_connection(t['webSocketDebuggerUrl'],timeout=5); seq=0
    def ev(expr):
        nonlocal seq
        seq+=1; w.send(json.dumps({'id':seq,'method':'Runtime.evaluate','params':{'expression':expr,'awaitPromise':True,'returnByValue':True}}))
        while True:
            m=json.loads(w.recv())
            if m.get('id')==seq:return m.get('result',{}).get('result',{}).get('value')
    out=Path(a.o); out.parent.mkdir(parents=True,exist_ok=True); n=nn=0; start=time.monotonic()
    with out.open('w',encoding='utf-8') as f:
        f.write(json.dumps({'record_type':'header','schema':'AEGIS-CADE-RAW-OBSERVER-v1','target_page':t['url'],'started_unix':time.time()})+'\n')
        while time.monotonic()-start<a.d:
            v=ev('ipcNamedPipeEndpoint.poll()'); f.write(json.dumps({'record_type':'poll','host_unix_ns':time.time_ns(),'value':v},ensure_ascii=False,separators=(',',':'))+'\n'); n+=1; nn+=v is not None; time.sleep(a.interval)
    w.close(); data=out.read_bytes(); s={'schema':'AEGIS-CADE-RAW-OBSERVER-v1','records':n,'non_null_polls':nn,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}; out.with_suffix(out.suffix+'.summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8'); print(json.dumps(s,indent=2))
if __name__=='__main__': main()
