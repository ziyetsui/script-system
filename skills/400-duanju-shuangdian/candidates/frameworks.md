# Candidates — Framework Extractor

> 识别结果: 思维模型 / 决策框架 / 推理方法
> 提取自: 《400 个爆款短剧剧本爽点》内容总结（源文本约 1100 字，单块直读）

```yaml
- id: f01
  title: 反差制造引擎
  type: framework
  source_chapter: 引言（底层逻辑）
  source_quote: |
    "核心底层逻辑是制造反差、信息差、反转，快速给读者情绪满足"
  summary: |
    所有爽点的底层共同结构：在"读者/配角以为 A"与"实际是 B"之间制造落差。
    反差越大、揭晓越突然、目击者越多，情绪满足越强。
    可作用维度：身份、实力、外貌、物件、信息掌握量。
  tags: [framework, contrast, emotional-payoff]

- id: f02
  title: 信息差冲突机
  type: framework
  source_chapter: 一、身份反差（配套情节）
  source_quote: |
    "利用信息差制造冲突（反派搬出靠山，殊不知靠山刚被主角击败）"
  summary: |
    让冲突双方掌握的信息不对称：反派按"旧信息"行动，
    读者知道"新信息"（靠山已败），等反派撞上新信息时反转产生。
    是反转/打脸类爽点的标准引擎，可独立成手法（见 d03）。
  tags: [framework, information-asymmetry, reversal]

- id: f03
  title: 扮猪吃虎反差结构
  type: framework
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "核心：主角实力/地位极高，但对外表现为小人物，旁人轻视、嘲讽，后续揭开反差制造爽感。"
  summary: |
    四段结构：①主角真实身份极高；②公开身份极低；③旁人基于公开身份轻视嘲讽；
    ④真实身份揭晓 → 打脸 + 震惊。是身份反差类的总框架，
    可作用于多重身份、幕后大佬、扫地僧角色等具体子套路。
  tags: [framework, identity-contrast, face-slap]

- id: f04
  title: 实力预期差框架
  type: framework
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "核心：主角硬实力超出对手预期，依靠战斗、能力碾压对手，收获胜利与敬畏。"
  summary: |
    核心变量是"对手对主角实力的预期"。制造预期差的方式：
    越级挑战、绝境反杀、破兵器胜神兵、大招无冷却、虚张声势。
    胜负本身不是爽点，'超出预期地赢'才是。
  tags: [framework, power-scaling, expectation-gap]

- id: f05
  title: 当众处刑结构
  type: framework
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "核心：配角炫耀、欺压、贬低主角，后续局势反转，配角颜面扫地。"
  summary: |
    反转必须有"观众"才有戏剧性：配角先公开羞辱/炫耀（建立公众预期），
    再在众人见证下反转。'当众'二字是核心变量——私下的反转不如当众反转爽。
  tags: [framework, public-reversal, face-slap]

- id: f06
  title: 脑补放大器（迪化机制）
  type: framework
  source_chapter: 一、身份反差（衍生桥段）
  source_quote: |
    "迪化流：配角根据主角普通言行，疯狂脑补高大上动机"
  summary: |
    主角的普通行为在配角脑内被解读为深不可测的布局。
    本质是'解读权'掌握在配角手里，主角越无辜，反差越强。
    与信息差配合可产生喜剧+敬畏双重效果。
  tags: [framework, misinterpretation, comedy]
```

## 自检

- [x] 每条都有原文根据
- [x] 都是可迁移的思考结构
- [x] 原文引用 ≤150 字
- [x] 未筛选，全部交阶段 1.5
