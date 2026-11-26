# 编剧指南 · 从 setup 到第一场戏

在 Codex 打开写稿文件夹，复制这一句：

```text
帮我安装剧本系统（https://github.com/ziyetsui/script-system），在当前项目下载或复用工作包，读里面的「skills/故事开发/SKILL.md」告诉我怎么开始写大纲。
```

也可以手动下载：在 GitHub 仓库首页点 **Code → Download ZIP**，解压。也可以从 **Code → HTTPS** 复制仓库地址，用 `git clone 仓库地址 剧本系统` 下载，把“仓库地址”替换成复制的地址。打开能同时看见 `skills`、`agents`、`automations` 的那一层。

| 已经在用什么 | 在哪里开始 |
| --- | --- |
| Codex | 在 Codex 中打开这个项目，或在该目录的终端运行已安装的 `codex`。 |
| Claude Code | 在该目录的终端运行已安装的 `claude`。 |
| Cursor | 用 Open Folder 打开这层目录，新建 Agent 聊天。 |

三种工具都可以直接贴同一句。只有网页聊天时，手动附上[写大纲 Skill 正文](../../skills/故事开发/SKILL.md)。

```text
/写大纲 小宁想让爷爷歇一天，给等修车的街坊发号请他们先散，请写发出第一张牌后的三个动作，停在小宁得亲自处理的新麻烦上。
```

安装时看技能名是不是“写大纲”，试写时看小宁发号后的三个动作。读完先问自己：“第二个人为什么跟着做？”历史答卷里，号码让街坊相信轮次有了保证，反而放心锁车、留下钥匙。如果这条因果成立，接下来就由编剧决定小宁在哪一场亲自撤单。 [看修车题的首轮答卷](../../skills/试跑记录/2026-11-26/group-01.md#run-008)

## 带自己的稿件进来

| 手上有什么 | 用哪个入口 | 这轮由编剧决定什么 |
| --- | --- | --- |
| 想先试一句 | [三句入门问法](roadmap.md#section-beginner) | 要几路试写、点名改稿，还是借作品找动作 |
| 想照着走一遍 | [《纸窗内外》四轮实例](roadmap.md#section-example) | 哪条线头值得追，哪段动机要重写 |
| 只有主题或生活点子 | [选高潮](roadmap.md#section-choice) → [写大纲](roadmap.md#section-outline) | 跟谁看，最后谁行动，舍掉什么 |
| 两场之间接不上 | [找梗及岗位交接](roadmap.md#section-roles) | 留下哪个会逼出下一场的动作 |
| 有旧稿，人物突然“懂事” | [从转念倒查原稿](roadmap.md#section-edit) | 最早哪一拍得改，哪些委屈要保住 |
| 有真实热点，要开发整集 | [招财童子独立仓库提示词](roadmap.md#section-automation) | 推荐稿是否成立，哪处退回返工 |
| 要给下一位编剧或新会话 | [续改与定稿](roadmap.md#section-handoff) | 认可哪一稿，下一轮从哪里开始 |

**查工具。** 项目总纲和人物资料在 `docs/harness/`。技能清单中的菜单别名取决于宿主配置，按正文路径读取就可以开始。用 Python 3 在仓库根运行 `python3 tools/skill_catalog.py` 可浏览各技能描述；输出路径起首是当前下载目录名。三个调度入口可从 `skills/找梗/`、`skills/群策/`、`skills/swarm/` 单独找。[项目总纲](../../docs/harness/北京一家人-创作大纲-520集.md) · [技能清单](../../skills/编剧技能清单.md) · [实际首轮记录](../../skills/试跑记录/2026-11-26/README.md)

**读整本。** Markdown 可直接在 GitHub 按章节跳转。下载 HTML 后用浏览器打开，全文搜索能定位到提示词；带去开会可用 PDF。[实战路线图](roadmap.md) · [离线网页](roadmap.html) · [PDF](roadmap.pdf)
