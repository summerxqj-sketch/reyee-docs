import json, os

data = [
  {"pri":"🔴紧急","seq":1,"region":"缅甸/伊拉克/阿联酋","title":"首批订单落地跟进","action":"确认下单进度、物流安排、付款状态","status":"进行中","deadline":"2026-04-30","owner":"","note":"缅甸1K+/伊拉克1K+/阿联酋2K+","done":"☐ 未完成"},
  {"pri":"🔴紧急","seq":2,"region":"印尼","title":"MB专代库存out及测试跟井","action":"做好现有库存out、测试跟井、软件开发进度交叉验证","status":"进行中","deadline":"2026-05-15","owner":"","note":"MB专代(router/AP/网桥等准备都给他)","done":"☐ 未完成"},
  {"pri":"🔴紧急","seq":3,"region":"马来西亚","title":"Synctnology+UB ND首批订单","action":"Synctnology 4月已签合同，UB ND谈订单中→跟进首批订单","status":"进行中","deadline":"2026-05-15","owner":"","note":"UB ND签约中","done":"☐ 未完成"},
  {"pri":"🔴紧急","seq":4,"region":"香港","title":"UTG首批订单跟进","action":"UTG为TP ND也为海康国代，有意愿→跟进首批订单","status":"进行中","deadline":"2026-05-15","owner":"","note":"香港有2家，人员精力问题","done":"☐ 未完成"},
  {"pri":"🟡中期","seq":5,"region":"R国","title":"Elcc/Xcom/Merion测试跟进","action":"Elcc有想法Xcom可谈；Merion网通专代→跟进测试进度","status":"测试中","deadline":"2026-05-31","owner":"","note":"ND能力弱(TG)","done":"☐ 未完成"},
  {"pri":"🟡中期","seq":6,"region":"巴基斯坦","title":"UltraTech(GS ND)测试跟进","action":"UltraTech已签约GS ND→跟进测试进度","status":"测试中","deadline":"2026-05-31","owner":"","note":"ND弱(Intextco意愿问题/ESCO精力)","done":"☐ 未完成"},
  {"pri":"🟡中期","seq":7,"region":"沙特","title":"SF以现有ND展开(SF)","action":"以现有ND为主展开(SP)→跟进测试进度","status":"测试中","deadline":"2026-05-31","owner":"","note":"Open to all","done":"☐ 未完成"},
  {"pri":"🟡中期","seq":8,"region":"斯里兰卡","title":"ITG专代测试跟进","action":"ITG专代→跟进测试进度","status":"测试中","deadline":"2026-05-31","owner":"","note":"ND中(但是会投入做网通)","done":"☐ 未完成"},
  {"pri":"🟡中期","seq":9,"region":"乌兹别克","title":"网通专代UB客户洽谈","action":"1家网通专代，一些UB客户在谈","status":"洽谈中","deadline":"2026-06-15","owner":"","note":"市场相对小","done":"☐ 未完成"},
  {"pri":"🟢重点","seq":10,"region":"哈萨克斯坦","title":"重点市场调研与进入","action":"6-8M市场容量，中亚最大市场！尽快完成调研进入开拓","status":"调研中","deadline":"2026-06-30","owner":"","note":"⭐中亚最大市场，重点聚焦！","done":"☐ 未完成"},
  {"pri":"🟢重点","seq":11,"region":"泰国","title":"催促反馈+sell-out监控","action":"有1家有意愿但反馈慢，注意其sell-out进度","status":"等待反馈","deadline":"2026-06-15","owner":"","note":"分公司意愿'中'","done":"☐ 未完成"},
  {"pri":"📋持续","seq":12,"region":"其余32国","title":"先锋客户反推ND导入","action":"从PM/销售经理/中心反馈相对积极，以先锋客户测试反推ND导入","status":"长期跟进","deadline":"持续","owner":"","note":"剩余32国配合度较好","done":"☐ 进行中"},
  {"pri":"🎯产品","seq":13,"region":"产品团队","title":"高概率场景产品针对性开发","action":"根据各国家客户需求反馈，推动产品针对性开发","status":"规划中","deadline":"持续","owner":"","note":"端到端直接对接管理跟进","done":"☐ 规划中"},
  {"pri":"🎯产品","seq":14,"region":"产品团队","title":"软件开发进度交叉验证","action":"印尼MB等客户的软件开发需求跟进验证","status":"进行中","deadline":"2026-05-31","owner":"","note":"配合MB专代需求","done":"☐ 未完成"}
]

