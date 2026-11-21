"""LLM Wiki lint（機械檢查）：python3 tools/lint.py wiki
連結格式：[顯示文字](相對路徑.md)。語意檢查（矛盾、相近概念對照）由 agent 判斷。"""
import re, glob, os, sys
root = sys.argv[1] if len(sys.argv) > 1 else 'wiki'
os.chdir(root)
files = sorted(glob.glob('**/*.md', recursive=True))
stem = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
mdlink = re.compile(r'\]\(([^)\s#]+\.md)(?:#[^)]*)?\)')
read = {f: open(f, encoding='utf-8').read() for f in files}

def targets(f):
    out = []
    for m in mdlink.findall(read[f]):
        out.append(os.path.normpath(os.path.join(os.path.dirname(f), m)))
    return out

inc = {f: set() for f in files}; out = {f: set() for f in files}; broken = []
for f in files:
    for t in targets(f):
        if t not in read: broken.append((f, t)); continue
        out[f].add(t)
        if f not in ('index.md', 'log.md'): inc[t].add(f)
skip = {'index.md', 'log.md'}
print('BROKEN', broken)
print('LEFTOVER [[wikilinks]]', [f for f in files if '[[' in read[f]])
print('ORPHAN(no incoming except index)', [f for f in files if f not in skip and not inc[f]])
print('NO OUTGOING', [f for f in files if f not in skip and not out[f]])
print('NO FRONTMATTER', [f for f in files if f != 'log.md' and not read[f].startswith('---')])
print('NO 白話版', [f for f in files if f.startswith('concepts/') and '白話版' not in read[f]])
gl = set(targets('glossary.md'))
print('NOT IN GLOSSARY', [f for f in files if f.startswith('concepts/') and f not in gl])
print('SOURCE MISSING SECTIONS', [f for f in files if f.startswith('sources/') and not all(k in read[f] for k in ('## 設計決策與消融證據', '## 作者提到的限制與未來方向', '## 矛盾'))])
idx = set(targets('index.md'))
print('NOT IN INDEX', [f for f in files if f not in skip and f not in idx])
print('MISSING summary', [f for f in files if f not in skip and 'summary:' not in read[f].split('---')[1]])
num = re.compile(r'\d+\.\d|\d{2,}'); cite = re.compile(r'p\.\s?\d|Table|Fig\.')
print('--- numeric lines w/o citation (請人工確認是否需補出處)')
for f in files:
    if f in ('log.md', 'index.md', 'glossary.md'): continue
    inblk = False
    for i, l in enumerate(read[f].split('\n'), 1):
        if l.startswith('```'): inblk = not inblk; continue
        if inblk or l.startswith('|---') or l.startswith('#') or (i < 15 and re.match(r'^[a-z-]+:', l)): continue
        l2 = re.sub(r'\[[^\]]*\]\([^)]*\)', '', l)
        if num.search(l2) and not cite.search(l2): print(f'{f}:{i}: {l[:110]}')
