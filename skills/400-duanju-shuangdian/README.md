# 《400 个爆款短剧剧本爽点》Agent 技能包

> 把网文 / 短剧的爆款爽感套路蒸馏成 **26 个可执行的 Agent Skills**，
> 供 AI 在剧本创作中**生成桥段**与**校验爽点缺失**。

| | |
|---|---|
| **官网** | https://icoolkj.com |
| **作者** | daipeng |
| **邮箱** | icoolkj@163.com / 594047667@qq.com |
| **蒸馏方法** | cangjie-skill（RIA-TV++ 流水线） |
| **处理时间** | 2026-08-21 |

---

## 📖 这是什么

《400 个爆款短剧剧本爽点》是一份流传于网文 / 短剧圈的创作方法论汇编。它的核心洞察只有一句话：

> **一切爽感都是"落差"的产物** —— 对比、反差、信息差，三大底层机制，落成三大类桥段。

本仓库把这份汇编蒸馏为一组**原子化、可被 agent 在真实创作场景下调用**的 skills：

- 🎯 **生成**：需要某个爽点桥段时，直接调用对应 skill，按"可执行步骤"产出带铺垫、引爆、避坑的完整桥段。
- ✅ **校验**：剧本写完后，用元技能按 A/B/C/D 四类清单逐集打标，输出爽点分布 / 密度 / 多样性 / 雷区体检报告。

---

## 🗂 技能总览（26 个）

### A 类 — 身份反差・隐藏大佬（扮猪吃虎核心体系，8 个）

| Skill | 一句话 | 典型桥段 |
|---|---|---|
| `a01-darenwu-fushou` | 大人物俯首 | 权威者当众对主角毕恭毕敬，认证其隐藏地位 |
| `a02-weifu-bei-diaonan` | 微服被刁难・有眼不识泰山 | 贵宾被门卫刁难，身份揭晓当众打脸 |
| `a03-duochong-majia` | 多重马甲 | 主角同时是战神、医圣、财阀掌门…… |
| `a04-muhou-dalao` | 幕后大佬 | 培养大人物却被世人嘲笑，徒弟当众认主 |
| `a05-qinyou-buzhiqing` | 亲友不知情 | 全世界知道主角厉害，唯独家里不知道 |
| `a06-saodiseng-shijue` | 扫地僧式角色 | 捡垃圾的老头其实是隐退武道宗师 |
| `a07-wujian-waimao-fancha` | 物件与外貌反差 | 破碗是圣物、丑貌是伪装 |
| `a08-shien-yu-guiren` | 施恩遇贵人 | 随手救的老头是财阀掌门 |

### B 类 — 实力碾压・越级反杀（7 个）

| Skill | 一句话 | 典型桥段 |
|---|---|---|
| `b01-yueji-fansha` | 越级反杀・绝境翻盘 | 必败之局极限反杀（含死后复活变体） |
| `b02-po-bingqi-sheng-shenbing` | 破兵胜神兵 | 断刀打赢屠龙级神兵 |
| `b03-dazhao-wu-lengque` | 大招无冷却 | 反常规机制碾碎反派预判 |
| `b04-xuzhang-shengshi` | 虚张声势 | 不战而屈人之兵 |
| `b05-jinzhishou-ziyuan` | 金手指与资源碾压 | 宝物像地摊货随意赠送（含弱点修复） |
| `b06-peijue-hongtuo` | 配角烘托 | 反派靠山其实是主角手下 |
| `b07-juzhong-ruoqing` | 举重若轻 | 别人历尽千辛，主角轻松搞定 |

### C 类 — 打脸反转・当众处刑（6 个）

| Skill | 一句话 | 典型桥段 |
|---|---|---|
| `c01-jiazufan-dalian` | 家族嘲讽反打脸 | 族会上亮底牌，亲人颜面扫地 |
| `c02-xiaozhang-zhuan-xianmei` | 嚣张转谄媚 | 刚才狂得要命，现在跪地求饶 |
| `c03-xuanfu-bei-nianya` | 炫富炫技被碾压 | 炫耀变成献丑 |
| `c04-jie-shizhuang-bi` | 借势装 X 自取其辱 | 假资本被真主当场戳穿 |
| `c05-wuxin-zhi-ju-re-bo` | 无心之举引风波 | 一句话引发连锁风波 |
| `c06-gonglao-bei-qiang` | 功劳被抢真相大白 | 抢功者爬得越高摔得越重 |

