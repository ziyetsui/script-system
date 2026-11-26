# XiYouJiSkills

《西游记》角色本地离线 Codex Skills 集合。每个角色都是一个独立 skill，包含角色说明、口吻画像、原文发言候选、本地检索脚本和《西游记》全文分章材料，用来在对话中尽量贴近原著人物的说话方式。

## 特点

- 中文优先：skill 说明和使用方式面向中文对话。
- 本地离线：安装后日常对话不需要联网搜索。
- 原著打底：每个角色都带有《西游记》全文、分章索引和角色发言候选。
- 可检索：每个 skill 都提供本地搜索脚本，方便按关键词或章回查找原文语料。
- 可重建：保留构建脚本，可从本地全文重新生成角色语料。

## 已包含角色

| Skill 目录 | 角色 | 发言候选数 |
| --- | --- | ---: |
| `wukong` | 孙悟空 | 3080 |
| `tangseng` | 唐僧 | 1218 |
| `zhubajie` | 猪八戒 | 1098 |
| `shaseng` | 沙僧 | 357 |
| `guanyin` | 观音菩萨 | 133 |
| `rulai` | 如来佛祖 | 54 |
| `yuhuang` | 玉皇大帝 | 42 |
| `taibai` | 太白金星 | 33 |
| `nezha` | 哪吒 | 24 |
| `litianwang` | 托塔李天王 | 32 |
| `erlangshen` | 二郎神 | 24 |
| `honghaier` | 红孩儿 | 23 |
| `tieshangongzhu` | 铁扇公主 | 24 |
| `niumowang` | 牛魔王 | 26 |

## 快速开始

克隆仓库：

```bash
git clone https://github.com/xiaomengsuifeng/XiYouJiSkills.git
cd XiYouJiSkills
```

安装所有 skills 到 Codex 本地 skill 目录：

```bash
mkdir -p ~/.codex/skills
cp -R wukong tangseng zhubajie shaseng guanyin rulai yuhuang taibai nezha litianwang erlangshen honghaier tieshangongzhu niumowang ~/.codex/skills/
```

也可以只安装单个角色：

```bash
mkdir -p ~/.codex/skills
cp -R wukong ~/.codex/skills/
```

安装后，在 Codex 对话里直接点名 skill：

```text
用 $wukong 和我说话，回答要像孙悟空。
用 $tangseng 劝我静心处理这件事。
用 $zhubajie 用猪八戒的口吻吐槽一下今天的工作。
用 $niumowang 以牛魔王的口吻回应孙悟空来借芭蕉扇。
```

## 本地检索

每个角色目录下都有对应的搜索脚本。例如：

```bash
cd wukong
python3 scripts/search_wukong.py "妖怪" --limit 5
```

牛魔王示例：

```bash
cd niumowang
python3 scripts/search_niumowang.py "芭蕉扇" --chapter 61 --limit 8
```

搜索脚本只读取本地 `references/` 里的语料，不需要联网。

## 目录结构

每个 skill 目录大致如下：

```text
角色目录/
├── SKILL.md                         # Codex 读取的 skill 主说明
├── agents/openai.yaml               # skill 元信息
├── scripts/
│   ├── build_corpus.py              # 从本地全文重建角色语料
│   ├── fetch_xiyouji.py             # 可选：重新获取《西游记》全文
│   └── search_*.py                  # 本地语料检索脚本
└── references/
    ├── voice-profile.md             # 角色口吻画像
    ├── speech-seeds.jsonl           # 精选口吻种子
    ├── speech-corpus.jsonl          # 自动抽取的发言候选
    ├── source-index.md              # 章回索引和统计
    └── full-text/                   # 《西游记》全文和分章文本
```

## 更详细的使用说明

见 [USAGE.md](USAGE.md)。

## 开源前建议

- 添加开源许可证：如果希望别人可以自由使用和修改，建议选择 `MIT`、`Apache-2.0` 或其他明确许可证。
- 核对文本来源：本项目包含《西游记》全文材料，发布前应确认文本来源和附带声明符合你的开源发布方式。
- 初始化 git 仓库并推送到 GitHub：当前目录需要执行 `git init`、提交文件、添加远程仓库后再推送。
- 避免提交缓存文件：`.gitignore` 已忽略 `__pycache__`、`.pyc`、本地环境文件等。

## 免责声明

本项目用于文学角色风格研究、文本检索和本地 Codex skill 实验。角色口吻来自对公开文学文本的整理和提示词设计，不代表真实人物或官方改编作品。
