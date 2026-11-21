"""產生 wiki/index.md（樹狀、可點擊的 markdown 相對連結）。
用法：python3 tools/build_index.py wiki
每頁 frontmatter 需有 title、type、summary；order（數字，小的在前）可選。"""
import os, re, sys, glob, datetime
root = sys.argv[1] if len(sys.argv) > 1 else 'wiki'
os.chdir(root)

def fm(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---', t, re.S)
    d = {}
    if m:
        for line in m.group(1).split('\n'):
            if ':' in line:
                k, v = line.split(':', 1); d[k.strip()] = v.strip()
    return d

pages = []
for f in sorted(glob.glob('**/*.md', recursive=True)):
    if f in ('index.md',): continue
    d = fm(f)
    pages.append(dict(path=f, stem=os.path.splitext(os.path.basename(f))[0], title=d.get('title', ''),
                      type=d.get('type', ''), summary=d.get('summary', ''), order=float(d.get('order', 999))))

def line(p, indent=1):
    s = f' — {p["summary"]}' if p['summary'] else ''
    return f'{"  " * indent}- [{p["stem"]}]({p["path"]}){s}'

def group(pred):
    return sorted([p for p in pages if pred(p)], key=lambda p: (p['order'], p['stem']))

src = group(lambda p: p['path'].startswith('sources/'))
con = group(lambda p: p['path'].startswith('concepts/') and p['type'] == 'concept')
met = group(lambda p: p['path'].startswith('concepts/') and p['type'] == 'method')
dat = group(lambda p: p['path'].startswith('concepts/') and p['type'] == 'dataset')
oth = group(lambda p: p['path'].startswith('concepts/') and p['type'] not in ('concept', 'method', 'dataset'))
cmp_ = group(lambda p: p['path'].startswith('comparisons/'))
top = group(lambda p: '/' not in p['path'] and p['stem'] not in ('log',))
ncon = len(con) + len(met) + len(dat) + len(oth)

out = ['---', 'title: Index', 'type: index', f'updated: {datetime.date.today().isoformat()}',
       'generated-by: tools/build_index.py（請勿手改，改各頁 frontmatter 的 summary／order 後重跑）', '---',
       '# SF-DAOD Wiki 目錄', '',
       '> 點檔名即可開啟。建議閱讀順序：[object-detection](concepts/object-detection.md) → [domain-shift](concepts/domain-shift.md) → '
       '[source-free-adaptation](concepts/source-free-adaptation.md) → [sfod-method-families](concepts/sfod-method-families.md) → 各篇論文。', '',
       '```', 'wiki/', '├── index.md', '├── glossary.md', '├── log.md',
       f'├── sources/      （{len(src)} 篇論文）', f'├── concepts/     （{ncon} 頁：概念 {len(con)}、方法 {len(met)}、資料集與指標 {len(dat)}）',
       f'└── comparisons/  （{len(cmp_)} 頁：比較與發想）', '```', '']
out.append('- 📄 根目錄')
for p in top: out.append(line(p))
out.append('  - [log](log.md) — 操作紀錄（ingest／lint／synthesize／build…）')
out.append(f'- 📁 [sources/](sources/) — 論文（{len(src)}）')
out += [line(p) for p in src]
out.append(f'- 📁 [concepts/](concepts/) — 概念、方法、資料集（{ncon}）')
for name, g in (('🧩 概念與問題', con), ('🛠️ 方法', met), ('📊 資料集與指標', dat), ('其他', oth)):
    if not g: continue
    out.append(f'  - {name}（{len(g)}）')
    out += [line(p, 2) for p in g]
out.append(f'- 📁 [comparisons/](comparisons/) — 比較與發想（{len(cmp_)}）')
out += [line(p) for p in cmp_]
open('index.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(f'index.md: {len(pages)} pages')
