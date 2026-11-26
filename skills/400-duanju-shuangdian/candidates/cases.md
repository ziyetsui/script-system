# Candidates — Case Extractor

> 识别结果: 文档中给出的桥段实例 / 原型（作为各 skill 的 A1 素材）
> 提取自: 《400 个爆款短剧剧本爽点》内容总结

```yaml
- id: c01
  title: 大人物俯首
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "外界敬畏的强人、大人物，见到主角毕恭毕敬、俯首"
  summary: |
    反差信号：权威人物对主角的态度与主角公开身份不符。
    用于铺垫"主角真实身份极高"。
  bound_to:
    - "f03 扮猪吃虎反差结构"
    - "a01 大人物俯首"
  outcome: 外部视角建立主角神秘感，为揭晓蓄力

- id: c02
  title: 贵宾被刁难
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "贵宾身份的主角被门卫、普通人刁难，后续身份揭晓打脸"
  summary: |
    低身份者对高身份主角刁难，构成"有眼不识泰山"经典桥段。
    刁难越具体、揭晓越当众，打脸越响。
  bound_to:
    - "a02 微服被刁难・有眼不识泰山"
  outcome: 揭晓后门卫/路人惊惧，观众获得情绪满足

- id: c03
  title: 多重身份叠加
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "同时拥有多个赫赫有名的代号，旁人却不知道都是主角一人"
  summary: |
    主角 = 多个大佬身份的集合，信息差最大化。
    每个身份都是独立的反差引爆点。
  bound_to:
    - "a03 多重马甲"
  outcome: 层层揭晓，爽感叠加

- id: c04
  title: 幕后大佬
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "幕后大佬，培养一众大人物却被世人嘲笑"
  summary: |
    主角培养的大人物们功成名就，世人却嘲笑主角无用；
    反差在"被培养者俯首/感恩"时引爆。
  bound_to:
    - "a04 幕后大佬"
  outcome: 培养者地位揭晓 → 世人震惊

- id: c05
  title: 死后复活震撼全场
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "死后复活，震撼全场"
  summary: |
    主角以"已死"之名被低估，复活登场时全场震动。
    属"绝境/死亡 → 回归"类爽点，并入 b01 越级反杀・绝境翻盘。
  bound_to:
    - "b01 越级反杀・绝境翻盘"
  outcome: 回归反差最大化

- id: c06
  title: 身边人暗藏实力（扫地僧式）
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "扫地、捡垃圾、快递员这类不起眼配角，实际是顶级大佬"
  summary: |
    不起眼职业 + 顶级实力 = 扫地僧式角色。
    常用于主角的"隐藏守护者"或主角本人的伪装。
  bound_to:
    - "a06 扫地僧式角色"
  outcome: 关键时刻出手，全场震惊

- id: c07
  title: 全世界知道主角厉害，唯独亲友不知情
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "全世界知道主角厉害，唯独身边亲友不知情"
  summary: |
    信息差主体是"亲友"：他们基于日常印象低估主角，
    揭晓时亲缘关系制造更强烈的情绪冲击。
  bound_to:
    - "a05 亲友不知情"
  outcome: 亲情 + 反差双重情绪

- id: c08
  title: 破旧物品实为珍宝
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "主角普通破旧物品，在别人眼中是绝世珍宝"
  summary: |
    物件反差：主角随手之物在识货者眼中价值连城。
    与 b02 破兵胜神兵同源（器物层面）。
  bound_to:
    - "a07 物件与外貌反差"
    - "b02 破兵胜神兵"
  outcome: 识货者惊骇，不识货者自打脸

- id: c09
  title: 外貌反差
  type: case
  source_chapter: 一、身份反差・隐藏大佬
  source_quote: |
    "众人以为主角样貌不堪，实际容貌出众"
  summary: |
    认知 vs 实际的外貌落差，揭晓时制造惊艳感。
  bound_to:
    - "a07 物件与外貌反差"
  outcome: 惊艳反转

- id: c10
  title: 迪化流脑补
  type: case
  source_chapter: 一、身份反差（衍生桥段）
  source_quote: |
    "迪化流：配角根据主角普通言行，疯狂脑补高大上动机"
  summary: |
    主角无心之举被配角解读为深谋远虑，笑点与敬畏并存。
  bound_to:
    - "d01 迪化流"
  outcome: 喜剧 + 敬畏双效果

- id: c11
  title: 曝光流
  type: case
  source_chapter: 一、身份反差（衍生桥段）
  source_quote: |
    "曝光流：主角姿态放低，却做出轰动大事"
  summary: |
    低姿态 + 高成就的对比本身即爽点，无需刻意打脸。
  bound_to:
    - "d02 曝光流"
  outcome: 无声碾压式爽感

- id: c12
  title: 有眼不识泰山 / 微服私访误会身份
  type: case
  source_chapter: 一、身份反差（衍生桥段）
  source_quote: |
    "有眼不识泰山、微服私访误会身份、系统加持伪装实力"
  summary: |
    三个变体：不识泰山（认不出真神）、微服误会（认错身份）、
    系统加持（借系统伪装）。前两者并入 a02，后者独立为 d04。
  bound_to:
    - "a02 微服被刁难"
    - "d04 系统加持伪装实力"
  outcome: 揭晓时刻统一引爆

- id: c13
  title: 越级杀敌 / 同级无敌 / 绝境极限反杀
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "越级杀敌、同级无敌；绝境极限反杀"
  summary: |
    实力预期差的三种打法：跨等级取胜、同阶无敌、绝境翻盘。
  bound_to:
    - "b01 越级反杀・绝境翻盘"
  outcome: 超出预期的胜利

- id: c14
  title: 破兵器战胜神兵
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "破兵器战胜神兵"
  summary: |
    装备劣势 + 实力/技巧优势 = 器物层面的大反差。
  bound_to:
    - "b02 破兵胜神兵"
  outcome: 对手对装备自信崩塌

- id: c15
  title: 大招无冷却，打破反派预判
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "大招无冷却，打破反派预判"
  summary: |
    反派按常规冷却时间预判，主角技能机制碾压其算计。
  bound_to:
    - "b03 大招无冷却"
  outcome: 预判失效 → 心理崩溃

- id: c16
  title: 虚张声势误导对手高估
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "虚张声势误导对手高估自己实力"
  summary: |
    反向操作：让对手高估主角，主动退让/放弃。
  bound_to:
    - "b04 虚张声势"
  outcome: 不战而屈人之兵

- id: c17
  title: 天赋功法神器靠山
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "天赋、功法、神器、高人靠山；失传、传说级的能力宝物"
  summary: |
    金手指四大来源：天赋、功法、神器、靠山；传说级资源更佳。
  bound_to:
    - "b05 金手指与资源碾压"
  outcome: 起点即终点

- id: c18
  title: 珍贵宝物随意赠送
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "珍贵宝物主角如同地摊货随意赠送"
  summary: |
    主角对宝物的态度本身即身份信号，赠予即碾压。
  bound_to:
    - "b05 金手指与资源碾压"
  outcome: 收礼者震惊

- id: c19
  title: 配角烘托完胜
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "所有人预判主角必败，主角完胜；反派引以为傲的靠山，实际是主角手下；徒弟狂妄，师傅却敬畏主角；主角粉丝、手下主动出手替主角摆平麻烦。"
  summary: |
    用配角预期、靠山关系、师徒反差、粉丝行为四路烘托主角实力。
  bound_to:
    - "b06 配角烘托"
  outcome: 多方视角坐实碾压

- id: c20
  title: 别人历尽千辛，主角轻松搞定
  type: case
  source_chapter: 二、实力碾压・越级反杀
  source_quote: |
    "别人历尽千辛完成的难事，主角轻松搞定；善待手下收获敬畏与拥护。"
  summary: |
    效率反差 + 驭下反差，双路爽点。
  bound_to:
    - "b07 举重若轻"
  outcome: 轻松感 + 忠诚度

- id: c21
  title: 家族内部嘲讽反打脸
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "家族内部嘲讽贬低主角，主角凭借身份实力完成反打脸"
  summary: |
    家族内部羞辱 → 公开场合反打脸。
  bound_to:
    - "c01 家族嘲讽反打脸"
  outcome: 家族颜面扫地

- id: c22
  title: 嚣张找上门转谄媚
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "配角气焰嚣张找上门，得知主角实力之后立刻谄媚求饶"
  summary: |
    态度 180° 反转：嚣张 → 得知真相 → 求饶。
  bound_to:
    - "c02 嚣张转谄媚"
  outcome: 前后对比即爽点

- id: c23
  title: 富家公子炫富被碾压 / 配角炫耀珍藏主角拿出更好的
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "富家公子哥炫富装 X 被主角碾压；配角炫耀珍藏物件，主角拿出更好的物品"
  summary: |
    比拼类反转：对方炫耀什么，主角拿出更强的同类。
  bound_to:
    - "c03 炫富炫技被碾压"
  outcome: 炫耀变成献丑

- id: c24
  title: 借不属于自己的资本装 X
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "反派借用不属于自己的资本装 X，自取其辱"
  summary: |
    装 X 建立在虚假资本上，戳穿时自取其辱。
  bound_to:
    - "c04 借势装 X 自取其辱"
  outcome: 虚假资本崩塌

- id: c25
  title: 无心之举被过度解读
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "主角无心之举，被配角过度解读，引发风波"
  summary: |
    主角无意的行为引发连锁风波（与迪化同源，但结果导向'风波'）。
  bound_to:
    - "c05 无心之举引风波"
    - "d01 迪化流"
  outcome: 主角被迫卷入，最终反转受益

- id: c26
  title: 他人抢夺主角功劳，真相大白
  type: case
  source_chapter: 三、打脸反转・当众处刑
  source_quote: |
    "他人抢夺主角功劳，后续真相大白"
  summary: |
    功劳被抢 → 隐忍 → 真相大白，抢功者身败名裂。
  bound_to:
    - "c06 功劳被抢真相大白"
  outcome: 迟到的正义更解气

- id: c27
  title: 弱点修复
  type: case
  source_chapter: 一、身份反差（配套情节）
  source_quote: |
    "配套情节：弱点修复"
  summary: |
    主角的短板被修复（废柴觉醒/体质改造），作为实力成长的配套弧线。
    并入 b05 金手指资源体系，不单独成 skill。
  bound_to:
    - "b05 金手指与资源碾压"
  outcome: 成长弧线 + 爽点

- id: c28
  title: 救人发现被救者出身豪门
  type: case
  source_chapter: 一、身份反差（配套情节）
  source_quote: |
    "配套情节：救人却发现被救者本身出身豪门"
  summary: |
    主角无意中施恩于隐藏身份者，后续获得意外回报。
  bound_to:
    - "a08 施恩遇贵人"
  outcome: 善有善报 + 身份反转

- id: c29
  title: 扫地僧（经典原型）
  type: case
  source_chapter: 四、通用创作要点
  source_quote: |
    "参考扫地僧、一拳超人等作品的叙事思路"
  summary: |
    金庸《天龙八部》扫地僧：藏经阁无名老僧，轻易化解绝顶高手冲突。
    是"不起眼角色 = 顶级实力"的叙事原型。
  bound_to:
    - "a06 扫地僧式角色"
  outcome: 原型级案例，供复用叙事思路

- id: c30
  title: 一拳超人（经典原型）
  type: case
  source_chapter: 四、通用创作要点
  source_quote: |
    "参考扫地僧、一拳超人等作品的叙事思路"
  summary: |
    《一拳超人》：绝对实力 + 不被认可的日常 = 反差与迪化的极致示范。
    是"实力碾压 + 迪化流"的叙事原型。
  bound_to:
    - "b01 越级反杀"
    - "d01 迪化流"
  outcome: 原型级案例，供复用叙事思路
```

## 自检

- [x] 每条案例都有 `bound_to`
- [x] 有原文引用
- [x] 有 outcome
- [x] 未筛选
