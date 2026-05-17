import json, os

with open(r'C:\Users\HP\Desktop\AI练习\reyee_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    if not d['status']:
        d['status'] = 'none'

json_str = json.dumps(data, ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>锐捷 vs 海康 · 功能对比手册</title>
<style>
:root {
  --bg: #f0f2f5;
  --card: #ffffff;
  --accent: #0d47a1;
  --accent2: #1565c0;
  --green: #1b5e20;
  --orange: #e65100;
  --red: #b71c1c;
  --text: #1a1a2e;
  --muted: #546e7a;
  --border: #cfd8dc;
  --shadow: 0 1px 3px rgba(0,0,0,.08);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
  background: var(--bg); color: var(--text); font-size: 14px;
}
/* === HEADER === */
.header {
  background: linear-gradient(135deg, #0d47a1 0%, #1565c0 100%);
  color: #fff; padding: 20px 16px 16px;
}
.header h1 { font-size: 18px; font-weight: 700; letter-spacing: .3px; }
.header .sub { font-size: 12px; opacity: .7; margin-top: 4px; }
.search-box {
  margin-top: 12px; display: flex; gap: 8px;
}
.search-box input {
  flex: 1; padding: 10px 14px; border: none; border-radius: 8px;
  font-size: 14px; background: rgba(255,255,255,.15); color: #fff;
  outline: none;
}
.search-box input::placeholder { color: rgba(255,255,255,.5); }
.search-box input:focus { background: rgba(255,255,255,.25); }

/* === STATS === */
.stats {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 0;
  background: rgba(0,0,0,.12); margin: 12px -16px -16px; padding: 8px 16px;
}
.stats .s { text-align: center; font-size: 11px; color: rgba(255,255,255,.6); }
.stats .s strong { display: block; font-size: 17px; color: #fff; line-height: 1.4; }

/* === FILTERS === */
.filters {
  background: #fff; padding: 8px 12px; position: sticky; top: 0; z-index: 50;
  box-shadow: var(--shadow); display: flex; gap: 6px; overflow-x: auto;
  scrollbar-width: none;
}
.filters::-webkit-scrollbar { display: none; }
.filter-btn {
  flex-shrink: 0; padding: 5px 12px; border-radius: 16px; font-size: 12px;
  font-weight: 600; cursor: pointer; border: 1.5px solid var(--border);
  color: var(--muted); background: transparent;
}
.filter-btn.on { background: var(--accent); color: #fff; border-color: var(--accent); }
.filter-btn.green.on { background: var(--green); border-color: var(--green); }
.filter-btn.orange.on { background: var(--orange); border-color: var(--orange); }
.filter-btn.red.on { background: var(--red); border-color: var(--red); }
.filter-divider { width: 1px; background: var(--border); flex-shrink: 0; }

/* === CATEGORY NAV === */
.cat-nav {
  background: #fff; display: flex; gap: 0; overflow-x: auto;
  border-bottom: 1px solid var(--border); scrollbar-width: none;
  position: sticky; top: 48px; z-index: 49;
}
.cat-nav::-webkit-scrollbar { display: none; }
.cat-item {
  flex-shrink: 0; padding: 8px 12px; font-size: 12px; font-weight: 600;
  color: var(--muted); cursor: pointer; border-bottom: 2px solid transparent;
}
.cat-item.on { color: var(--accent); border-bottom-color: var(--accent); }

/* === CONTENT === */
.main { padding: 8px; max-width: 800px; margin: 0 auto; }

.scene-title {
  font-size: 13px; font-weight: 700; color: var(--accent);
  padding: 16px 4px 6px; letter-spacing: .5px;
  display: flex; align-items: center; gap: 6px;
}
.scene-title .n {
  background: var(--accent); color: #fff; font-size: 10px;
  padding: 1px 7px; border-radius: 8px;
}

/* === TABLE-LIKE CARD === */
.row {
  background: var(--card); border-radius: 8px; margin-bottom: 4px;
  border: 1px solid var(--border); overflow: hidden;
}
.row-top {
  display: flex; align-items: stretch; cursor: pointer;
  min-height: 44px;
}
.row-main {
  flex: 1; padding: 10px 10px; display: flex; flex-direction: column;
  justify-content: center;
}
.row-main .fn { font-size: 13px; font-weight: 600; line-height: 1.3; }
.row-main .fn-sub { font-size: 11.5px; color: var(--muted); margin-top: 2px; }
.row-badge {
  display: flex; align-items: center; gap: 4px;
  padding: 0 10px; flex-shrink: 0;
}
.badge-dot {
  display: inline-block; width: 8px; height: 8px; border-radius: 50%;
}
.badge-dot.g { background: var(--green); }
.badge-dot.o { background: var(--orange); }
.badge-dot.r { background: var(--red); }

.prio-tag {
  display: inline-block; font-size: 10px; font-weight: 700;
  padding: 1px 6px; border-radius: 3px;
}
.prio-tag.p0 { background: #fff3e0; color: #e65100; }
.prio-tag.p1 { background: #e3f2fd; color: #0d47a1; }
.prio-tag.p2 { background: #f5f5f5; color: #78909c; }

/* === EXPANDED DETAIL === */
.row-detail {
  border-top: 1px solid var(--border); display: none;
  padding: 10px 12px; background: #fafbfc; font-size: 13px;
}
.row-detail.show { display: block; }
.dl { display: flex; gap: 6px; margin-bottom: 5px; }
.dl:last-child { margin-bottom: 0; }
.dt { color: var(--muted); width: 64px; flex-shrink: 0; }
.dd { flex: 1; }

/* sub features */
.subs { margin-top: 8px; border-top: 1px solid #e0e0e0; padding-top: 6px; }
.subs-title { font-size: 11px; font-weight: 700; color: var(--muted); margin-bottom: 4px; }
.sub-row {
  display: flex; align-items: center; gap: 6px; padding: 3px 0;
  font-size: 12.5px;
}
.sub-row .sn { flex: 1; }

/* === EMPTY === */
.empty-state {
  text-align: center; padding: 60px 20px; color: var(--muted); font-size: 14px;
}

/* === BOTTOM HINT === */
.footer {
  text-align: center; padding: 20px; font-size: 11px; color: var(--muted);
}
</style>
</head>
<body>

<div class="header">
  <h1>锐捷 vs 海康 · 功能对比</h1>
  <div class="sub">reyee软件需求分析_在线手册版 · 共 <span id="hdrTotal">0</span> 项</div>
  <div class="search-box">
    <input id="searchInput" type="search" placeholder="搜索功能名称、场景…" autocomplete="off">
  </div>
  <div class="stats">
    <div class="s"><strong id="stTotal">0</strong>全部</div>
    <div class="s"><strong id="stSame">0</strong>相同</div>
    <div class="s"><strong id="stWeak">0</strong>较弱</div>
    <div class="s"><strong id="stNone">0</strong>暂无</div>
  </div>
</div>

<div class="filters" id="filterBar">
  <button class="filter-btn on" data-group="pri" data-val="all">全部</button>
  <button class="filter-btn" data-group="pri" data-val="高 - P0">P0 必做</button>
  <button class="filter-btn" data-group="pri" data-val="高 - P1">P1 重要</button>
  <button class="filter-btn" data-group="pri" data-val="中 - P2">P2 一般</button>
  <div class="filter-divider"></div>
  <button class="filter-btn green on" data-group="status" data-val="all">所有</button>
  <button class="filter-btn green" data-group="status" data-val="相同">相同</button>
  <button class="filter-btn orange" data-group="status" data-val="海康较弱">较弱</button>
  <button class="filter-btn red" data-group="status" data-val="none">暂无</button>
</div>

<div class="cat-nav" id="catNav"></div>

<div class="main" id="mainContent"></div>
<div class="footer">数据来源: reyee软件需求分析_在线手册版-与海康HPP比较.xlsx</div>

<script>
var RAW = ''' + json_str + ''';

var D = RAW;
var CATS = ['全部'].concat([...new Set(D.map(function(r){ return r.category.split(' > ')[0]; }))].sort());

var state = { cat: '全部', pri: 'all', status: 'all', q: '' };

function filter() {
  return D.filter(function(r) {
    if (state.cat !== '全部' && r.category.split(' > ')[0] !== state.cat) return false;
    if (state.pri !== 'all' && r.priority !== state.pri) return false;
    if (state.status !== 'all' && r.status !== state.status) return false;
    if (state.q) {
      var q = state.q.toLowerCase();
      return r.feature.toLowerCase().indexOf(q) !== -1 ||
             r.scene.toLowerCase().indexOf(q) !== -1 ||
             r.hik_feature.toLowerCase().indexOf(q) !== -1;
    }
    return true;
  });
}

function statusInfo(s) {
  if (s === '相同') return { cls: 'g', label: '✓ 相同' };
  if (s === '海康较弱') return { cls: 'o', label: '△ 较弱' };
  return { cls: 'r', label: '✗ 暂无' };
}

function render() {
  var items = filter();
  var total = items.length;
  var nSame = 0, nWeak = 0, nNone = 0;
  items.forEach(function(r) {
    if (r.status === '相同') nSame++;
    else if (r.status === '海康较弱') nWeak++;
    else nNone++;
  });
  document.getElementById('hdrTotal').textContent = D.length;
  document.getElementById('stTotal').textContent = total;
  document.getElementById('stSame').textContent = nSame;
  document.getElementById('stWeak').textContent = nWeak;
  document.getElementById('stNone').textContent = nNone;

  var el = document.getElementById('mainContent');
  if (!total) {
    el.innerHTML = '<div class="empty-state">没有匹配的功能项</div>';
    return;
  }

  // group by scene
  var map = {};
  items.forEach(function(r) {
    var key = r.scene;
    if (!map[key]) map[key] = { scene: key, items: [] };
    map[key].items.push(r);
  });

  var html = '';
  var scenes = Object.keys(map).sort();
  scenes.forEach(function(scene) {
    var list = map[scene].items;
    // group parent/sub
    var parents = [];
    var seen = {};
    list.forEach(function(r) {
      var idx = r.feature.indexOf(' - ');
      if (idx === -1) {
        if (!seen[r.feature]) {
          seen[r.feature] = true;
          parents.push({ item: r, subs: [] });
        }
      }
    });
    list.forEach(function(r) {
      var idx = r.feature.indexOf(' - ');
      if (idx !== -1) {
        var pName = r.feature.substring(0, idx);
        var p = null;
        for (var i = 0; i < parents.length; i++) {
          if (parents[i].item.feature === pName) { p = parents[i]; break; }
        }
        if (p) { p.subs.push(r); }
        else if (!seen[r.feature]) {
          seen[r.feature] = true;
          parents.push({ item: r, subs: [] });
        }
      }
    });

    html += '<div class="scene-title">' + scene + ' <span class="n">' + parents.length + '</span></div>';
    parents.forEach(function(g, idx) {
      var r = g.item;
      var si = statusInfo(r.status);
      var cardId = 'c' + scene.replace(/\\s/g,'') + idx;
      html += '<div class="row">';
      html += '<div class="row-top" onclick="toggle(\'' + cardId + '\')">';
      html += '<div class="row-main">';
      html += '<div class="fn">' + r.feature + '</div>';
      if (r.value) html += '<div class="fn-sub">' + r.value + '</div>';
      html += '</div>';
      html += '<div class="row-badge">';
      html += '<span class="prio-tag ' + (r.priority.includes('P0')?'p0':r.priority.includes('P1')?'p1':'p2') + '">' + (r.priority.includes('P0')?'P0':r.priority.includes('P1')?'P1':'P2') + '</span>';
      html += '<span class="badge-dot ' + si.cls + '"></span>';
      html += '</div></div>';
      html += '<div class="row-detail" id="' + cardId + '">';
      html += '<div class="dl"><div class="dt">优先级</div><div class="dd">' + r.priority + '</div></div>';
      if (r.value) html += '<div class="dl"><div class="dt">价值</div><div class="dd">' + r.value + '</div></div>';
      html += '<div class="dl"><div class="dt">用户</div><div class="dd">' + r.user + '</div></div>';
      if (r.hik_feature) {
        html += '<div class="dl"><div class="dt">海康对应</div><div class="dd">' + r.hik_feature + ' <span style="color:' + (r.status==='相同'?'var(--green)':r.status==='海康较弱'?'var(--orange)':'var(--red)') + ';font-weight:600">' + si.label + '</span></div></div>';
      }
      if (g.subs.length > 0) {
        html += '<div class="subs"><div class="subs-title">子功能 ' + g.subs.length + ' 项</div>';
        g.subs.forEach(function(s) {
          var ssi = statusInfo(s.status);
          var subName = s.feature.substring(s.feature.indexOf(' - ') + 3);
          html += '<div class="sub-row"><span class="badge-dot ' + ssi.cls + '"></span><span class="sn">' + subName + '</span><span style="font-size:11px;color:var(--muted)">' + ssi.label + '</span></div>';
        });
        html += '</div>';
      }
      html += '</div></div>';
    });
  });

  el.innerHTML = html;
}

function toggle(id) {
  var el = document.getElementById(id);
  if (el) el.classList.toggle('show');
}

// === CATEGORY NAV ===
function buildCatNav() {
  var el = document.getElementById('catNav');
  el.innerHTML = CATS.map(function(c) {
    return '<div class="cat-item' + (c === state.cat ? ' on' : '') + '" data-cat="' + c + '">' + c + '</div>';
  }).join('');
  el.querySelectorAll('.cat-item').forEach(function(t) {
    t.addEventListener('click', function() {
      state.cat = this.getAttribute('data-cat');
      el.querySelectorAll('.cat-item').forEach(function(x){ x.classList.remove('on'); });
      this.classList.add('on');
      render();
    });
  });
}

// === FILTERS ===
document.getElementById('filterBar').addEventListener('click', function(e) {
  var btn = e.target.closest('[data-group]');
  if (!btn) return;
  var group = btn.getAttribute('data-group');
  var val = btn.getAttribute('data-val');
  if (group === 'pri') {
    state.pri = val;
    document.querySelectorAll('[data-group="pri"]').forEach(function(b){ b.classList.remove('on'); });
  } else {
    state.status = val;
    document.querySelectorAll('[data-group="status"]').forEach(function(b){ b.classList.remove('on'); });
  }
  btn.classList.add('on');
  render();
});

// === SEARCH ===
var st;
document.getElementById('searchInput').addEventListener('input', function(e) {
  clearTimeout(st);
  st = setTimeout(function() {
    state.q = e.target.value.trim();
    render();
  }, 200);
});

buildCatNav();
render();
</script>
</body>
</html>'''

output = r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\index.html'
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)
size = os.path.getsize(output)
print(f'Done: {output} ({size/1024:.1f} KB)')
print(f'Data records: {len(data)}')