# Priority colors mapping
pri_colors = {
  "🔴紧急": {"bg":"#ffebee","dot":"#d32f2f","label":"紧急","order":0},
  "🟡中期": {"bg":"#fff8e1","dot":"#f57f17","label":"中期","order":1},
  "🟢重点": {"bg":"#e8f5e9","dot":"#2e7d32","label":"重点","order":2},
  "📋持续": {"bg":"#e3f2fd","dot":"#1565c0","label":"持续","order":3},
  "🎯产品": {"bg":"#f3e5f5","dot":"#7b1fa2","label":"产品","order":4}
}

# Status colors
status_colors = {
  "进行中": {"dot":"#1976d2","bg":"#e3f2fd"},
  "测试中": {"dot":"#f57f17","bg":"#fff8e1"},
  "洽谈中": {"dot":"#f57f17","bg":"#fff8e1"},
  "调研中": {"dot":"#7b1fa2","bg":"#f3e5f5"},
  "等待反馈": {"dot":"#757575","bg":"#f5f5f5"},
  "长期跟进": {"dot":"#1565c0","bg":"#e3f2fd"},
  "规划中": {"dot":"#7b1fa2","bg":"#f3e5f5"}
}

json_str = json.dumps(data, ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>网通专代开拓 · 任务跟踪表</title>
<style>
:root {
  --bg: #f0f2f5; --card: #fff; --text: #1a1a2e; --muted: #546e7a;
  --border: #cfd8dc; --shadow: 0 1px 3px rgba(0,0,0,.08);
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
  font-family: -apple-system, 'PingFang SC', 'Microsoft YaHei', sans-serif;
  background: var(--bg); color: var(--text); font-size: 14px;
}
.header {
  background: linear-gradient(135deg, #1a237e 0%, #283593 100%);
  color: #fff; padding: 20px 16px 16px;
}
.header h1 { font-size: 18px; font-weight: 700; }
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
.stats {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 0;
  background: rgba(0,0,0,.12); margin: 12px -16px -16px; padding: 8px 16px;
}
.stats .s { text-align: center; font-size: 11px; color: rgba(255,255,255,.6); }
.stats .s strong { display: block; font-size: 17px; color: #fff; line-height: 1.4; }

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
.filter-btn.on { background: var(--text); color: #fff; border-color: var(--text); }
.filter-divider { width: 1px; background: var(--border); flex-shrink: 0; }

.main { padding: 8px; max-width: 800px; margin: 0 auto; }

.card {
  background: var(--card); border-radius: 10px; margin-bottom: 6px;
  border: 1px solid var(--border); overflow: hidden;
}
.card-top {
  display: flex; align-items: stretch; cursor: pointer;
  min-height: 48px;
}
.card-left {
  width: 4px; flex-shrink: 0; border-radius: 10px 0 0 10px;
}
.card-body {
  flex: 1; padding: 10px 10px; display: flex; flex-direction: column;
  justify-content: center;
}
.card-body .t {
  font-size: 14px; font-weight: 600; line-height: 1.3;
}
.card-body .m {
  font-size: 12px; color: var(--muted); margin-top: 3px;
  display: flex; gap: 8px; flex-wrap: wrap;
}
.card-body .m span { display: inline-flex; align-items: center; gap: 3px; }
.card-right {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  padding: 0 12px; flex-shrink: 0; gap: 4px;
}
.card-right .status-tag {
  font-size: 11px; font-weight: 600; padding: 2px 8px;
  border-radius: 10px; white-space: nowrap;
}
.card-right .done-tag {
  font-size: 11px; color: var(--muted);
}

.detail {
  border-top: 1px solid var(--border); display: none;
  padding: 10px 12px; background: #fafbfc; font-size: 13px;
}
.detail.show { display: block; }
.dl { display: flex; gap: 6px; margin-bottom: 5px; }
.dl:last-child { margin-bottom: 0; }
.dt { color: var(--muted); width: 60px; flex-shrink: 0; }
.dd { flex: 1; }

.empty-state { text-align: center; padding: 60px 20px; color: var(--muted); }

.legend {
  margin-top: 12px; padding: 10px 12px; background: var(--card);
  border-radius: 8px; border: 1px solid var(--border);
}
.legend-title { font-size: 12px; font-weight: 700; color: var(--muted); margin-bottom: 6px; }
.legend-items { display: flex; gap: 12px; flex-wrap: wrap; }
.legend-item { display: flex; align-items: center; gap: 4px; font-size: 11px; color: var(--muted); }
.legend-dot { width: 8px; height: 8px; border-radius: 50%; }

.footer { text-align: center; padding: 16px; font-size: 11px; color: var(--muted); }
</style>
</head>
<body>

<div class="header">
  <h1>网通专代开拓 · 任务跟踪</h1>
  <div class="sub">更新日期：2026-04-26 · 共 <span id="hdrTotal">0</span> 项任务</div>
  <div class="search-box">
    <input id="searchInput" type="search" placeholder="搜索国家/地区、事项…" autocomplete="off">
  </div>
  <div class="stats">
    <div class="s"><strong id="stTotal">0</strong>全部</div>
    <div class="s"><strong id="stUrgent">0</strong>紧急</div>
    <div class="s"><strong id="stMid">0</strong>中期</div>
    <div class="s"><strong id="stKey">0</strong>重点</div>
    <div class="s"><strong id="stOther">0</strong>其他</div>
  </div>
</div>

<div class="filters" id="filterBar">
  <button class="filter-btn on" data-val="all">全部</button>
  <button class="filter-btn" data-val="🔴紧急">🔴 紧急</button>
  <button class="filter-btn" data-val="🟡中期">🟡 中期</button>
  <button class="filter-btn" data-val="🟢重点">🟢 重点</button>
  <button class="filter-btn" data-val="📋持续">📋 持续</button>
  <button class="filter-btn" data-val="🎯产品">🎯 产品</button>
  <div class="filter-divider"></div>
  <button class="filter-btn on" data-status="all">所有状态</button>
  <button class="filter-btn" data-status="进行中">进行中</button>
  <button class="filter-btn" data-status="测试中">测试中</button>
  <button class="filter-btn" data-status="洽谈中/调研中">洽谈/调研</button>
</div>

<div class="main" id="mainContent"></div>

<div class="footer">数据来源: 网通专代开拓-任务跟踪表.xlsx</div>

<script>
var RAW = ''' + json_str + ''';

var D = RAW;
var PRI_LABELS = { "🔴紧急":"紧急","🟡中期":"中期","🟢重点":"重点","📋持续":"持续","🎯产品":"产品" };
var PRI_COLORS = { "🔴紧急":"#d32f2f","🟡中期":"#f57f17","🟢重点":"#2e7d32","📋持续":"#1565c0","🎯产品":"#7b1fa2" };
var STATUS_COLORS = {
  "进行中":"#1976d2","测试中":"#f57f17","洽谈中":"#f57f17","调研中":"#7b1fa2",
  "等待反馈":"#757575","长期跟进":"#1565c0","规划中":"#7b1fa2"
};

function statusBg(s) { return STATUS_COLORS[s] || '#757575'; }

var state = { pri: 'all', st: 'all', q: '' };

function filter() {
  return D.filter(function(r) {
    if (state.pri !== 'all' && r.pri !== state.pri) return false;
    if (state.st !== 'all') {
      if (state.st === '洽谈中/调研中') {
        if (r.status !== '洽谈中' && r.status !== '调研中') return false;
      } else if (r.status !== state.st) return false;
    }
    if (state.q) {
      var q = state.q.toLowerCase();
      return r.region.toLowerCase().indexOf(q) !== -1 ||
             r.title.toLowerCase().indexOf(q) !== -1 ||
             r.action.toLowerCase().indexOf(q) !== -1 ||
             r.note.toLowerCase().indexOf(q) !== -1;
    }
    return true;
  });
}

function render() {
  var items = filter();
  var total = items.length;
  var urgent = 0, mid = 0, key = 0, other = 0;
  items.forEach(function(r) {
    if (r.pri === "🔴紧急") urgent++;
    else if (r.pri === "🟡中期") mid++;
    else if (r.pri === "🟢重点") key++;
    else other++;
  });
  document.getElementById('hdrTotal').textContent = D.length;
  document.getElementById('stTotal').textContent = total;
  document.getElementById('stUrgent').textContent = urgent;
  document.getElementById('stMid').textContent = mid;
  document.getElementById('stKey').textContent = key;
  document.getElementById('stOther').textContent = other;

  var el = document.getElementById('mainContent');
  if (!total) {
    el.innerHTML = '<div class="empty-state">没有匹配的任务</div>';
    return;
  }

  var html = '';
  items.forEach(function(r, idx) {
    var cardId = 'task' + idx;
    var color = PRI_COLORS[r.pri] || '#757575';
    var sColor = statusBg(r.status);
    html += '<div class="card">';
    html += '<div class="card-top" onclick="toggle(\'' + cardId + '\')">';
    html += '<div class="card-left" style="background:' + color + '"></div>';
    html += '<div class="card-body">';
    html += '<div class="t">' + r.pri + ' ' + r.title + '</div>';
    html += '<div class="m">';
    html += '<span>🌍 ' + r.region + '</span>';
    html += '<span>📅 ' + r.deadline + '</span>';
    html += '<span>#' + r.seq + '</span>';
    html += '</div></div>';
    html += '<div class="card-right">';
    html += '<span class="status-tag" style="background:' + sColor + '22;color:' + sColor + '">' + r.status + '</span>';
    html += '<span class="done-tag">' + r.done + '</span>';
    html += '</div></div>';
    html += '<div class="detail" id="' + cardId + '">';
    html += '<div class="dl"><div class="dt">行动项</div><div class="dd">' + r.action + '</div></div>';
    if (r.note) html += '<div class="dl"><div class="dt">备注</div><div class="dd">' + r.note + '</div></div>';
    html += '<div class="dl"><div class="dt">负责人</div><div class="dd">' + (r.owner || '待分配') + '</div></div>';
    html += '<div class="dl"><div class="dt">优先级</div><div class="dd">' + r.pri + ' ' + (PRI_LABELS[r.pri]||'') + '</div></div>';
    html += '</div></div>';
  });

  // Legend
  html += '<div class="legend">';
  html += '<div class="legend-title">图例说明</div>';
  html += '<div class="legend-items">';
  html += '<div class="legend-item"><div class="legend-dot" style="background:#d32f2f"></div>🔴紧急 · 4月底-5月初</div>';
  html += '<div class="legend-item"><div class="legend-dot" style="background:#f57f17"></div>🟡中期 · 5月-6月</div>';
  html += '<div class="legend-item"><div class="legend-dot" style="background:#2e7d32"></div>🟢重点 · 聚焦/调研</div>';
  html += '<div class="legend-item"><div class="legend-dot" style="background:#1565c0"></div>📋持续 · 长期跟进</div>';
  html += '<div class="legend-item"><div class="legend-dot" style="background:#7b1fa2"></div>🎯产品 · 产品侧配合</div>';
  html += '</div></div>';

  el.innerHTML = html;
}

function toggle(id) {
  var el = document.getElementById(id);
  if (el) el.classList.toggle('show');
}

document.getElementById('filterBar').addEventListener('click', function(e) {
  var btn = e.target.closest('[data-val]');
  if (btn) {
    state.pri = btn.getAttribute('data-val');
    document.querySelectorAll('[data-val]').forEach(function(b){ b.classList.remove('on'); });
    btn.classList.add('on');
    render();
    return;
  }
  var btn2 = e.target.closest('[data-status]');
  if (btn2) {
    state.st = btn2.getAttribute('data-status');
    document.querySelectorAll('[data-status]').forEach(function(b){ b.classList.remove('on'); });
    btn2.classList.add('on');
    render();
  }
});

var st;
document.getElementById('searchInput').addEventListener('input', function(e) {
  clearTimeout(st);
  st = setTimeout(function() {
    state.q = e.target.value.trim();
    render();
  }, 200);
});

render();
</script>
</body>
</html>'''

output = r'C:\Users\HP\AppData\Local\Temp\reyee-deploy\tasks.html'
with open(output, 'w', encoding='utf-8') as f:
    f.write(html)
size = os.path.getsize(output)
print(f'Done: {output} ({size/1024:.1f} KB)')
