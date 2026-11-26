# Candidates — Glossary Extractor

> 识别结果: 关键概念词典（源文档的核心行话）
> 提取自: 《400 个爆款短剧剧本爽点》内容总结

```yaml
- id: g01
  term: 爽点
  type: term
  source_chapter: 全篇
  author_definition: |
    "快速给读者情绪满足"的情节单位。
  key_distinction: |
    ≠ 仅指打架打脸 — 物质收获、地位提升、他人崇拜、感情收获都是爽点。
    = 任何"制造反差、信息差、反转"并让读者情绪满足的桥段。
  why_it_matters: |
    本技能包的校验单位。校验剧本时按此宽口径盘点，
    避免只统计战斗/打脸场景。
  tags: [term, core-concept]

- id: g02
  term: 扮猪吃虎
  type: term
  source_chapter: 一、身份反差・隐藏大佬
  author_definition: |
    "主角实力/地位极高，但对外表现为小人物，旁人轻视、嘲讽，后续揭开反差制造爽感"。
  key_distinction: |
    ≠ 单纯低调 — 必须包含'被轻视'与'揭晓'两个阶段。
    = 身份反差类的总称，涵盖多重身份、幕后大佬、扫地僧等变体。
  why_it_matters: |
    本技能包第一大类的识别关键词，也是用户提问的高频词。
  tags: [term, core-concept]

- id: g03
  term: 迪化流
  type: term
  source_chapter: 一、身份反差（衍生桥段）
  author_definition: |
    "配角根据主角普通言行，疯狂脑补高大上动机"。
  key_distinction: |
    ≠ 主角主动装 X — 脑补是配角单方面的，主角可能完全无辜。
    = 解读权错位，喜剧 + 敬畏双效果。
  why_it_matters: |
    易与'虚张声势'混淆：迪化是配角脑补，虚张声势是主角主动误导。
  tags: [term, narrative-technique]

- id: g04
  term: 曝光流
  type: term
  source_chapter: 一、身份反差（衍生桥段）
  author_definition: |
    "主角姿态放低，却做出轰动大事"。
  key_distinction: |
    ≠ 身份揭晓 — 重点是'低姿态 + 高结果'的对比，不需要刻意打脸。
    = 无声碾压式的爽感。
  why_it_matters: |
    与'当众处刑'的区别：曝光流不打脸，只展示结果。
  tags: [term, narrative-technique]

- id: g05
  term: 信息差
  type: term
  source_chapter: 引言 + 一（配套情节）
  author_definition: |
    "利用双方掌握信息的不对称制造冲突与反转"（如反派搬出靠山，
    殊不知靠山刚被主角击败）。
  key_distinction: |
    ≠ 单纯隐瞒 — 信息差必须在'错误认知撞上真相'时引爆反转。
    = 反转类爽点的底层引擎，可独立成手法。
  why_it_matters: |
    三大底层逻辑（对比/反差/信息差）之一，可跨题材迁移。
  tags: [term, core-concept]

- id: g06
  term: 打脸 / 当众处刑
  type: term
  source_chapter: 三、打脸反转・当众处刑
  author_definition: |
    "配角炫耀、欺压、贬低主角，后续局势反转，配角颜面扫地"。
  key_distinction: |
    ≠ 私下逆转 — '当众'是核心变量，有目击者才有戏剧张力。
    = 公众预期崩塌式反转。
  why_it_matters: |
    C 类 6 个 skill 的共同识别词。
  tags: [term, core-concept]

- id: g07
  term: 越级反杀
  type: term
  source_chapter: 二、实力碾压・越级反杀
  author_definition: |
    "主角硬实力超出对手预期，越级杀敌、绝境反杀"。
  key_distinction: |
    ≠ 靠运气翻盘 — 核心是'硬实力超出预期'。
    = 预期差框架的战斗化表达。
  why_it_matters: |
    与'绝境'组合时需避免落入机械降神。
  tags: [term, core-concept]

- id: g08
  term: 金手指
  type: term
  source_chapter: 二、实力碾压・越级反杀
  author_definition: |
    "天赋、功法、神器、高人靠山；失传、传说级的能力宝物"。
  key_distinction: |
    ≠ 单纯外挂 — 源文档强调资源碾压（含'宝物像地摊货一样随意赠送'）。
    = 主角优势的系统化来源。
  why_it_matters: |
    与'弱点修复'配套构成成长弧线。
  tags: [term, core-concept]

- id: g09
  term: 降智
  type: term
  source_chapter: 四、通用创作要点（风险提醒）
  author_definition: |
    "强行让配角做出不符常理的愚蠢行为，以便主角打脸"。
  key_distinction: |
    ≠ 正常冲突 — 降智是作者干预角色的合理性，读者会立刻察觉。
    = 最典型的写作雷区，所有打脸 skill 的 B 段必查项。
  why_it_matters: |
    校验剧本爽点时的反向检查词：配角行为是否合理。
  tags: [term, red-flag]

- id: g10
  term: 马甲（多重身份）
  type: term
  source_chapter: 一、身份反差・隐藏大佬
  author_definition: |
    "主角同时拥有多个赫赫有名的代号，旁人却不知道都是主角一人"。
  key_distinction: |
    ≠ 化名 — 马甲必须各自'赫赫有名'，且互相独立存在。
    = 信息差最大化的身份结构。
  why_it_matters: |
    a03 多重马甲 skill 的核心术语。
  tags: [term, narrative-technique]
```

## 自检

- [x] 每条有 author_definition
- [x] 每条有 key_distinction
- [x] 每条有 why_it_matters
- [x] 只收真正关键的术语（10 条）