### D 类 — 特殊叙事手法（4 个）

| Skill | 一句话 | 定位 |
|---|---|---|
| `d01-dihua-liu` | 迪化流 | 配角脑补主角高大上动机（喜剧 + 敬畏） |
| `d02-puguang-liu` | 曝光流 | 低姿态 + 大结果的无声碾压 |
| `d03-xinxi-cha` | 信息差 | **底层引擎**，所有反转类 skill 的依赖基座 |
| `d04-xitong-weizhuang` | 系统加持伪装实力 | 假面板，真底牌 |

### 🧰 元技能（1 个）

| Skill | 一句话 |
|---|---|
| `shuangdian-jiaoyan` | 剧本爽点缺失校验：逐集打标，输出分布 / 密度 / 雷区体检报告 |

---

## 🚀 快速开始

### 安装

把各分类目录下的 skill 文件夹复制到宿主 skills 目录：

```bash
# DeepSeek Harness（用户级，全局可用）
cp -r a-shenfen-fancha/* ~/.dsh/skills/
cp -r b-shili-nianya/* ~/.dsh/skills/
cp -r c-dalian-fanzhuan/* ~/.dsh/skills/
cp -r d-xushi-shoufa/* ~/.dsh/skills/
cp -r meta-shuangdian-jiaoyan ~/.dsh/skills/

# 或项目级
cp -r <skill-dir> <项目>/.dsh/skills/
# 其他宿主：~/.agents/skills/ · ~/.claude/skills/ · <项目>/.cursor/skills/
```

### 使用示例

**生成桥段**：

> "写一个桥段：主角微服去酒店被前台看不起，最后身份揭晓全场傻眼。"

→ 触发 `a02-weifu-bei-diaonan`，按"前压后弹"结构生成完整桥段。

**校验剧本**：

> "我写完一部 40 集短剧，帮我检查爽点分布和哪里不够爽。"

→ 触发 `shuangdian-jiaoyan`，逐集打标并输出体检报告。

---

## 🧭 文档导航

| 文档 | 作用 |
|---|---|
| [`INDEX.md`](./INDEX.md) | 完整爽点总目录 + 引用图 + 推荐学习顺序 |
| [`DIGEST.md`](./DIGEST.md) | 精华长文（不读原素材看这篇） |
| [`BOOK_OVERVIEW.md`](./BOOK_OVERVIEW.md) | 整书理解（主旨 / 骨架 / 术语 / 批判） |
| [`GLOSSARY.md`](./GLOSSARY.md) | 12 条共享术语词典 |
| [`verified.md`](./verified.md) | 26 个单元三重验证记录 |
| [`candidates/`](./candidates/) | 原始候选池（审计用） |
| [`rejected/`](./rejected/) | 重复套路合并 + 降智桥段拒绝记录 |

---

## ⚠️ 两条红线（蒸馏时强制保留）

1. **降智是毒药** —— 配角行为必须能用其立场 / 信息量解释；无脑装 X、强行降智会让读者瞬间出戏。
2. **爽点要多维 + 有梯度** —— 打架打脸之外，物质收获、地位提升、他人崇拜、感情收获同样有效；全剧最大的反差只能出现一次。

---

## 🔄 生态接入

- 所有 skill 均带 `test-prompts.json`（darwin-skill 兼容格式），可直接接入自动进化：

  ```bash
  darwin evolve books/400-duanju-shuangdian/
  ```

- 建议先读 [`INDEX.md`](./INDEX.md) 的"推荐学习顺序"：从信息差（d03）入手，再学 A/B/C 类桥段，最后用元技能校验。

---

## 📮 联系

- **官网**: https://icoolkj.com
- **作者**: daipeng
- **邮箱**: icoolkj@163.com / 594047667@qq.com
