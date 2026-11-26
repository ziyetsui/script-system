# Candidates — Counter-Example Extractor

> 识别结果: 作者警告的失败模式 / 反例 / 陷阱
> 提取自: 《400 个爆款短剧剧本爽点》内容总结

```yaml
- id: ce01
  title: 无脑装 X
  type: counter-example
  source_chapter: 四、通用创作要点（风险提醒）
  source_quote: |
    "无脑装 X、强行降智容易引起读者反感"
  failure_mode: |
    主角毫无节制、毫无理由地炫耀/碾压，缺乏铺垫与代价，
    读者只感到油腻与尴尬，而非爽感。
  mechanism: |
    爽感需要"反差 + 铺垫 + 合理性"共同作用；
    去掉铺垫与代价，反差就退化为单纯的炫耀，触发读者反感。
  warning_signs:
    - 主角刚出场就无理由吊打所有人
    - 每个配角都毫无动机地跪舔主角
    - 主角碾压后没有剧情后果（无代价）
  bound_to:
    - "全部 A/B/C 类爽点 skill 的 B 段"
  tags: [counter-example, overreach, cringe]

- id: ce02
  title: 强行降智
  type: counter-example
  source_chapter: 四、通用创作要点（风险提醒）
  source_quote: |
    "无脑装 X、强行降智容易引起读者反感"
  failure_mode: |
    为了让主角打脸，把配角写成智商为负的工具人：
    明知主角身份仍无脑挑衅、明明可避免冲突偏要送人头。
  mechanism: |
    降智让反转失去'合理性'——读者觉得'这不可能发生'，
    情绪满足被'这太假了'的吐槽取代。
  warning_signs:
    - 配角在已经见识主角实力后仍反复挑衅
    - 全世界都在传主角的事迹，反派却一无所知且无理由
    - 配角的行为无法用其立场/性格解释
  bound_to:
    - "全部打脸类 skill（c01–c06）的 B 段"
    - "a02 微服被刁难"
  tags: [counter-example, dumbdown, credibility]

- id: ce03
  title: 爽点维度单一（只会打架打脸）
  type: counter-example
  source_chapter: 四、通用创作要点
  source_quote: |
    "爽点不只局限打架打脸，物质收获、地位提升、他人崇拜、感情收获，同样是有效爽点。"
  failure_mode: |
    整部剧本只有战斗和羞辱两种爽点，读者审美疲劳，
    且人物关系单一、缺乏可持续的叙事动力。
  mechanism: |
    单一维度的爽点收益递减；混合维度（物质/地位/崇拜/感情）
    才能维持读者的新鲜感与对主角的认同。
  warning_signs:
    - 连续多集只有'又赢了'和'又打脸了'
    - 主角除实力外没有其他可投入的属性
  bound_to:
    - "b07 举重若轻"
    - "meta-shuangdian-jiaoyan 爽点校验"
  tags: [counter-example, monotony, payoff-dimension]

- id: ce04
  title: 反差无节制堆砌
  type: counter-example
  source_chapter: 批判（BOOK_OVERVIEW 阶段 0）
  source_quote: |
    "假设'反差越大越爽'始终成立；实际上过度夸张的反差会滑向荒诞或尴尬。"
  failure_mode: |
    每集都塞入最大值反差，主角从扫地僧到宇宙至尊层层叠加，
    反差失去梯度，读者麻木。
  mechanism: |
    反差需要梯度与节奏：全剧最大的反差只能出现一次，
    提前透支会让后续所有反差失去效果。
  warning_signs:
    - 主角身份/实力层级在前期就拉到顶
    - 单集内出现 3 次以上'全场震惊'
  bound_to:
    - "全部 A 类 skill 的 B 段"
  tags: [counter-example, escalation, fatigue]

- id: ce05
  title: 把桥段当万能公式（套路流水线）
  type: counter-example
  source_chapter: 批判（BOOK_OVERVIEW 阶段 0）
  source_quote: |
    "真正让读者上头的不是套路本身，而是作者对情绪节奏、人物关系的把握；照搬清单只会写出千篇一律的工业糖精。"
  failure_mode: |
    机械套用桥段清单，不处理人物动机与情绪节奏，
    产出千篇一律、人物脸谱化的剧本。
  mechanism: |
    桥段是'结果'不是'原因'；脱离人物与情绪的桥段是空壳。
  warning_signs:
    - 所有配角都是为了被打脸而存在
    - 桥段之间没有因果链，只是流水账
  bound_to:
    - "meta-shuangdian-jiaoyan 爽点校验"
  tags: [counter-example, formulaic, character]
```

## 自检

- [x] 每条都有 failure_mode + mechanism
- [x] 有 warning_signs
- [x] 有 bound_to
- [x] 有原文引用
