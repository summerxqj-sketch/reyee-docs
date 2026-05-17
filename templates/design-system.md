# 锐捷文档中心 · 设计系统模板

## 风格概览

移动端优先的深色渐变表头 + 白色卡片内容区，适用于：
- 功能对比/数据手册
- 任务跟踪/进度表
- 文档目录/导航页

## 配色体系

```
表头渐变:  linear-gradient(135deg, #0d47a1 0%, #1565c0 50%, #1976d2 100%)
背景色:    #f0f2f5
卡片色:    #ffffff
文字色:    #1a1a2e
次要文字:  #546e7a
边框色:    #cfd8dc
阴影:      0 1px 3px rgba(0,0,0,.08)
```

## 状态色板

```
绿色(相同/完成):   #2e7d32
橙色(较弱/进行中): #e65100 / #f57f17
红色(暂无/延迟):   #b71c1c / #d32f2f
蓝色(进行中):      #1976d2 / #1565c0
紫色(规划/产品):   #7b1fa2
灰色(等待):        #757575
```

## 核心组件

### 1. 入口页 (index.html)
- 渐变全屏背景，垂直居中
- 卡片列表，每项带标题、描述、标签
- hover 微动效: translateY(-1px) + 背景透明度变化
- backdrop-filter: blur 毛玻璃效果

### 2. 表头 (header)
```css
.header {
  background: linear-gradient(135deg, #0d47a1 0%, #1565c0 100%);
  padding: 20px 16px 16px;
}
```
- h1: 18px bold
- sub: 12px opacity .7
- 搜索框: 圆角8px, 背景 rgba(255,255,255,.15)
- 统计栏: 内部 grid 4-5列, 背景 rgba(0,0,0,.12)

### 3. 筛选栏 (filters)
- sticky top:0, z-index:50, 白底带阴影
- 横向滚动 overflow-x:auto, 隐藏滚动条
- 筛选按钮: border-radius:16px, padding:5px 12px
- `.filter-btn.on` 状态: 背景变深色文字变白
- 分隔线: 1px solid var(--border)

### 4. 数据卡片/行
- 圆角 8-10px, 白底, 细边框, 底部间距 4-6px
- 左侧 4px 彩色竖条 (优先级/状态色)
- 点击行展开详情: `onclick="toggle(' + cardId + ')"` 
- 详情区: display:none → .show 切换为 block

### 5. 展开详情 (detail)
- border-top 分隔
- padding:10px 12px, 背景 #fafbfc
- 键值对: .dt (60px宽, muted色) + .dd (flex:1)

### 6. 子功能列表 (sub-features/legend)
- 小圆点状态指示器 6-8px
- 紧凑排列, gap:6-8px

## 响应式设计
- viewport: width=device-width, initial-scale=1.0
- max-width: 800px, margin:0 auto 居中
- 所有尺寸用 px/rem, 无固定宽度
- 筛选栏横向滚动适配小屏

## HTML 结构模板

### 入口页
```
渐变背景 > 居中卡片 > 链接列表(hover毛玻璃) > footer
```

### 数据页
```
渐变表头(h1 + sub + 搜索 + 统计) 
→ sticky筛选栏(优先级/状态)
→ 卡片列表(点击展开详情)
→ 图例说明
→ footer
```
