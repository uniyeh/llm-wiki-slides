"""LLM Wiki lint：python3 tools/lint.py wiki"""
import re,glob,os,sys
root=sys.argv[1]; os.chdir(root)
files=[f for f in glob.glob('**/*.md',recursive=True)]
stem={os.path.splitext(os.path.basename(f))[0]:f for f in files}
link=re.compile(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]')
inc={s:set() for s in stem}; out={s:set() for s in stem}; broken=[]
for f in files:
    s=os.path.splitext(os.path.basename(f))[0]; t=open(f).read()
    for m in link.findall(t):
        m=m.strip()
        if m not in stem: broken.append((f,m))
        else:
            out[s].add(m)
            if s not in('index','log'): inc[m].add(s)
print('BROKEN',broken)
skip={'index','log'}
print('ORPHAN(no incoming except index)',[s for s in stem if s not in skip and not inc[s]])
print('NO OUTGOING',[s for s in stem if s not in skip and not out[s]])
print('NO FRONTMATTER',[f for f in files if f!='log.md' and not open(f).read().startswith('---')])
print('NO 白話版',[f for f in files if f.startswith('concepts/') and '白話版' not in open(f).read()])
gl=open('glossary.md').read()
print('NOT IN GLOSSARY',[s for s,f in stem.items() if f.startswith('concepts/') and f'[[{s}]]' not in gl])
print('SOURCE MISSING SECTIONS',[f for f in files if f.startswith('sources/') and not all(k in open(f).read() for k in ('## 設計決策與消融證據','## 作者提到的限制與未來方向','## 矛盾'))])
print('NOT IN INDEX',[s for s in stem if s not in skip and f'[[{s}]]' not in open('index.md').read()])
num=re.compile(r'\d+\.\d|\d{2,}')
cite=re.compile(r'p\.\s?\d|Table|Fig\.')
print('--- numeric lines w/o citation')
for f in files:
    if f in('log.md','index.md','glossary.md'): continue
    inblk=False
    for i,l in enumerate(open(f).read().split('\n'),1):
        if l.startswith('---') and i<15: continue
        if re.match(r'^(title|venue|raw|updated|sources|tags|aliases|type|slide-role|name):',l): continue
        if l.startswith('```'): inblk=not inblk; continue
        if inblk or l.startswith('|---') or l.startswith('#'): continue
        l2=re.sub(r'\[\[[^\]]*\]\]','',l)
        if num.search(l2) and not cite.search(l2):
            print(f'{f}:{i}: {l[:110]}')
