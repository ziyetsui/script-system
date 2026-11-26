# 剧本系统

## 简介

剧本系统是给编剧使用的 AI 工作包。只有一个生活点子时，可以让它比较谁来做主角、高潮由谁行动，再把选定的方向写成约 500 字的单集大纲。已有稿子时，可以只找一个能引出下一场的桥段，或让导演审稿岗位指出最先要改的动作。[在线查工具](https://ziyetsui.github.io/script-system/) · [编剧实战手册](docs/github-guide/roadmap.md)

**177 个 Skill、5 个编剧 Agent、1 套单集自动化。** 技能覆盖热点选题、故事选型、大纲与分场、人物与对白、喜剧桥段、审稿改稿、动画分镜和字幕校译。五个岗位分别是故事新编、爆款复刻、剧本模型、找梗、导演审稿。「招财童子」把它们串起来，从一张有出处的热点卡做到一版待编剧确认的推荐稿；它另附 1 个内部大纲开发 Skill。[五个岗位](#usage-agents) · [整集自动化](#usage-automation)

| 创作参考 | 收录范围 | 写稿时怎么用 |
| --- | --- | --- |
| 动画作品 | 片单有 **300 个编号条目**，保留译名和系列衍生条目，其中 89 项附本地资料入口。另有 40 项喜剧细查。 | 按片名找角色、镜头或单集案例。国际动画研究收录了 **10 个系列的 16 个故事**，可从《小猪佩奇》或《小羊肖恩》挑一场拆动作。[动画片单](skills/animation-writing-research/catalog-300.md) · [喜剧细查](skills/animation-writing-research/comedy-40.md) · [国际故事卡](skills/animation-writing-research/international/README.md) |
| 动画导演 | **2 位动画导演、3 个具名视角技能**。曹小卉有 1 个，宫崎骏有 2 个。 | 儿童动作像在背词时用[曹导审稿](skills/cao-xiaohui-perspective/SKILL.md)；想换孩子看世界的角度，用[宫崎骏创作视角](skills/miyazaki-skill/SKILL.md)；要安排光影和镜头，用[宫崎骏动画镜头设计](skills/hayaomiyazaki-perspective/SKILL.md)。 |
| 家庭喜剧 | **3 部剧集、526 个本地集标、1,110 张可检索梗卡**。《我爱我家》120 个集标、355 张卡；《成长的烦恼》157 个集标、288 张卡；《摩登家庭》249 个集标、467 张卡。 | 用“好心帮倒忙”“两条线怎样会合”这类眼前的难题找原剧动作，再用自己的人物重写下一场。[跨剧找梗示范](skills/trope-library/编剧调梗.md) |
| 人物与短剧 | **52 个动画人物技能、14 个《西游记》原著人物技能、26 个短剧桥段与爽点技能**，均计入上述 177 个 Skill。 | 同一场争执可以换角色试演，也可以挑一个身份揭晓或信息差桥段，比较哪一版的后果更适合本集。[动画人物](#usage-characters) · [西游人物](#usage-journey) · [短剧桥段](#usage-short-drama) |

## Setup · 在 Codex 里说“帮我安装”

在 Codex 打开准备写稿的文件夹，把这一句发给它：

```text
帮我安装剧本系统（https://github.com/ziyetsui/script-system），在当前项目下载或复用工作包，读里面的「skills/故事开发/SKILL.md」告诉我怎么开始写大纲。
```

看到 Codex 读出技能名 **「写大纲」**，就可以发第一个点子：“爷爷想歇一天，小宁却替他接了六辆车的修理活，请先给我两个不同的高潮让我选。” 工作包就位后，下面各表的提示词都从含有 `skills/` 的目录读取文件。[详细上手指南](docs/github-guide/README.md) · [PDF 手册](docs/github-guide/roadmap.pdf) · [离线 HTML](docs/github-guide/roadmap.html)

## 新手入门 · 最好用的三句芝麻开门

**记一种写法就够了：`/技能名称 + 想让它帮忙的那件事`。** 比如 `/写大纲 小宁想让爷爷歇一天，却替他接了六辆车的活，请给我两个不同的高潮让我选。` 所有技能都可以按本页的中文名或英文名点名。斜杠菜单取决于当前工具注册了哪些命令；如果菜单里找不到，就在普通对话里说“用剧本系统里的『写大纲』帮我……”，Codex 可以按 README 找到对应的技能文件。

> **Tips｜为什么大多数 Skill 用英文命名？** 建库时优先沿用英文编剧术语，让 Codex 能按原名找到对应的写作方法。比如看到 `story-circle`，可以直接用中文说：“用哈蒙故事圈帮我看看，小宁为了查清这张照片付出了什么代价？”下表把中英文名称并排列出，写需求、贴原稿和提修改意见都可以用中文。

### ① `/热点` 找选题

```text
/热点 我想给《北京一家人》写一集关于科学探索精神的故事，请找三条有原文可查的北京生活新闻，每条附出处和一件小宁可能想亲手验证的事。
```

挑一条你想往下写的新闻，把报道原文和为小宁设想的动作分开留好。[热点选题](skills/hotspot/SKILL.md)

### ② `/群策` 从选中的新闻挖故事

```text
/群策 我选平谷小学地质科普课这条新闻，请让导演审稿、剧本模型和找梗各试一条故事线，写清小宁先信了什么、哪件事让他改主意、最后得舍掉什么，等我选。
```

把例句里的新闻换成你选的那条。群策会先查技能库，挑出这次用得上的方法；支持多个 Agent 时，各组可以同时试写。读完候选，选你最想看下去的那场戏。[群策分派规则](skills/swarm/SKILL.md)

### ③ `用剧本系统skill` 把选中的一场改顺

```text
用剧本系统skill 帮我改小宁拿到旧车票就去查救援这段，挑一个适合写探案线索的技能，让他先认出照片里自家的黄被子，再有理由去问爷爷。
```

有想用的方法可以点名，比如借柯南式线索、哆啦A梦的道具或《老友记》的群像误会；拿不准时，贴上原段，说清哪一拍让你没看懂就行。[柯南式线索设计](skills/conan-skill/SKILL.md) · [哆啦A梦角色卡](skills/animation-character-skills/doraemon-skill/SKILL.md)

## 实例 · 四轮写出《纸窗内外》

一堂讲山体滑坡的小学科普课，怎么会写成一个孩子追问“陌生男孩为什么盖着我的被子”的故事？下面把这集的 38 条创作提示整理成四轮。按顺序把这四句发给同一个 Codex 对话即可。提示词为教学改写，三个候选和结尾都可回查。[38 条原始提示词回顾](docs/example/《纸窗内外》-38条提示词回顾.md) · [完整大纲](docs/example/《纸窗内外》-最终大纲.md)

### 1. 热点：先找能让孩子动手的一件事

```text
/热点 这集想写科学探索精神，请从平谷靠山集中心小学地质科普课的报道里找一件孩子能亲手验证的事，分开写课堂事实和康小宁回家后的设想。
```

**这轮拿到的线头**：课堂上，讲师用野外影像和模型讲地质现象。到了康家，小宁看到院墙上的斜缝，想在学校科普展上用模型还原它。编剧现在可以抓住一个问题往下写：**照片和模型看起来一样，就能说明墙是这样裂的吗？** 原会话里，这堂课是热点列表的第 10 条。[当时选用的报道](https://www.geosociety.org.cn/?v1=v14&v2=6abe2d0113f7d&v3=v41&v4=v17&v6=1)

### 2. 群策：同一条新闻里，有哪些故事可挖？

```text
/群策 请从这堂地质科普课挖出三个能独立成集的故事，各写小宁原本相信什么、看见什么才起疑、最后得舍掉什么，等我选。
```

| 群策给出的候选 | 编剧可以挑哪场戏 |
| --- | --- |
| 《跟着山跑的尺子》 | 牙签尺和坡面一起移动，小宁误以为山没动。要重新测，就得亲手浇坏他做了两晚的纸灯笼铺。 |
| 《照片里那道缝》 | 同一摞照片，一家人排出了三种先后顺序。小宁发现拍摄角度就能让裂缝显得更宽，得撤回已经装裱好的展板。 |
| 《纸窗外面》 | 透过纸板方孔，画上去的线和两块板之间的缝一模一样。小宁把印好的主持卡扣下，把科普展第一个上台的位置让给下一组。 |

系统首推第一条，编剧选了**第三条**。吸引编剧的是照片被裁掉的另一半：小宁原本只想看清墙，那一半里还可能有谁？

### 3. 深挖：告诉系统“我的直觉是……”

```text
/柯南式线索设计 我选《纸窗外面》，直觉是照片外藏着一件感人的事，请沿照片边缘挖两条探案线，其中一条接上 K396 救援，标出小宁看见的虚构线索和能核对的事实。
```

**这集沿着被角往下写了**：整张照片里，墙根坐着一个陌生男孩。小宁认出男孩身上那床黄被子，被角的小船是他小时候央爷爷绣的。他有理由去问爷爷：“他怎么盖着我的被子？”接下来翻出旧车票、查车次，就都有了来由。男孩、黄被子和康家旧照是本集的虚构线索。

### 4. 改稿：指出“哪一拍不对”，再看替换后的戏

```text
/写大纲 小宁拿票就搜救援像是提前知道了答案，请只重写从收模型到查车次这一段，让他先认出男孩身上的黄被子，再想查他去了哪里，把照片背面的“小康家”留到最后。
```

**可以这样改（按成稿压缩）**：小宁回家把模型往抽屉里塞，底座顶住一本旧相册。他把相册抽出来，一张照片滑到桌上。还是那道墙缝，可照片边上坐着个男孩，身上那床黄被子露出半只绣歪的小船。小宁把照片举到爷爷眼前：“他怎么盖着我的被子？”爷爷认出照片，让他摸摸封底的纸袋。小宁抽出一张终点北京丰台的旧票。他想知道男孩后来去了哪儿，这才把车次和日期输进去，却读到列车当年停在了落坡岭。

这次改动给了小宁一个**查车次之前就已经在乎的问题**。它也能撑到结尾：科普展上，童子又问“那他最后，到哪儿了？”，小宁把照片翻过来：“你自己看。”背面只有三个字——**小康家**。

## 三个常用入口

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [写大纲](skills/故事开发/SKILL.md) | Story Outline Development | 有一个点子，想先理清行动和后果，再写成大纲。 | /写大纲 小宁发修车号却收了一桌钥匙，写三步后果逼他亲自撤单。 |
| [找梗](agents/找梗.md) | Trope Finder<br>`trope-finder` | 前后两场已经定了，中间还缺一个让人物非接招不可的动作。 | 找梗岗位，小宁发完修车号又想撤单，给两个能让他改主意的中间动作。 |
| [招财童子](automations/招财童子/FOR_AGENTS.md) | Fortune Child | 已经选好一张有出处的热点卡，想拿到整集推荐稿。 | 招财童子自动化，请用我选定的热点卡写约五百字的单集推荐稿，标上待反馈稿号。 |

[浏览技能清单](skills/编剧技能清单.md) · [查看历史首轮试跑](skills/试跑记录/2026-11-26/README.md) · [项目创作资料](docs/harness/)

## 按任务查用法

在含有 `skills/`、`agents/` 和 `automations/` 的仓库根目录打开 Codex、Claude Code 或 Cursor，按手上的任务选一行，复制末栏的整句。用自己的题材替换示例，涉及热点卡、旧稿或原作片段时，把材料一同贴上。

独自写一场戏时可用 `/找梗`，整集协作时可把候选交给找梗岗位。`群策` 和 `swarm` 共用分派规则。点「历史答卷」可查看当时的实际交付。


| 手上的任务 | 在本页查哪里 |
| --- | --- |
| 已选带来源的热点，要交一整集 | [招财童子自动化（2 项）](#usage-automation) |
| 要找人接手取材、选型、找梗或审稿 | [五个编剧岗位（5 项）](#usage-agents) |
| 一个卡点要试几条走法 | [找梗与多方案比较（3 项）](#usage-dispatch) |
| 只有点子，还没选主题、主角或高潮 | [选题与选型（7 项）](#usage-writing) |
| 已选方向，开始铺大纲或分场 | [大纲与结构（13 项）](#usage-structure) |
| 前后两场之间缺一个会引发后果的动作 | [桥段与场景（16 项）](#usage-scenes) |
| 对白反复，或包袱落地后剧情停住 | [对白与喜剧（7 项）](#usage-comedy) |
| 拿着旧稿找最早失效的一拍 | [审稿与改稿（10 项）](#usage-revision) |
| 想换人物观察方式、口吻或叙述节奏 | [人物与文风（11 项）](#usage-voice) |
| 要做镜头表、分镜、分镜提示词或素材 | [动画制作（9 项）](#usage-animation) |
| 需查资料、译词、考据或改写 | [翻译与辅助（9 项）](#usage-support) |
| 设计短剧的揭晓、升级或回收 | [短剧桥段与爽点（26 项）](#usage-short-drama) |
| 按《西游记》原著口吻试一场 | [西游人物（14 项）](#usage-journey) |
| 换动画角色试演具体行动 | [动画人物（52 项）](#usage-characters) |
| 按词找技能、对照镜头或原剧 | [配套资料和查询命令](#usage-resources) |

<a id="usage-automation"></a>

## 招财童子自动化

在仓库根贴入已选热点卡，再用下表第一项。若已有一版稿，只需检查关键戏和返工环节，可直接选第二项。编剧明确认可后才登记对应的定稿版本。[续改示范](docs/github-guide/roadmap.md#section-handoff)

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [招财童子](automations/招财童子/FOR_AGENTS.md)<br>教学示例 | Fortune Child | 热点已选，想从一张真实材料卡直接得到一集可读的推荐稿。 | 招财童子自动化，请对照热点卡比较典故和原剧两案，交约五百字的推荐稿并说明取舍。 |
| [单集大纲开发](automations/招财童子/skills/develop-outline/SKILL.md)<br>教学示例 | Episode Outline Development<br>`develop-outline` | 候选已交到招财童子手里，需要查清它如何比较、试写、返工。 | /develop-outline 请替招财童子自动化试写小宁拦奶奶赴约这场争执，把经得起试演的转折写回大纲。 |

<a id="usage-agents"></a>

## 五个编剧岗位

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [故事新编](agents/故事新编.md)<br>教学示例 | Story Reteller<br>`story-reteller` | 有教育题或典故，需要把两难换成北京孩子自己的选择。 | 故事新编岗位，请借《曾子杀猪》写一张康家故事卡，让小宁为爸爸的随口承诺付出代价。 |
| [爆款复刻](agents/爆款复刻.md)<br>教学示例 | Reference Adapter<br>`reference-adapter` | 想借一部成熟剧集的具体机制，已经知道本集卡在什么地方。 | 爆款复刻岗位，请找一场能核到集数的群口露馅戏，改成爷爷用一把修车钥匙揭穿父子俩。 |
| [剧本模型](agents/剧本模型.md)<br>教学示例 | Story Model<br>`story-model` | 已有候选，选不定主角、升级方式或高潮。 | 剧本模型岗位，小宁替想歇业的爷爷接了活，比较小宁撤单和爷爷拒修两个高潮各让谁吃亏。 |
| [找梗](agents/找梗.md)<br>教学示例 | Trope Finder<br>`trope-finder` | 候选已定，要把一场具体的断点交给专人找接法。 | 找梗岗位，小宁想管好修车队伍，请用院门、车铃和一把锁找两种越管越乱的桥段并附出处。 |
| [导演审稿](agents/导演审稿.md)<br>教学示例 | Outline Director<br>`outline-director` | 已有完整大纲和难写的关键戏，准备决定是否返工。 | 导演审稿岗位，请按五项标准复审奶奶出门赴约这场戏，指出最先该返工的动作。 |

<a id="usage-dispatch"></a>

## 找梗与多方案比较

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [找梗](skills/找梗/SKILL.md)<br>教学示例 | Trope Search | 中段人物反复说同一句话，下一场没人接招。 | /找梗 小宁想留奶奶看戏，给两个不用电话也能让她按时赴约的下一拍。 |
| [群策](skills/群策/SKILL.md)<br>教学示例 | Writers’ Room Brainstorm | 还没定下要写哪种高潮，想把同一难题交给几个创作方向比较。 | /群策 奶奶赴约和小宁开演撞了时间，给三种代价不同的收场办法。 |
| [群策（英文入口）](skills/swarm/SKILL.md)<br>教学示例 | Swarm<br>`swarm` | 同一份稿能朝多种方向改，想请几个方向各自试一遍，最后合并重复建议。 | /swarm 奶奶刚跨出门，分别用结构、家庭喜剧和动画动作给小宁试一个送别结尾。 |

<a id="usage-writing"></a>

## 选题与选型

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [前提、主题与戏核](skills/sw-premise-theme/SKILL.md)<br>教学示例 | Premise and Theme<br>`sw-premise-theme` | 有教育主题，想试出它能靠哪一个高潮动作成立。 | /sw-premise-theme 小宁非要奶奶留下看戏，把他学会尊重奶奶的那一刻写成一个送她赴约的动作。 |
| [斯奈德选型](skills/snyder-genre-choice/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-001) | Snyder Genre Selection<br>`snyder-genre-choice` | 用两种类型的高潮检验选型。 | /斯奈德选型 校乐队散伙前还有最后一场演出，用伙伴之情和变迁仪式各写一个台上高潮。 |
| [单集故事选型](skills/aiscript-story-type/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-002) | Episode Story Type Selection<br>`aiscript-story-type` | 为单集点子比较故事类型。 | /aiscript-story-type 爸爸随口许诺却要付代价才能兑现，用两种故事类型各推一个高潮供我选。 |
| [BMad 头脑风暴](skills/bmad-brainstorming/SKILL.md)<br>[有缺口 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-003) | BMad Brainstorming<br>`bmad-brainstorming` | 用不同限制发散单集点子。 | /bmad-brainstorming 全家停电只能在厨房拍，接着爸爸抢当手电筒管理员的点子给我一个新限制。 |
| [热点选题](skills/hotspot/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-004) | News-Based Story Ideas<br>`hotspot` | 为北京一家人核实新闻选题。 | /hotspot 从近三个月北京报道里找三条孩子替老人做主的选题，每条附原文和一个可拍动作。 |
| [公版名著改编短剧](skills/screenwriter/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-005) | Short Drama from Classic Literature<br>`screenwriter` | 从公版名著选材编照片短剧。 | /screenwriter 我有老站台、票夹和撑伞人的照片，选两张有出处的名著卡供我拍九十秒离别短片。 |
| [新闻选题提案](skills/story-pitch/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-006) | News Story Pitch<br>`story-pitch` | 为新闻编辑撰写选题投稿信。 | /story-pitch 末班渡轮下周停航，用船长和两名夜班护士的采访线索给城市周报写封投稿信。 |

<a id="usage-structure"></a>

## 大纲与结构

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [菲尔德情节点](skills/field-plot-point/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-007) | Field Plot Points<br>`field-plot-point` | 让转折消息改变下一场任务。 | /菲尔德情节点 女儿已报平安，改一句电话里的话，让爸爸下一场有比继续找人更急的事。 |
| [写大纲](skills/故事开发/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-008) | Story Outline Development | 从故事点子写起承转合大纲。 | /写大纲 爷爷想歇一天却被小宁接满修车单，写约五百字大纲，让小宁亲手收拾补救惹出的麻烦。 |
| [故事改编整合](skills/adaptation-synthesis/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-009) | Story Adaptation Synthesis<br>`adaptation-synthesis` | 按已提取的故事功能改编新作。 | /adaptation-synthesis 把账房学徒发现错账却会连累师父的困局搬进小学戏剧节，用一场彩排试出来。 |
| [番茄短故事](skills/fanqie-short-story.skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-010) | Fanqie Short Fiction<br>`fanqie-short-story`<br>目录 `fanqie-short-story.skill` | 设计番茄短故事导语与情节。 | /fanqie-short-story 裁缝铺交钥匙时女儿发现停业牌背面的取衣日期，用它写八千字家庭短篇的导语和章纲。 |
| [马伯庸式历史故事构思](skills/maborong-creation/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-011) | Historical Story Development in the Style of Ma Boyong<br>`maborong-creation` | 从历史细节搭建小人物困局。 | /马伯庸式历史故事构思 唐代驿卒要在封城前送达错名调令，写一城一昼夜的三段梗概并标出待考手续。 |
| [网文章节节奏](skills/novel-pacing/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-012) | Web Fiction Pacing<br>`novel-pacing` | 安排网文章节的压抑与兑现。 | /novel-pacing 学徒被退单后听出了异响，重排开篇三章，让退单的人亲眼看到他修好车。 |
| [皮克斯六句故事提案](skills/pixar-pitch/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-013) | Pixar Pitch<br>`pixar-pitch` | 用六句因果讲清一次转变。 | /pixar-pitch 把食堂改用黑板订餐后邻居开始替老人留饭的故事写成六句，让两个「因此」各带出一个后果。 |
| [迈克尔·阿恩特高潮设计](skills/screenwriter-michael-arndt/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-014) | Michael Arndt’s Climax Design<br>`screenwriter-michael-arndt` | 从高潮抉择倒推三重利害。 | /screenwriter-michael-arndt 队友抄了近路，从小宁冲线前的一个选择倒推三拍，让奖杯和友情同时受考验。 |
| [哈蒙故事圈](skills/story-circle/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-015) | Harmon Story Circle<br>`story-circle` | 用哈蒙八步故事圈设计单集。 | /story-circle 小宁第一次独自去夜市讨修车钱，用八步故事圈写出拿到钱后他付了什么代价。 |
| [斯奈德十五节拍表](skills/story-design-beat-sheet/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-01.md#run-016) | Save the Cat Beat Sheet<br>`story-design-beat-sheet` | 给选定的故事排斯奈德十五节拍。 | /story-design-beat-sheet 爸爸误把孩子买鱼竿当成想去钓鱼，排十五个节拍，让开头和结尾落在同一钓位。 |
| [三幕结构与分场](skills/sw-story-structure/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-017) | Three-Act Story Structure<br>`sw-story-structure` | 用三幕式编排单集分场大纲。 | /sw-story-structure 爸爸按孩子的搜索记录准备惊喜却带错路，把他出发、改主意和最后选择排成三幕。 |
| [特鲁比故事解剖](skills/sw-truby-anatomy/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-018) | Truby’s Anatomy of Story<br>`sw-truby-anatomy` | 用特鲁比揭示与决定修复中段。 | /sw-truby-anatomy 小宁伪造好评想保住修车摊，给三组新发现和决定，把他逼到当众认错的关口。 |
| [知乎短篇构思](skills/zhihu-short-story/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-019) | Zhihu Short Fiction<br>`zhihu-short-story` | 用雪花法逐层构思知乎短篇。 | /zhihu-short-story 明天的社区寻人启事登着我的照片，把这个反常之处写成二十五字内的开篇钩子。 |

<a id="usage-scenes"></a>

## 桥段与场景

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [契诃夫改判](skills/chekhov-changing-verdict/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-020) | Chekhov’s Changing Verdict<br>`chekhov-changing-verdict` | 用同一件事的改判写偏心。 | /契诃夫改判 操场窗户碎了，让值日生听到三个不同的名字后对同一块玻璃下三道不同的命令。 |
| [《成长的烦恼》梗库](skills/growing-pains-tropes/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-021) | Growing Pains Tropes<br>`growing-pains-tropes` | 查成长的烦恼梗卡改家庭戏。 | /growing-pains-tropes 妹妹替藏坏录音机的哥哥求情，找两张越帮越忙的原剧梗卡并标出集名和时间。 |
| [快乐王子善举](skills/happy-prince-cost/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-022) | The Cost of Kindness in The Happy Prince<br>`happy-prince-cost` | 让上一次善举改变下一次代价。 | /快乐王子善举 爷爷三次送伞，把每次少掉的东西变成他下一次帮人时的难处。 |
| [西游三叠](skills/journey-repeated-trials/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-023) | Repeated Trials in Journey to the West<br>`journey-repeated-trials` | 让三次相遇逐次封住旧解法。 | /西游三叠 守门人连拦主角三次，改第二次求情的后果，让主角第三次非换招不可。 |
| [莫泊桑误判](skills/maupassant-misjudged-value/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-024) | Misjudged Value in Maupassant<br>`maupassant-misjudged-value` | 用价值误判写出有代价的结尾。 | /莫泊桑误判 小禾弄丢旧照片，分别用高估和低估照片价值写一个要付代价的结尾。 |
| [《摩登家庭》梗库](skills/modern-family-tropes/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-025) | Modern Family Tropes<br>`modern-family-tropes` | 查摩登家庭梗卡安排多线会合。 | /modern-family-tropes 奶奶要送走爸爸藏礼物的沙发，找两个能核到集号的原剧道具撞线桥段。 |
| [欧亨利交叉赠礼](skills/ohenry-crossed-gifts/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-026) | O. Henry’s Crossed Gifts<br>`ohenry-crossed-gifts` | 用交叉赠礼改写双人结局。 | /欧亨利交叉赠礼 兄妹互送毕业礼物，写到两人伸手试用时才发现对方为这件礼物舍掉了什么。 |
| [《我爱我家》梗库](skills/wo-ai-wo-jia-tropes/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-027) | I Love My Family Tropes<br>`wo-ai-wo-jia-tropes` | 从我爱我家逐集梗卡找接法。 | /wo-ai-wo-jia-tropes 修车摊涨价后爸爸却按旧价收钱，找两张有集号和时间的原剧梗卡各续一场。 |
| [疯狂动物城道具](skills/zootopia-prop-handoff/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-028) | Zootopia Prop Handoff<br>`zootopia-prop-handoff` | 用两次道具交接铺垫结尾。 | /疯狂动物城道具 弟弟最后要开柜替姐姐作证，往前补两次钥匙交接，让他拿得到也懂得怎么用。 |
| [柯南式线索设计](skills/conan-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-029) | Detective Conan Clue Design<br>`conan-skill` | 用可见线索设计少年推理戏。 | /conan-skill 奶奶留客的糖饼不见了，只在小宁进过的两间屋布三条能支持两种解释的线索。 |
| [场景因果衔接](skills/scene-craft/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-030) | Scene-to-Scene Causality<br>`scene-craft` | 让一次补救的后果引出下一场。 | /scene-craft 爸爸想修玩具劝退排队的街坊，分别写修好了更麻烦、修坏了被撞见两个后果。 |
| [儿童故事开发](skills/story_skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-031) | Children’s Story Development<br>`children-story`<br>目录 `story_skill` | 按动画角色分工续写儿童桥段。 | /children-story 小宁替爷爷接了三辆坏车，给五岁孩子写三个能看懂的动作，让他的帮忙给旁人添个麻烦。 |
| [经典戏剧情境](skills/storytelling/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-02.md#run-032) | Classic Dramatic Situations<br>`storytelling` | 用经典戏剧情境推演下一场。 | /经典戏剧情境 爷孙准备同一场胡同比赛，用亲族竞争和为亲人牺牲各推一场戏。 |
| [马伯庸式历史悬念](skills/style-ma-boyong/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-033) | Historical Suspense in the Style of Ma Boyong<br>`style-ma-boyong` | 以史料空白和公文时限构思悬念。 | /style-ma-boyong 粮车出城却没有到仓签收，写小吏赶在明早封账前追查联单的三场戏。 |
| [美国电影编剧案例](skills/sw-american-case-studies/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-034) | American Screenwriting Case Studies<br>`sw-american-case-studies` | 从美国电影案例提取编剧手法。 | /sw-american-case-studies 姐妹送旧琴去修的三场戏可以互换，借《塞尔玛与路易丝》的转折改成三次被迫换招。 |
| [单场转折与潜台词](skills/sw-scene-craft/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-035) | Scene Turns and Subtext<br>`sw-scene-craft` | 用价值转折和潜台词重写单场。 | /sw-scene-craft 爷爷认定小宁丢了钥匙，写一场备用钥匙第二次露面才让他改口的戏。 |

<a id="usage-comedy"></a>

## 对白与喜剧

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [坎特维尔喜剧道具](skills/canterville-comic-prop/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-036) | The Canterville Ghost Comic Prop<br>`canterville-comic-prop` | 让人物主动取回嫌弃的道具。 | /坎特维尔喜剧道具 老师傅嫌徒弟的头灯丢人，写个笑点让他在末场亲自回来取灯。 |
| [麦基节拍](skills/mckee-scene-beats/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-037) | McKee Scene Beats<br>`mckee-scene-beats` | 用动作与回应改出对白换招。 | /麦基节拍 姐弟在校门口互推道歉，给各执一词的两人写一拍换招，让另一个人必须回应。 |
| [多线情景喜剧编剧](skills/comedy-scriptwriter/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-038) | Multi-Plot Sitcom Writing<br>`comedy-scriptwriter` | 编排情景喜剧的多线单集。 | /comedy-scriptwriter 爸爸想藏起烫坏的桌布，写一场女儿的全黑魔术排练反而让他露馅的戏。 |
| [信息差喜剧写作](skills/comedy-writing/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-039) | Information Gaps in Comedy<br>`comedy-writing` | 用信息差给短剧加笑点。 | /comedy-writing 爸爸把女儿录失物招领广播误听成练歌，用三拍升级误会并回收第一句台词。 |
| [罗温·艾金森肢体喜剧](skills/rowan-atkinson/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-040) | Rowan Atkinson Physical Comedy<br>`rowan-atkinson-expert`<br>目录 `rowan-atkinson` | 用克制的表情与停顿设计笑点。 | /rowan-atkinson-expert 主持人夸自己从不迟到时外套还夹在门外，用三个眼神或手势写二十秒的遮掩。 |
| [半小时情景喜剧](skills/sw-sitcom-comedy/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-041) | Half-Hour Sitcom Writing<br>`sw-sitcom-comedy` | 设计半小时情景喜剧的困境与笑点。 | /sw-sitcom-comedy 电梯停修时七楼的爸爸承诺替全楼送菜，在三个常设场景里排一集主副线相撞的喜剧。 |
| [情景喜剧工坊](skills/情景喜剧工坊/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-042) | Sitcom Workshop | 从情景喜剧卡挑选误会桥段。 | /情景喜剧工坊 爸爸和爷爷都替小宁瞒着做糖饼的事，给他们各写一句单听合理、合起来露馅的话。 |

<a id="usage-revision"></a>

## 审稿与改稿

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [曹导](skills/cao-xiaohui-perspective/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-043) | Cao Xiaohui’s Animation Review<br>`cao-xiaohui-perspective` | 从儿童动作审改动画场景。 | /曹导 把小宁说「好东西应该分享」改成静音也看得懂的动作，道具只用最后一张糖饼券。 |
| [梁左](skills/liang-zuo-perspective/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-044) | Liang Zuo’s Sitcom Review<br>`liang-zuo-perspective` | 用梁左的家庭喜剧写法改大纲。 | /梁左 小宁委屈奶奶没留下看戏，写到他愿意亲口问奶奶下回什么时候有空。 |
| [书库技法](skills/screenwriting-book-techniques/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-045) | Screenwriting Book Techniques<br>`screenwriting-book-techniques` | 按稿面症状选编剧书练习。 | /书库技法 妹妹三次讨糖饼都只换来摇头，挑一个书中练习改出三次不同的回应。 |
| [索金式段落诊断](skills/cw-sorkin/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-046) | Sorkin-Style Writing Diagnosis<br>`cw-sorkin` | 逐段诊断文字停滞并试改。 | /cw-sorkin 闭馆还剩两分钟，用借书证和关灯动作改写三句对白，让每句都逼下一人行动。 |
| [网文黄金三章](skills/golden-three/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-047) | The First Three Chapters<br>`golden-three` | 诊断网文前三章的留人节奏。 | /golden-three 送信员第二章才收到明天寄出的信，重排开篇三章，让每章都有值得追下去的疑问。 |
| [皮克斯故事会诊](skills/pixar-storyteller/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-03.md#run-048) | Pixar Story Review<br>`pixar-storyteller` | 用皮克斯创作会诊断情感转折。 | /pixar-storyteller 小宁藏车怕爷爷摔倒，爷爷买车后他立刻道歉，请用三条看片笔记指出情绪在哪一拍断了。 |
| [三轮成稿审读](skills/protocol-craft/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-049) | Three-Pass Draft Review<br>`protocol-craft` | 分三遍审读成稿并排定改稿顺序。 | /protocol-craft 小宁宣布修车免费却收到游戏币，从投入感、结构和台词三遍审读这场戏。 |
| [无对白喜剧分镜审读](skills/readability-comedy-slapstick/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-050) | Slapstick Storyboard Readability<br>`readability-comedy-slapstick` | 审查无对白分镜的道具因果。 | /readability-comedy-slapstick 爸爸抽走报修单时纸飞了，逐镜指出该在哪里停一拍让观众误以为他得手。 |
| [口播故事因果改稿](skills/storytelling-content-skills/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-051) | Causal Storytelling for Spoken Content<br>`storytelling`<br>目录 `storytelling-content-skills` | 用转折和因果串起口播故事。 | /口播故事因果改稿 小宁接活、爸爸藏车、街坊找车，只改藏车的动作，让街坊非来找不可。 |
| [强化章末钩子](skills/通用-强化章末钩子/SKILL.md)<br>[有缺口 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-052) | Chapter-Ending Hooks | 核对原设定后局部改强章末。 | /通用-强化章末钩子 从没赊账的林秋在账尾看见自己的名字，改写末尾两百字，让她找签字人的动作悬在半途。 |

<a id="usage-voice"></a>

## 人物与文风

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [陈萍萍人物视角](skills/chenpingping-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-053) | Chen Pingping Character Perspective<br>`chenpingping-skill` | 用陈萍萍的矛盾塑造谋臣。 | /chenpingping-skill 替旧友翻案的老臣正是当年压下申诉的人，用轮椅旁的一个动作写出他的矛盾。 |
| [柯南侦探视角](skills/conan-detective-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-054) | Detective Conan’s Perspective<br>`conan-detective`<br>目录 `conan-detective-skill` | 用柯南第一人称查找矛盾。 | /conan-detective 钟指四点十分却响起四点铃声，用侦探的口吻问一个能区分钟错和彩排录音的问题。 |
| [韩非子视角](skills/hanfeizi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-055) | Han Feizi’s Perspective<br>`hanfeizi-perspective`<br>目录 `hanfeizi-skill` | 用韩非子视角分析制度与人心。 | /hanfeizi-perspective 上报失物能加分，同一支铅笔竟报了六次，写则百字寓言让孩子看懂该改哪条规定。 |
| [宫崎骏创作视角](skills/miyazaki-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-056) | Hayao Miyazaki’s Creative Perspective<br>`miyazaki-perspective`<br>目录 `miyazaki-skill` | 从儿童与自然视角推敲创作取舍。 | /miyazaki-perspective 停水车能让鱼洄游却会耽误磨面，给孩子一个亲自查证的动作和两个各有代价的结尾。 |
| [《纽约客》人物特写](skills/new-yorker-style/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-057) | New Yorker Profile Writing<br>`new-yorker-style` | 撰写纽约客式英文人物特写。 | /new-yorker-style 从修钟师傅分装客人发条的信封写起，用约一百三十个英文词写人物特写开头。 |
| [琼瑶式言情对白](skills/qiongyao-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-058) | Romantic Dialogue in the Style of Qiong Yao<br>`qiongyao-perspective`<br>目录 `qiongyao-skill` | 设计言情剧的误会与重逢对白。 | /qiongyao-perspective 女儿重逢误以为她退信的旧爱，写八句对白，让误会松动时的称呼变一次。 |
| [《红楼梦》文风](skills/style-hongloumeng/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-059) | Dream of the Red Chamber Style<br>`style-hongloumeng` | 用红楼梦语感改写人物叙事。 | /style-hongloumeng 把姨妈推回凉茶、侄女低头理袖写成一段，用亲属称谓和停顿带出两人的心思。 |
| [《三国演义》文风](skills/style-sanguo/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-060) | Romance of the Three Kingdoms Style<br>`style-sanguo` | 用三国演义语感改写叙事。 | /style-sanguo 雨淹两路后守桥人指向山腰，用简练的章回笔法写到信使收信牵马转身。 |
| [《水浒传》文风](skills/style-shuihu/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-061) | Water Margin Style<br>`style-shuihu` | 用水浒传语感改写市井动作。 | /style-shuihu 伙计认出欠账客又把板凳放回门槛，用称谓和搬凳的动作写出火气。 |
| [《西游记》文风](skills/style-xiyouji/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-062) | Journey to the West Style<br>`style-xiyouji` | 用西游记语感改写奇遇场面。 | /style-xiyouji 樵夫听见空筐喊自己的名字，用说书口吻写到他解下筐滚出一颗会说话的桃核。 |
| [《庆余年》权谋叙事](skills/xin-maoni-style-qingyunian/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-063) | Political Intrigue in Joy of Life<br>`xin-maoni-style-qingyunian` | 用庆余年双重视角写权谋场景。 | /xin-maoni-style-qingyunian 赈粮总数没错却多了一排领粮人，写小官在朝堂上靠一次心算看出蹊跷的场景。 |

<a id="usage-animation"></a>

## 动画制作

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [黏土定格广告](skills/claymation-ad/SKILL.md)<br>[有缺口 · 历史答卷](skills/试跑记录/2026-11-26/group-04.md#run-064) | Claymation Advertising<br>`claymation-ad` | 制作黏土定格品牌广告。 | /claymation-ad 黏土小熊的午餐汤汁洇湿了信，请为团团饭盒设计五段竖屏广告动作供我先看。 |
| [宫崎骏动画镜头设计](skills/hayaomiyazaki-perspective/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-065) | Miyazaki-Style Animation Cinematography<br>`hayaomiyazaki-perspective` | 设计儿童动画的光影与镜头。 | /hayaomiyazaki-perspective 女孩在停驶缆车的积水里发现蝌蚪，用三个镜头写出她目光停住的那一刻。 |
| [儿童动画角色设定](skills/kids-concept-creator/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-066) | Children’s Animation Concept Design<br>`kids-concept-creator` | 设计儿童动画角色与参考图。 | /kids-concept-creator 给剪纸动画《修伞的小獾》做角色设定，让高过头的黄伞和数伞骨的习惯一眼可认。 |
| [儿童动画短镜头编剧](skills/kids-script-writer/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-067) | Short Scenes for Children’s Animation<br>`kids-script-writer` | 拆写儿童动画八秒镜头提示词。 | /kids-script-writer 剪纸小獾用黄伞帮乌龟过桥，按角色参考图写三个各八秒的横屏镜头提示词。 |
| [连载漫剧分镜](skills/manjuforge/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-068) | Serialized Comic Drama Storyboarding<br>`manjuforge` | 编写连载漫剧分镜并跟踪伏笔。 | /manjuforge 修旧钟的学徒收到一只倒走的校钟，写首集一分钟竖屏分镜并记下留给下集的线索。 |
| [追逐喜剧插画](skills/slapstick-art/SKILL.md)<br>[有缺口 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-069) | Slapstick Illustration<br>`slapstick-art` | 生成原创猫鼠追逐的缓存示意图。 | /slapstick-art 画一张横屏卡通图，让小鼠拉开空抽屉、大猫取回资料并留一份在抽屉里，讲清缓存回填。 |
| [上美影风格分镜](skills/smy-seedance-storyboard/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-070) | Shanghai Animation Style Storyboards for Seedance<br>`smy-seedance-storyboard` | 编写上美影风格短剧分镜提示词。 | /smy-seedance-storyboard 学徒给灶王像补眼后全街的糊锅都被看见了，先写三集各十五秒的手绘动画大纲。 |
| [无对白喜剧分镜](skills/storyboarder-situational-comedy/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-071) | Visual Comedy Storyboarding<br>`storyboarder-situational-comedy` | 把无对白喜剧动作拆成分镜。 | /storyboarder-situational-comedy 爸爸从睡着的爷爷手下抽报修单，用四到六个无对白镜头让他刚以为得手就被小宁撞见。 |
| [动画短片故事与镜头设计](skills/storycraft/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-072) | Animated Short Story and Shot Design<br>`storycraft` | 为动画短片编制故事与镜头文档。 | /storycraft 守夜人发现雨衣挡住了灯塔的光，写一分钟无对白短片梗概，让末镜回应首镜。 |

<a id="usage-support"></a>

## 翻译与辅助

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [儿童睡前故事](skills/bedtime-story/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-073) | Bedtime Stories<br>`bedtime-story` | 把寓言讲成儿童睡前故事。 | /bedtime-story 给五岁孩子写一段能慢慢念的《乌鸦喝水》，在水升高时留一个轻声问他的问题。 |
| [创作细节考证](skills/creative-research/SKILL.md)<br>[有缺口 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-074) | Creative Research<br>`creative-research` | 查证故事中的年代与生活细节。 | /creative-research 核对一九八五年北京孩子买蜂窝煤该去哪儿、带什么凭证，每个能查实的细节附出处。 |
| [双语成语练习](skills/daily-idiom/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-075) | Bilingual Idiom Practice<br>`daily-idiom` | 用中英双语学成语并自测。 | /daily-idiom 我以为「画蛇添足」是把东西做漂亮，请用中英双语讲清典故并出一道情境题。 |
| [哆啦A梦式日语讲解](skills/explaining-like-doraemon/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-076) | Doraemon-Style Explanations in Japanese<br>`explaining-like-doraemon` | 用日语角色对话重讲难点。 | /explaining-like-doraemon 用四轮日语问答帮大雄弄懂为什么删除符号链接后原文件还在。 |
| [《飞出个未来》字幕校译](skills/futurama-context/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-077) | Futurama Subtitle Review<br>`futurama-context` | 统一飞出个未来的字幕译名。 | /futurama-context 弗莱问这是不是自己首趟送货，把本德那句「你头一趟，我歇一趟」润成简短带刺的字幕。 |
| [寓言讲解](skills/parable/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-078) | Teaching through Parables<br>`parable` | 用寓言和两道题讲懂概念。 | /parable 周六免费修车也有机会成本，请先讲个不提修车的小寓言让我猜原因。 |
| [《瑞克和莫蒂》字幕校译](skills/rick-and-morty-context/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-079) | Rick and Morty Subtitle Review<br>`rick-and-morty-context` | 按瑞克和莫蒂设定校译字幕。 | /rick-and-morty-context 莫蒂误以为传送枪坏了，请把瑞克的「We're out of portal fluid」译成简中字幕。 |
| [《海绵宝宝》台词检索](skills/spongebob-quote/SKILL.md)<br>[受阻 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-080) | SpongeBob Quote Lookup<br>`spongebob-quote` | 按情境查海绵宝宝台词出处。 | /spongebob-quote 朋友头一回上台有点怯，找三条适合排练前发的短台词并标出原剧集名和时间。 |
| [《辛普森一家》字幕校译](skills/the-simpsons-context/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-05.md#run-081) | The Simpsons Subtitle Review<br>`the-simpsons-context` | 按辛普森一家地区译名校字幕。 | /the-simpsons-context 霍默听说核电厂是家就问家人能否替他上班，请给大陆和台湾观众各译一句保住笑点的字幕。 |

<a id="usage-short-drama"></a>

## 短剧桥段与爽点

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [大人物俯首](skills/400-duanju-shuangdian/a-shenfen-fancha/a01-darenwu-fushou/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-082) | When the Powerful Bow<br>`darenwu-fushou`<br>目录 `a01-darenwu-fushou` | 用权威者的反常礼遇暗示身份。 | /darenwu-fushou 戏院开幕时名旦替收票老人拉开主位，用经理慢半拍才收回的手势写出众人的意外。 |
| [微服被刁难・有眼不识泰山](skills/400-duanju-shuangdian/a-shenfen-fancha/a02-weifu-bei-diaonan/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-083) | The Unrecognized VIP<br>`weifu-bei-diaonan`<br>目录 `a02-weifu-bei-diaonan` | 安排短剧桥段时，想让微服主角受阻后当众揭晓身份。 | /weifu-bei-diaonan 便装店主被前台让走最后一间房，写到开业仪式揭晓身份时前台收回那句推辞。 |
| [多重马甲](skills/400-duanju-shuangdian/a-shenfen-fancha/a03-duochong-majia/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-084) | Multiple Secret Identities<br>`duochong-majia`<br>目录 `a03-duochong-majia` | 安排短剧桥段时，想编排多重身份的线索与揭晓顺序。 | /duochong-majia 女主既匿名点歌又给老电影配乐，分三集让声音和手稿先后泄露她的身份。 |
| [幕后大佬](skills/400-duanju-shuangdian/a-shenfen-fancha/a04-muhou-dalao/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-085) | The Power Behind the Scenes<br>`muhou-dalao`<br>目录 `a04-muhou-dalao` | 安排短剧桥段时，想让门生当众认师揭开幕后身份。 | /muhou-dalao 老裁缝被笑只会缝扣子，让两位获奖设计师各拿一件曾被他救回的衣服认师。 |
| [亲友不知情](skills/400-duanju-shuangdian/a-shenfen-fancha/a05-qinyou-buzhiqing/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-086) | Family in the Dark<br>`qinyou-buzhiqing`<br>目录 `a05-qinyou-buzhiqing` | 用家人误会对照主角的外部声望。 | /qinyou-buzhiqing 父亲把女儿的签绘当零工，让他从一个只有父女懂的画中细节认出这位匿名画家。 |
| [扫地僧式角色](skills/400-duanju-shuangdian/a-shenfen-fancha/a06-saodiseng-shijue/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-087) | The Unassuming Master<br>`saodiseng-shijue`<br>目录 `a06-saodiseng-shijue` | 安排短剧桥段时，想从旁观视角揭开不起眼的高手。 | /saodiseng-shijue 镇店老钟漏了一拍，借学徒早先见过的扫地动作揭出老人的本事。 |
| [物件与外貌反差](skills/400-duanju-shuangdian/a-shenfen-fancha/a07-wujian-waimao-fancha/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-088) | A Treasure in Disguise<br>`wujian-waimao-fancha`<br>目录 `a07-wujian-waimao-fancha` | 安排短剧桥段时，想借识货者揭示旧物的真实价值。 | /wujian-waimao-fancha 义卖上有人用缺角木版垫桌脚，写印刷师傅怎样拿旧年画对出原版。 |
| [施恩遇贵人](skills/400-duanju-shuangdian/a-shenfen-fancha/a08-shien-yu-guiren/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-089) | Kindness Repaid<br>`shien-yu-guiren`<br>目录 `a08-shien-yu-guiren` | 安排短剧桥段时，想让有代价的善举在身份揭晓后得到回报。 | /shien-yu-guiren 送餐员耽误送单陪老人找戏班，写到他后来借排练场时才认出班主。 |
| [越级反杀・绝境翻盘](skills/400-duanju-shuangdian/b-shili-nianya/b01-yueji-fansha/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-090) | An Underdog’s Comeback<br>`yueji-fansha`<br>目录 `b01-yueji-fansha` | 安排短剧桥段时，想铺垫弱者越级翻盘的底牌。 | /yueji-fansha 学徒在幻境擂台只能留下自己的影子，先写一次小失败再让同一条规则帮他守旗。 |
| [破兵胜神兵](skills/400-duanju-shuangdian/b-shili-nianya/b02-po-bingqi-sheng-shenbing/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-091) | Humble Gear Beats a Legendary Weapon<br>`po-bingqi-sheng-shenbing`<br>目录 `b02-po-bingqi-sheng-shenbing` | 用普通装备胜出反转神兵优势。 | /po-bingqi-sheng-shenbing 试剑大会比的是隔空击铃，让学徒靠旧竹枝的节奏胜过少主的名剑。 |
| [大招无冷却](skills/400-duanju-shuangdian/b-shili-nianya/b03-dazhao-wu-lengque/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-092) | A Special Move with No Cooldown<br>`dazhao-wu-lengque`<br>目录 `b03-dazhao-wu-lengque` | 安排短剧桥段时，想利用技能冷却预判制造反转。 | /dazhao-wu-lengque 传送门开一次要等三刻，用计时牌和两次亮起的短程门写出接力赛反转。 |
| [虚张声势](skills/400-duanju-shuangdian/b-shili-nianya/b04-xuzhang-shengshi/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-093) | Winning with a Bluff<br>`xuzhang-shengshi`<br>目录 `b04-xuzhang-shengshi` | 用可信的假象扭转弱势局面。 | /xuzhang-shengshi 新人误拿冠军的封棋签，写对手主动求和时他差点露馅的那一拍。 |
| [金手指与资源碾压](skills/400-duanju-shuangdian/b-shili-nianya/b05-jinzhishou-ziyuan/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-094) | An Overwhelming Resource Advantage<br>`jinzhishou-ziyuan`<br>目录 `b05-jinzhishou-ziyuan` | 安排短剧桥段时，想给特殊资源设代价并展示优势。 | /jinzhishou-ziyuan 每救活一粒珍稀种子就得舍掉一季收成，写花店主把幼苗送给邻居的那场戏。 |
| [配角烘托](skills/400-duanju-shuangdian/b-shili-nianya/b06-peijue-hongtuo/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-095) | Power Revealed by Supporting Characters<br>`peijue-hongtuo`<br>目录 `b06-peijue-hongtuo` | 用配角的预判和行动烘托主角实力。 | /peijue-hongtuo 老琴师应聘时没碰琴，用学徒押注、评委认指法和学生演奏写出他的分量。 |
| [举重若轻](skills/400-duanju-shuangdian/b-shili-nianya/b07-juzhong-ruoqing/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-096) | Making the Impossible Look Easy<br>`juzhong-ruoqing`<br>目录 `b07-juzhong-ruoqing` | 用相同难题对照高手的举重若轻。 | /juzhong-ruoqing 合唱总慢半拍，先写两次纠错失败，再让老伴奏挪开挡住指挥手势的谱架。 |
| [家族嘲讽反打脸](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c01-jiazufan-dalian/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-097) | Turning the Tables on a Mocking Family<br>`jiazufan-dalian`<br>目录 `c01-jiazufan-dalian` | 安排短剧桥段时，想让受家族轻视的人当众拿回选择权。 | /jiazufan-dalian 叔伯笑女主离家学徒没出息，写买家认出她的手艺后等她决定接不接单的场面。 |
| [嚣张转谄媚](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c02-xiaozhang-zhuan-xianmei/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-098) | From Arrogance to Flattery<br>`xiaozhang-zhuan-xianmei`<br>目录 `c02-xiaozhang-zhuan-xianmei` | 安排短剧桥段时，想写出同一人从嚣张到讨好的变脸。 | /xiaozhang-zhuan-xianmei 经纪人刚把老人赶下椅子就认出她是终审，替他写半句改口让座的话。 |
| [炫富炫技被碾压](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c03-xuanfu-bei-nianya/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-099) | When Showing Off Backfires<br>`xuanfu-bei-nianya`<br>目录 `c03-xuanfu-bei-nianya` | 安排短剧桥段时，想在同一标准下反转炫耀者的优势。 | /xuanfu-bei-nianya 买家拿稀有唱片嘲笑修音师，让修音师用整套母盘的编号回应。 |
| [借势装 X 自取其辱](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c04-jie-shizhuang-bi/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-100) | Borrowed Status Exposed<br>`jie-shizhuang-bi`<br>目录 `c04-jie-shizhuang-bi` | 安排短剧桥段时，想让真正的拥有者拆穿借名炫耀。 | /jie-shizhuang-bi 画展租客冒充策展人叫人撤画，写一处开幕前才改过的细节让他当众露馅。 |
| [无心之举引风波](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c05-wuxin-zhi-ju-re-bo/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-101) | An Innocent Act Sparks a Stir<br>`wuxin-zhi-ju-re-bo`<br>目录 `c05-wuxin-zhi-ju-re-bo` | 安排短剧桥段时，想让无心之举经连续误读引发风波。 | /wuxin-zhi-ju-re-bo 女主怕泼湿校舍模型才挪杯子，写三个人怎样误读这个动作，竟让座谈会改了议程。 |
| [功劳被抢真相大白](skills/400-duanju-shuangdian/c-dalian-fanzhuan/c06-gonglao-bei-qiang/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-102) | Stolen Credit Restored<br>`gonglao-bei-qiang`<br>目录 `c06-gonglao-bei-qiang` | 安排短剧桥段时，想让抢功者先得势再由证据归还功劳。 | /gonglao-bei-qiang 领班冒领修复录音的功劳，让助理在颁奖返听时靠一段底噪拿回署名。 |
| [迪化流](skills/400-duanju-shuangdian/d-xushi-shoufa/d01-dihua-liu/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-103) | Others Read Too Much into It<br>`dihua-liu`<br>目录 `d01-dihua-liu` | 安排短剧桥段时，想让配角层层脑补主角的普通举动。 | /dihua-liu 新人盯着棋盘只想捡饭粒，给老棋手写三次越来越离谱的内心推断。 |
| [曝光流](skills/400-duanju-shuangdian/d-xushi-shoufa/d02-puguang-liu/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-104) | A Hidden Deed Comes to Light<br>`puguang-liu`<br>目录 `d02-puguang-liu` | 用事后曝光放大低调行动的结果。 | /puguang-liu 志愿者默默补齐旧戏曲录音，写听众怎样从重播片尾的小字认出她。 |
| [信息差](skills/400-duanju-shuangdian/d-xushi-shoufa/d03-xinxi-cha/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-105) | The Information Gap<br>`xinxi-cha`<br>目录 `d03-xinxi-cha` | 安排短剧桥段时，想分配角色与观众掌握的信息来制造反转。 | /xinxi-cha 观众先看见错户转账被退回，写收据在会上出现时房东和剧团长谁先改口。 |
| [系统加持伪装实力](skills/400-duanju-shuangdian/d-xushi-shoufa/d04-xitong-weizhuang/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-106) | A System That Masks True Strength<br>`xitong-weizhuang`<br>目录 `d04-xitong-weizhuang` | 安排短剧桥段时，想给系统伪装安排时限和真实底牌。 | /xitong-weizhuang 学徒只能假扮宗师十息，写他在伪装消失前靠唯一会的定音术通过考核。 |
| [剧本爽点缺失校验](skills/400-duanju-shuangdian/meta-shuangdian-jiaoyan/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-06.md#run-107) | Payoff Audit<br>`shuangdian-jiaoyan`<br>目录 `meta-shuangdian-jiaoyan` | 安排短剧桥段时，想逐场校验爽点分布、密度与合理性。 | /shuangdian-jiaoyan 女主连亮两次证书就被任命院长，指出重复的爽点和任命前缺的一场铺垫。 |

<a id="usage-journey"></a>

## 西游人物

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [二郎神](skills/XiYouJiSkills/erlangshen/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-108) | Erlang Shen<br>`erlangshen` | 要试演二郎神在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /erlangshen 悟空来请杨戬辨真假灵鸟，写四轮新对白，让旧对手的打趣收在一声兄弟上。 |
| [观音菩萨](skills/XiYouJiSkills/guanyin/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-109) | Guanyin<br>`guanyin` | 要试演观音菩萨在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /guanyin 小徒丢了乡民的包袱想逃，用三句新台词安抚他并带他回去担责。 |
| [红孩儿](skills/XiYouJiSkills/honghaier/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-110) | Red Boy<br>`honghaier` | 要试演红孩儿在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /honghaier 同听「有人要见你」，给火云洞称王和做善财童子时的红孩儿各写两句回应。 |
| [托塔李天王](skills/XiYouJiSkills/litianwang/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-111) | Pagoda-Bearing Heavenly King Li<br>`litianwang` | 要试演托塔李天王在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /litianwang 哪吒抢着应天庭军令，用李天王点名时的一次称呼变化写出公事里的父子情。 |
| [哪吒三太子](skills/XiYouJiSkills/nezha/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-112) | Nezha, the Third Prince<br>`nezha` | 要试演哪吒三太子在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nezha 李天王宣旨要哪吒留下守候，写三句接话让少年从抢着请缨到收住话头领命。 |
| [牛魔王](skills/XiYouJiSkills/niumowang/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-113) | Bull Demon King<br>`niumowang` | 要试演牛魔王在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /niumowang 悟空酒斟满才提借芭蕉扇，写四句由热转冷的新台词，收在牛魔王扣杯的动作上。 |
| [如来佛祖](skills/XiYouJiSkills/rulai/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-114) | Tathagata Buddha<br>`rulai` | 要试演如来佛祖在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /rulai 两名取经人争头功，让如来一句问起途中被落下的人，再作裁断。 |
| [沙僧](skills/XiYouJiSkills/shaseng/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-115) | Sha Wujing<br>`shaseng` | 要试演沙僧在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /shaseng 雨后渡口停船，给沙僧写两句分别接住八戒和师父的话，收在他安置经箱的动作上。 |
| [太白金星](skills/XiYouJiSkills/taibai/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-116) | Taibai Jinxing<br>`taibai` | 要试演太白金星在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /taibai 悟空嫌赴宴座次低，替太白金星写一句私下劝话和一句席前圆场。 |
| [唐僧](skills/XiYouJiSkills/tangseng/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-117) | Tang Sanzang<br>`tangseng` | 要试演唐僧在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /tangseng 村人只收肯付钱的客人，写三轮借宿对白，让唐僧止住悟空并提出做工换宿。 |
| [铁扇公主](skills/XiYouJiSkills/tieshangongzhu/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-118) | Princess Iron Fan<br>`tieshangongzhu` | 要试演铁扇公主在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /tieshangongzhu 悟空来借扇，给铁扇公主写三句称呼渐冷的回应，到问过红孩儿才拒借。 |
| [孙悟空](skills/XiYouJiSkills/wukong/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-119) | Sun Wukong<br>`wukong` | 要试演孙悟空在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /wukong 客栈挂着昨夜在别处见过的匾，给悟空写四句从识破破绽到安排照看师父的台词。 |
| [玉皇大帝](skills/XiYouJiSkills/yuhuang/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-120) | Jade Emperor<br>`yuhuang` | 要试演玉皇大帝在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /yuhuang 两位星官为同一场迟雨各执一词，拟一道五句短旨交代谁查时辰、何时回奏。 |
| [猪八戒](skills/XiYouJiSkills/zhubajie/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-121) | Zhu Bajie<br>`zhubajie` | 要试演猪八戒在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /zhubajie 经箱落在泥路上，写八戒边算耽误多久吃饭边把担子挑上肩的独白。 |

<a id="usage-characters"></a>

## 动画人物

按角色名查找。这里的动画人物卡和上一组的《西游记》原著口吻卡各有独立正文。

| 中文名称 | 英文名称 | 什么时候用 | 可复制提示词 |
| --- | --- | --- | --- |
| [赤木刚宪](skills/animation-character-skills/akagi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-122) | Takenori Akagi<br>`akagi-skill` | 要试演赤木刚宪在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /akagi-skill 暂停时球队落后两分，让赤木松开攥紧的毛巾，认下漏抢的篮板再提醒队友补位。 |
| [安室透](skills/animation-character-skills/amuro-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-123) | Toru Amuro<br>`amuro-skill` | 要试演安室透在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /amuro-skill 咖啡店客人用另一个名字喊安室，在他端稳杯碟问要不要糖时写两处停顿。 |
| [哆啦A梦](skills/animation-character-skills/doraemon-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-124) | Doraemon<br>`doraemon-skill` | 要试演哆啦A梦在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /doraemon-skill 大雄借口袋送忘带的作业，写三拍道具惹出的意外，把向老师解释的机会留给他。 |
| [沸羊羊](skills/animation-character-skills/feiyangyang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-125) | Boiling Sheep<br>`feiyangyang-skill` | 要试演沸羊羊在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /feiyangyang-skill 沸羊羊抢着多跑一棒却被当成抢风头，写到他忍住争辩蹲下替伙伴系鞋带。 |
| [杰诺斯](skills/animation-character-skills/genos-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-126) | Genos<br>`genos-skill` | 要试演杰诺斯在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /genos-skill 杰诺斯撞坏抢购用的菜篮，写他郑重复盘三条教训时师父递来布袋的笑点。 |
| [坂田银时](skills/animation-character-skills/gintoki-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-127) | Gintoki Sakata<br>`gintoki-skill` | 要试演坂田银时在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /gintoki-skill 万事屋停电了，给银时一句自嘲，掩住他把最后一支蜡烛递给委托人的关心。 |
| [五条悟](skills/animation-character-skills/gojo-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-128) | Satoru Gojo<br>`gojo-skill` | 要试演五条悟在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /gojo-skill 训练课上学生等老师报答案，给五条悟两句玩笑，让他顺势把讲台让出来。 |
| [光头强](skills/animation-character-skills/guangtouqiang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-129) | Logger Vick<br>`guangtouqiang-skill` | 要试演光头强在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /guangtouqiang-skill 光头强第一天带团就被风吹跑指路牌，画成四格让森林伙伴排队替他指路。 |
| [灰原哀](skills/animation-character-skills/haibara-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-130) | Ai Haibara<br>`haibara-skill` | 要试演灰原哀在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /haibara-skill 灰原哀被当小孩赶下展台，写她怎样点出标签贴反又给讲解员留个台阶。 |
| [红太狼](skills/animation-character-skills/hongtailang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-131) | Red Wolf<br>`hongtailang-skill` | 要试演红太狼在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /hongtailang-skill 狼堡晚餐准点端来空盘，用红太狼扣上又揭开的平底锅写一段餐桌交锋。 |
| [灰太狼](skills/animation-character-skills/huitailang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-132) | Grey Wolf<br>`huitailang-skill` | 要试演灰太狼在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huitailang-skill 灰太狼每修一次早餐机就多加一个功能，写三次试用让早饭越做越慢。 |
| [二娃](skills/animation-character-skills/huluwa-erwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-133) | Second Calabash Brother<br>`huluwa-erwa-skill` | 要试演二娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-erwa-skill 二娃在山谷听见风筝铃却看不见线，用三个镜头写他借兄弟指的位置报准方位。 |
| [六娃](skills/animation-character-skills/huluwa-liuwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-134) | Sixth Calabash Brother<br>`huluwa-liuwa-skill` | 要试演六娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-liuwa-skill 隐身的六娃排队领点心，写伙伴看见盘子自己移动时他怎样从忍笑到认领。 |
| [七娃](skills/animation-character-skills/huluwa-qiwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-135) | Seventh Calabash Brother<br>`huluwa-qiwa-skill` | 要试演七娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-qiwa-skill 七娃把庆典彩带当怪物收进葫芦，用葫芦里传出的排练歌声逼他开口道歉。 |
| [三娃](skills/animation-character-skills/huluwa-sanwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-136) | Third Calabash Brother<br>`huluwa-sanwa-skill` | 要试演三娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-sanwa-skill 彩排时人人都把忘掉的词推给扮铜墙的三娃，写一个动作让他终于开口求搭档接词。 |
| [四娃](skills/animation-character-skills/huluwa-siwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-137) | Fourth Calabash Brother<br>`huluwa-siwa-skill` | 要试演四娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-siwa-skill 四娃点云灯却照亮满天云，用三个镜头写他从看见同伴眯眼到慢慢收光。 |
| [五娃](skills/animation-character-skills/huluwa-wuwa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-07.md#run-138) | Fifth Calabash Brother<br>`huluwa-wuwa-skill` | 要试演五娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwa-wuwa-skill 五娃替云朵补水，用鼓腮、憋喷嚏和吐出一滴水写一场无对白喜剧。 |
| [大娃](skills/animation-character-skills/huluwadawa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-139) | First Calabash Brother<br>`huluwadawa-skill` | 要试演大娃在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /huluwadawa-skill 大娃举起布景板挡住自己的视线，写他在台阶前停住、放低板子让弟弟指路的三拍戏。 |
| [胡图图](skills/animation-character-skills/hututu-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-140) | Hu Tutu<br>`hututu-skill` | 要试演胡图图在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /hututu-skill 图图问月亮怕不怕独自吃饭，写四轮亲子对白，收在他给加班的爸爸留碗上。 |
| [黑崎一护](skills/animation-character-skills/ichigo-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-141) | Ichigo Kurosaki<br>`ichigo-skill` | 要试演黑崎一护在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /ichigo-skill 伙伴上台前失声，写一护看见写字板后从抢着代说到站在旁边翻页的四个动作。 |
| [旗木卡卡西](skills/animation-character-skills/kakashi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-142) | Kakashi Hatake<br>`kakashi-skill` | 要试演旗木卡卡西在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /kakashi-skill 卡卡西迟到挨队员抱怨，给他一句慢悠悠的提问点出排练时漏听的错拍。 |
| [奇犽](skills/animation-character-skills/killua-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-143) | Killua Zoldyck<br>`killua-skill` | 要试演奇犽在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /killua-skill 两个少年第一次约好同游，写奇犽分出最后一颗糖又装作无所谓的动作。 |
| [懒羊羊](skills/animation-character-skills/lanyangyang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-144) | Lazy Sheep<br>`lanyangyang-skill` | 要试演懒羊羊在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /lanyangyang-skill 运动会收垫子时懒羊羊赖着没起，写四拍让软垫意外挡住滚来的球。 |
| [利威尔](skills/animation-character-skills/levi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-145) | Levi Ackerman<br>`levi-skill` | 要试演利威尔在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /levi-skill 撤展快赶不上末班车，用一声短命令和放下抹布的动作写利威尔先带走疲惫队员。 |
| [路飞](skills/animation-character-skills/luffy-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-146) | Monkey D. Luffy<br>`luffy-skill` | 要试演路飞在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /luffy-skill 船长想改航去新岛，给路飞一句听完伙伴的约定后把决定权交还对方的台词。 |
| [小丸子](skills/animation-character-skills/maruko-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-147) | Chibi Maruko-chan<br>`maruko-skill` | 要试演小丸子在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /maruko-skill 小丸子偷懒买酱油时看见爷爷等的小花开了，写她怎样把爷爷带下楼。 |
| [美羊羊](skills/animation-character-skills/meiyangyang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-148) | Pretty Sheep<br>`meiyangyang-skill` | 要试演美羊羊在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /meiyangyang-skill 闺蜜压扁了花环，写美羊羊嘴上说没事、理花瓣时却露出小脾气的四轮对白。 |
| [绿谷出久](skills/animation-character-skills/midoriya-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-149) | Izuku Midoriya<br>`midoriya-skill` | 要试演绿谷出久在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /midoriya-skill 替补队员第一次带队，写绿谷翻着优点笔记含泪给每个队友分位置的独白。 |
| [御坂美琴](skills/animation-character-skills/misaka-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-150) | Mikoto Misaka<br>`misaka-skill` | 要试演御坂美琴在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /misaka-skill 学园祭停电，写四个镜头让御坂嘴上嫌麻烦却点亮低年级学生的摊位。 |
| [三井寿](skills/animation-character-skills/mitsui-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-151) | Hisashi Mitsui<br>`mitsui-skill` | 要试演三井寿在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /mitsui-skill 三井归队后第一次打到末节，用喘息、望向三分线和开口要球写出他对队友的信任。 |
| [宫城良田](skills/animation-character-skills/miyagi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-152) | Ryota Miyagi<br>`miyagi-skill` | 要试演宫城良田在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /miyagi-skill 对手没把矮个控卫放在眼里，用摸耳钉、启动和传球三个分镜写出宫城的速度。 |
| [娜美](skills/animation-character-skills/nami-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-153) | Nami<br>`nami-skill` | 要试演娜美在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nami-skill 娜美坚持绕航，写伙伴翻过她记港口费的小账本才看见避风路线的喜剧场面。 |
| [漩涡鸣人](skills/animation-character-skills/naruto-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-154) | Naruto Uzumaki<br>`naruto-skill` | 要试演漩涡鸣人在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /naruto-skill 同伴落选后不肯回排练厅，写鸣人邀他再练第一句的独白，给演员留一处破音。 |
| [哪吒](skills/animation-character-skills/nezha-mo-tong-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-155) | Nezha<br>`nezha-mo-tong-skill` | 要试演哪吒在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nezha-mo-tong-skill 镇民怪哪吒弄坏灯架，设计一个童身使神力的小动作，让他接过替他赔礼的母亲手里的活。 |
| [灶门祢豆子](skills/animation-character-skills/nezuko-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-156) | Nezuko Kamado<br>`nezuko-skill` | 要试演灶门祢豆子在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nezuko-skill 哥哥以为祢豆子怕人群，用目光和三步无对白动作写出她其实想替走失的孩子挡雨。 |
| [野比大雄](skills/animation-character-skills/nobita-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-157) | Nobita Nobi<br>`nobita-skill` | 要试演野比大雄在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nobita-skill 替人道歉的闹钟越抢话越糟，写三拍让大雄亲手按停它并向朋友认错。 |
| [暖羊羊](skills/animation-character-skills/nuanyangyang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-158) | Warm Sheep<br>`nuanyangyang-skill` | 要试演暖羊羊在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /nuanyangyang-skill 合唱队两人都怕站后排家人看不见，写暖羊羊听完各自顾虑后怎样换站位。 |
| [流川枫](skills/animation-character-skills/rukawa-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-159) | Kaede Rukawa<br>`rukawa-skill` | 要试演流川枫在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /rukawa-skill 最后一次进攻原该由流川单打，用四个无旁白镜头写出他看见空位队友后的传球。 |
| [琦玉](skills/animation-character-skills/saitama-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-160) | Saitama<br>`saitama-skill` | 要试演琦玉在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /saitama-skill 琦玉领完力量奖只惦记快过期的优惠券，用颁奖台和收银台切出一段喜剧。 |
| [樱木花道](skills/animation-character-skills/sakuragi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-161) | Hanamichi Sakuragi<br>`sakuragi-skill` | 要试演樱木花道在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /sakuragi-skill 樱木练篮板时接连失误还夸自己，用四镜蒙太奇写到他第一次默默卡准位置。 |
| [宇智波佐助](skills/animation-character-skills/sasuke-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-162) | Sasuke Uchiha<br>`sasuke-skill` | 要试演宇智波佐助在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /sasuke-skill 佐助收到失联兄长的旧护额，用三个折叠动作露出他嘴硬不肯承认的牵挂。 |
| [沙僧](skills/animation-character-skills/shaseng-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-163) | Sha Wujing<br>`shaseng-skill` | 要试演沙僧在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /shaseng-skill 两位师兄争谁多背行李，写沙僧把空筐倒扣成饭桌后用一句话把争论变成分饭。 |
| [野原新之助](skills/animation-character-skills/shinchan-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-164) | Shinnosuke Nohara<br>`shinchan-skill` | 要试演野原新之助在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /shinchan-skill 新之助一本正经替吸尘器请假，写四轮对白让妈妈听懂孩子想让谁歇一歇。 |
| [唐僧](skills/animation-character-skills/tangseng-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-165) | Tang Sanzang<br>`tangseng-skill` | 要试演唐僧在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /tangseng-skill 徒弟偷拿最后一块饼给路边孩子，写唐僧从唠叨分食规矩到把自己的饼也包进去。 |
| [灶门炭治郎](skills/animation-character-skills/tanjiro-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-166) | Tanjiro Kamado<br>`tanjiro-skill` | 要试演灶门炭治郎在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /tanjiro-skill 炭治郎循焦糖味找到偷点心的人，写三句对白，让他听出对方哭过仍坚持要回点心。 |
| [月野兔](skills/animation-character-skills/tsukino-usagi-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-167) | Usagi Tsukino<br>`tsukino-usagi-skill` | 要试演月野兔在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /tsukino-usagi-skill 好友开演前丢了发饰，写月野兔哭着变身找过一圈后答应留下看演出的那句话。 |
| [小灰灰](skills/animation-character-skills/xiaohuihui-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-168) | Little Grey Wolf<br>`xiaohuihui-skill` | 要试演小灰灰在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /xiaohuihui-skill 狼和羊争野餐桌摆哪边，给搬来两条长凳的小灰灰一句能让双方停下来的童言。 |
| [熊大](skills/animation-character-skills/xiongda-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-169) | Briar<br>`xiongda-skill` | 要试演熊大在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /xiongda-skill 光头强和熊二争招牌该朝哪边，写四句对白让熊大请两人从游客来的方向走一遍。 |
| [熊二](skills/animation-character-skills/xionger-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-170) | Bramble<br>`xionger-skill` | 要试演熊二在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /xionger-skill 野餐路标丢了，写三拍让熊二循蜂蜜香翻开倒扣的篮子，无意中找回路标。 |
| [喜羊羊](skills/animation-character-skills/xiyangyang-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-171) | Pleasant Goat<br>`xiyangyang-skill` | 要试演喜羊羊在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /xiyangyang-skill 羊村灯谜赛卡在最后一题，用一个看得见的动作让喜羊羊拼起伙伴各猜中的半句。 |
| [猪八戒](skills/animation-character-skills/zhubajie-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-172) | Zhu Bajie<br>`zhubajie-skill` | 要试演猪八戒在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /zhubajie-skill 八戒一路嫌果子小，写三个动作让他嘴上嘀咕却把最大的换给空手的小师弟。 |
| [索隆](skills/animation-character-skills/zoro-skill/SKILL.md)<br>[已交付 · 历史答卷](skills/试跑记录/2026-11-26/group-08.md#run-173) | Roronoa Zoro<br>`zoro-skill` | 要试演索隆在这场戏里的反应，决定角色先做哪个动作、哪句话随后出口。 | /zoro-skill 索隆带队绕回原码头，写三拍让他嘴硬过后扛起行李，把地图交给别人。 |

<a id="usage-resources"></a>

## 配套资料和查询命令

查技能描述可在仓库根运行 `python3 tools/skill_catalog.py`。输出每行是目录路径和用途。找梗、群策和 swarm 单列在[调度用法](#usage-dispatch)。核对《我爱我家》某一拍的转写，可运行 `python3 skills/liang-zuo-perspective/scripts/find_scene.py --episode 65 --at 00:04:40`。

| 中文名称 | 英文名称 | 什么时候查 | 从哪里开始 |
| --- | --- | --- | --- |
| 桥段检索库 | Trope Library<br>`trope-library` | 已有一场戏，想跨《我爱我家》《摩登家庭》《成长的烦恼》找接法 | [编剧调梗示范](skills/trope-library/编剧调梗.md)。在仓库根目录运行 `python3 skills/trope-library/trope-library.py all 误会 帮忙 --limit 8`。 |
| 动画编剧研究 | Animation Writing Research<br>`animation-writing-research` | 按作品找案例或制作稿 | [研究导航](skills/animation-writing-research/README.md)、[300 项片单](skills/animation-writing-research/catalog-300.md)、[40 项喜剧](skills/animation-writing-research/comedy-40.md)。 |
| 动画叙事技法研究 | Animation Craft Studies<br>`animation-craft-studies` | 比较四段结构、皮克斯和《南方公园》的叙事方法 | [起承转合研究](skills/animation-craft-studies/kishotenketsu-narratological-algorithms.md)、[皮克斯](skills/animation-craft-studies/pixar-narratological-algorithms.md)、[《南方公园》](skills/animation-craft-studies/south-park-narratological-algorithms.md)。 |
| 动画镜头拉片 | Animation Shot Studies<br>`animation-shot-studies` | 要把动作写进镜头，想找动画拉片参考 | [8 篇案例目录](skills/animation-shot-studies/)，可从[《千与千寻》](skills/animation-shot-studies/03_spirited_away.md)进入。 |
| 哆啦A梦分集参考 | Doraemon Episode Reference<br>`doraemon-episode-reference` | 对照《哆啦A梦》的原集故事简介 | [朝日电视台故事页本地存档](skills/doraemon-episode-reference/0923.html)，收有「でんしょひこうき」和「スネ夫ゆうかい事件」。 |
| 漫剧分镜案例库 | ManjuForge Case Studies<br>`manjuforge-cases` | 为中式动画场景找分镜对照 | [《中国奇谭》](skills/manjuforge-cases/10_china_tales.md)、[《哪吒2》](skills/manjuforge-cases/11_naza2.md)。 |
| 编剧术语与工作流 | Screenwriting Terms and Workflow<br>`sw-workflow` | 和合作者核对节拍表、出幕等术语的中英文 | [编剧术语对照表](skills/sw-workflow/terms.md)。 |
