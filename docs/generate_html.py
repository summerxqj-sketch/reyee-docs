import json, os, sys

with open(r'C:\Users\HP\Desktop\AI练习\reyee_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    if not d['status']:
        d['status'] = 'none'

json_str = json.dumps(data, ensure_ascii=False)

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>锐捷云 vs 海康 · 功能对比手册</title>
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{--blue:#1a2f5a;--blue-light:#1565c0;--red:#e53935;--green:#2e7d32;--amber:#e65100;--gray:#546e7a;--bg:#f5f7fa;--card:#fff;--border:#e0e4ef;--text:#1a1a2e;--muted:#6b7280}}
body{{font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;background:var(--bg);color:var(--text);font-size:14px;min-height:100vh}}
.topbar{{background:var(--blue);color:#fff;padding:14px 16px 0;position:sticky;top:0;z-index:100;box-shadow:0 2px 8px rgba(0,0,0,.25)}}
.topbar-title{{display:flex;align-items:center;gap:10px;margin-bottom:12px}}
.topbar-title h1{{font-size:15px;font-weight:700;letter-spacing:.5px}}
.topbar-title .badge{{background:var(--red);font-size:10px;padding:2px 8px;border-radius:10px;font-weight:600;letter-spacing:1px}}
.search-row{{display:flex;gap:8px;margin-bottom:12px}}
.search-input{{flex:1;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);color:#fff;padding:8px 12px;border-radius:6px;font-size:14px;outline:none}}
.search-input::placeholder{{color:rgba(255,255,255,.5)}}
.search-input:focus{{background:rgba(255,255,255,.18);border-color:rgba(255,255,255,.4)}}
.filter-bar{{display:flex;gap:6px;overflow-x:auto;padding-bottom:12px;scrollbar-width:none}}
.filter-bar::-webkit-scrollbar{{display:none}}
.pill{{flex-shrink:0;padding:5px 12px;border-radius:20px;font-size:12px;font-weight:600;cursor:pointer;border:1.5px solid rgba(255,255,255,.25);color:rgba(255,255,255,.7);background:transparent;transition:.15s}}
.pill.active{{background:#fff;color:var(--blue);border-color:#fff}}
.pill-status{{border-color:rgba(255,255,255,.2)}}
.stats-bar{{background:rgba(0,0,0,.15);display:flex;gap:0;border-top:1px solid rgba(255,255,255,.1)}}
.stat{{flex:1;text-align:center;padding:8px 4px;font-size:11px;color:rgba(255,255,255,.6)}}
.stat strong{{display:block;font-size:16px;font-weight:700;color:#fff;line-height:1.2}}
.cat-tabs{{display:flex;gap:0;overflow-x:auto;background:#fff;border-bottom:2px solid var(--border);scrollbar-width:none;position:sticky;top:130px;z-index:90}}
.cat-tabs::-webkit-scrollbar{{display:none}}
.cat-tab{{flex-shrink:0;padding:10px 14px;font-size:12px;font-weight:600;color:var(--muted);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;white-space:nowrap;transition:.15s}}
.cat-tab.active{{color:var(--blue-light);border-bottom-color:var(--blue-light)}}
.cat-tab:hover{{color:var(--blue)}}
.content{{padding:12px 12px 80px}}
.section-header{{font-size:12px;font-weight:700;color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;padding:16px 4px 8px;display:flex;align-items:center;gap:8px}}
.section-header .count{{background:var(--blue);color:#fff;font-size:10px;padding:1px 7px;border-radius:10px;letter-spacing:0}}
.feature-card{{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:8px;overflow:hidden;transition:.15s}}
.feature-card:active{{transform:scale(.99)}}
.card-header{{display:flex;align-items:center;gap:10px;padding:12px 14px;cursor:pointer}}
.card-chevron{{width:20px;height:20px;flex-shrink:0;color:var(--muted);transition:transform .2s}}
.card-chevron.open{{transform:rotate(90deg)}}
.card-feature-name{{flex:1;font-size:14px;font-weight:600;color:var(--text);line-height:1.35}}
.card-badges{{display:flex;gap:5px;flex-shrink:0}}
.badge-p{{font-size:10px;font-weight:700;padding:2px 7px;border-radius:4px}}
.badge-p0{{background:#fff3e0;color:#e65100}}
.badge-p1{{background:#e8edf8;color:#1a2f5a}}
.badge-p2{{background:#f3f4f6;color:#6b7280}}
.badge-same{{background:#e8f5e9;color:#2e7d32;font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px}}
.badge-weak{{background:#fff3e0;color:#e65100;font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px}}
.badge-none{{background:#fef2f2;color:#b91c1c;font-size:10px;font-weight:700;padding:2px 8px;border-radius:4px}}
.card-body{{border-top:1px solid var(--border);padding:12px 14px;display:none;background:#fafbfd}}
.card-body.open{{display:block}}
.detail-row{{display:flex;gap:8px;margin-bottom:8px;font-size:13px}}
.detail-label{{color:var(--muted);flex-shrink:0;width:72px}}
.detail-value{{color:var(--text);font-weight:500;flex:1}}
.detail-value.hik-same{{color:var(--green)}}
.detail-value.hik-weak{{color:var(--amber)}}
.detail-value.hik-none{{color:var(--red)}}
.sub-features{{margin-top:8px;border-top:1px solid var(--border);padding-top:8px}}
.sub-feature-title{{font-size:11px;font-weight:700;color:var(--muted);letter-spacing:1px;text-transform:uppercase;margin-bottom:6px}}
.sub-item{{display:flex;align-items:center;gap:8px;padding:5px 0;border-bottom:1px solid #f0f1f5;font-size:12.5px}}
.sub-item:last-child{{border-bottom:none}}
.sub-item-name{{flex:1;color:var(--text)}}
.sub-dot{{width:6px;height:6px;border-radius:50%;flex-shrink:0}}
.dot-same{{background:var(--green)}}
.dot-weak{{background:var(--amber)}}
.dot-none{{background:var(--red)}}
.empty{{text-align:center;padding:60px 20px;color:var(--muted)}}
.bottom-nav{{position:fixed;bottom:0;left:0;right:0;background:#fff;border-top:1px solid var(--border);display:flex;padding:8px 0;z-index:100;box-shadow:0 -2px 8px rgba(0,0,0,.08)}}
.nav-item{{flex:1;text-align:center;padding:4px;cursor:pointer;color:var(--muted);font-size:10px;font-weight:600}}
.nav-item.active{{color:var(--blue-light)}}
.status-legend{{display:flex;gap:12px;padding:8px 12px;background:#fff;border-bottom:1px solid var(--border);font-size:11px;color:var(--muted)}}
.legend-item{{display:flex;align-items:center;gap:4px}}
.legend-dot{{width:8px;height:8px;border-radius:50%}}
</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-title">
    <h1>锐捷云 vs 海康 · 功能对比</h1>
    <span class="badge">数据来源: reyee软件需求分析_在线手册版</span>
  </div>
  <div class="search-row">
    <input class="search-input" id="searchInput" type="text" placeholder="搜索功能关键词…" autocomplete="off">
  </div>
  <div class="filter-bar" id="priorityFilter">
    <button class="pill active" data-priority="all">全部</button>
    <button class="pill" data-priority="高 - P0">P0 必做</button>
    <button class="pill" data-priority="高 - P1">P1 重要</button>
    <button class="pill" data-priority="中 - P2">P2 一般</button>
  </div>
  <div class="filter-bar" id="statusFilter">
    <button class="pill pill-status active" data-status="all">所有状态</button>
    <button class="pill pill-status" data-status="相同">✓ 功能相同</button>
    <button class="pill pill-status" data-status="海康较弱">△ 海康较弱</button>
    <button class="pill pill-status" data-status="none">✗ 暂无对应</button>
  </div>
  <div class="stats-bar" id="statsBar">
    <div class="stat"><strong id="statTotal">0</strong>功能项</div>
    <div class="stat"><strong id="statSame">0</strong>相同</div>
    <div class="stat"><strong id="statWeak">0</strong>较弱</div>
    <div class="stat"><strong id="statNone">0</strong>暂无</div>
  </div>
</div>

<div class="cat-tabs" id="catTabs"></div>

<div class="status-legend">
  <div class="legend-item"><div class="legend-dot" style="background:#2e7d32"></div>功能相同</div>
  <div class="legend-item"><div class="legend-dot" style="background:#e65100"></div>海康较弱</div>
  <div class="legend-item"><div class="legend-dot" style="background:#b91c1c"></div>暂无对应</div>
</div>

<div class="content" id="content"></div>

<script>
const RAW = {json_str};

const data = RAW;

const CATS = ['全部', ...new Set(data.map(r => r.category.split(' > ')[0]))];

let activeCat = '全部';
let activePriority = 'all';
let activeStatus = 'all';
let searchQ = '';

function statusBadge(s){{
  if(s==='相同') return '<span class="badge-same">✓ 相同</span>';
  if(s==='海康较弱') return '<span class="badge-weak">△ 较弱</span>';
  return '<span class="badge-none">✗ 暂无</span>';
}}
function priorityBadge(p){{
  if(p.includes('P0')) return '<span class="badge-p badge-p0">P0</span>';
  if(p.includes('P1')) return '<span class="badge-p badge-p1">P1</span>';
  return '<span class="badge-p badge-p2">P2</span>';
}}

function filtered(){{
  return data.filter(r => {{
    const topCat = r.category.split(' > ')[0];
    if(activeCat !== '全部' && topCat !== activeCat) return false;
    if(activePriority !== 'all' && r.priority !== activePriority) return false;
    if(activeStatus !== 'all' && r.status !== activeStatus) return false;
    if(searchQ){{
      const q = searchQ.toLowerCase();
      return r.feature.toLowerCase().includes(q) || r.scene.toLowerCase().includes(q) || r.hik_feature.toLowerCase().includes(q) || r.value.toLowerCase().includes(q);
    }}
    return true;
  }});
}}

function group(items){{
  const parents = [];
  const seen = new Set();
  items.forEach(r => {{
    const isSub = r.feature.includes(' - ');
    if(!isSub){{
      if(!seen.has(r.feature)){{
        seen.add(r.feature);
        parents.push({{...r, subs: []}});
      }}
    }}
  }});
  items.forEach(r => {{
    if(r.feature.includes(' - ')){{
      const parentName = r.feature.split(' - ')[0];
      const parent = parents.find(p => p.feature === parentName);
      if(parent) parent.subs.push(r);
      else {{
        if(!seen.has(r.feature)){{
          seen.add(r.feature);
          parents.push({{...r, subs: []}});
        }}
      }}
    }}
  }});
  return parents;
}}

function render(){{
  const items = filtered();
  const total = items.length;
  const same = items.filter(r=>r.status==='相同').length;
  const weak = items.filter(r=>r.status==='海康较弱').length;
  const none = items.filter(r=>r.status==='none').length;

  document.getElementById('statTotal').textContent = total;
  document.getElementById('statSame').textContent = same;
  document.getElementById('statWeak').textContent = weak;
  document.getElementById('statNone').textContent = none;

  const content = document.getElementById('content');
  if(!total){{
    content.innerHTML = '<div class="empty">没有找到匹配的功能项</div>';
    return;
  }}

  const byScene = {{}};
  items.forEach(r => {{
    const key = r.category.split(' > ')[0] + '|' + r.scene;
    if(!byScene[key]) byScene[key] = {{cat: r.category.split(' > ')[0], scene: r.scene, items: []}};
    byScene[key].items.push(r);
  }});

  let html = '';
  const sections = Object.values(byScene);
  sections.forEach(sec => {{
    const parents = group(sec.items);
    if(!parents.length) return;
    html += '<div class="section-header">' + sec.scene + ' <span class="count">' + parents.length + '</span></div>';
    parents.forEach((r, idx) => {{
      const cardId = 'card_' + sec.scene + '_' + idx;
      const cleanId = cardId.replace(/[^a-zA-Z0-9_]/g, '_');
      const hasSubs = r.subs && r.subs.length > 0;
      html += '<div class="feature-card"><div class="card-header" onclick="toggleCard(\\'' + cleanId + '\\')">';
      html += '<svg class="card-chevron" id="chev_' + cleanId + '" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="9 18 15 12 9 6"/></svg>';
      html += '<div class="card-feature-name">' + r.feature + '</div>';
      html += '<div class="card-badges">' + priorityBadge(r.priority) + statusBadge(r.status) + '</div></div>';
      html += '<div class="card-body" id="' + cleanId + '">';
      if(r.value) html += '<div class="detail-row"><span class="detail-label">功能价值</span><span class="detail-value">' + r.value + '</span></div>';
      html += '<div class="detail-row"><span class="detail-label">目标用户</span><span class="detail-value">' + r.user + '</span></div>';
      if(r.hik_feature) {{
        const cls = r.status==='相同'?'hik-same':r.status==='海康较弱'?'hik-weak':'hik-none';
        html += '<div class="detail-row"><span class="detail-label">海康对应</span><span class="detail-value ' + cls + '">' + r.hik_feature + '</span></div>';
      }}
      if(hasSubs){{
        html += '<div class="sub-features"><div class="sub-feature-title">子功能 · ' + r.subs.length + '项</div>';
        r.subs.forEach(s => {{
          const dotClass = s.status==='相同'?'dot-same':s.status==='海康较弱'?'dot-weak':'dot-none';
          const subName = s.feature.split(' - ').slice(1).join(' - ');
          html += '<div class="sub-item"><div class="sub-dot ' + dotClass + '"></div><div class="sub-item-name">' + subName + '</div>' + statusBadge(s.status) + '</div>';
        }});
        html += '</div>';
      }}
      html += '</div></div>';
    }});
  }});

  content.innerHTML = html;
}}

function toggleCard(id){{
  const body = document.getElementById(id);
  const chev = document.getElementById('chev_'+id);
  body.classList.toggle('open');
  chev.classList.toggle('open');
}}

function buildCatTabs(){{
  const tabs = document.getElementById('catTabs');
  tabs.innerHTML = CATS.map(c => '<div class="cat-tab' + (c===activeCat?' active':'') + '" data-cat="' + c + '">' + c + '</div>').join('');
  tabs.querySelectorAll('.cat-tab').forEach(t => t.addEventListener('click', function() {{
    activeCat = this.dataset.cat;
    tabs.querySelectorAll('.cat-tab').forEach(function(x){{x.classList.remove('active');}});
    this.classList.add('active');
    render();
  }}));
}}

document.getElementById('priorityFilter').addEventListener('click', function(e) {{
  const pill = e.target.closest('[data-priority]');
  if(!pill) return;
  activePriority = pill.dataset.priority;
  document.querySelectorAll('[data-priority]').forEach(function(p){{p.classList.remove('active');}});
  pill.classList.add('active');
  render();
}});

document.getElementById('statusFilter').addEventListener('click', function(e) {{
  const pill = e.target.closest('[data-status]');
  if(!pill) return;
  activeStatus = pill.dataset.status;
  document.querySelectorAll('[data-status]').forEach(function(p){{p.classList.remove('active');}});
  pill.classList.add('active');
  render();
}});

let searchTimer;
document.getElementById('searchInput').addEventListener('input', function(e) {{
  clearTimeout(searchTimer);
  searchTimer = setTimeout(function() {{
    searchQ = e.target.value.trim();
    render();
  }}, 200);
}});

buildCatTabs();
render();
</script>
</body>
</html>'''

output_path = r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

size = os.path.getsize(output_path)
print(f'Generated: {output_path}')
print(f'Size: {size/1024:.1f} KB')
print(f'Total features in data: {len(data)}')
