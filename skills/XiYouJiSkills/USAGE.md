# 使用文档

本文说明如何安装、使用和维护 `XiYouJiSkills`。

## 1. 环境要求

- 已安装 Codex，并支持本地 skills。
- 已安装 Python 3，用于运行本地检索和语料重建脚本。
- 日常对话不需要联网；只有重新下载原文时才可能需要网络。

## 2. 安装方式

克隆仓库：

```bash
git clone https://github.com/xiaomengsuifeng/XiYouJiSkills.git
cd XiYouJiSkills
```

安装全部角色：

```bash
mkdir -p ~/.codex/skills
cp -R wukong tangseng zhubajie shaseng guanyin rulai yuhuang taibai nezha litianwang erlangshen honghaier tieshangongzhu niumowang ~/.codex/skills/
```

只安装一个角色，例如孙悟空：

```bash
mkdir -p ~/.codex/skills
cp -R wukong ~/.codex/skills/
```

如果你希望修改仓库后立即生效，也可以使用软链接：

```bash
mkdir -p ~/.codex/skills
ln -s "$(pwd)/wukong" ~/.codex/skills/wukong
```

## 3. 对话使用

在 Codex 对话里直接引用目录名即可：

```text
用 $wukong 回答我，语气要像孙悟空，但不要脱离现代问题。
用 $tangseng 安慰一下焦虑的学生。
用 $zhubajie 用轻松贪嘴的口吻写一段周报吐槽。
用 $shaseng 给我一个稳重踏实的建议。
用 $guanyin 以慈悲但清醒的方式分析这个选择。
用 $niumowang 写一段火焰山借扇失败后的回应。
```

建议写清楚三件事：

- 要使用哪个角色 skill。
- 要回答什么问题或完成什么任务。
- 需要保留多少古典口吻，是否需要现代易懂。

示例：

```text
用 $wukong 和我对话。我要问职场冲突，你可以有孙悟空的机敏和直爽，但回答要现代中文、可执行。
```

## 4. 本地检索原文风格

每个角色都有自己的搜索脚本。进入角色目录后运行即可。

孙悟空：

```bash
cd wukong
python3 scripts/search_wukong.py "妖怪" --limit 5
python3 scripts/search_wukong.py "师父" --chapter 27 --limit 10
```

唐僧：

```bash
cd tangseng
python3 scripts/search_tangseng.py "悟空" --limit 5
```

牛魔王：

```bash
cd niumowang
python3 scripts/search_niumowang.py "芭蕉扇" --chapter 61 --limit 8
```

常用参数：

- `关键词`：要搜索的词，可以是人物、法宝、地名、语气词。
- `--chapter`：限定章回。
- `--limit`：限制返回条数。

## 5. 重新生成角色语料

每个角色目录里都有 `scripts/build_corpus.py`。如果你修改了抽取规则或替换了全文，可以重新生成：

```bash
cd wukong
python3 scripts/build_corpus.py
```

生成结果一般包括：

- `references/speech-corpus.jsonl`
- `references/source-index.md`
- `references/full-text/chapters/`

## 6. 重新下载《西游记》全文

各角色目录里保留了 `scripts/fetch_xiyouji.py`。日常使用不需要运行它，因为仓库已经带有本地全文。

需要更新全文时：

```bash
cd wukong
python3 scripts/fetch_xiyouji.py
python3 scripts/build_corpus.py
```

注意：下载脚本需要网络，且应确认文本来源许可适合你的发布方式。

## 7. 增加新角色

建议复制已有角色的结构，再调整四类内容：

- `SKILL.md`：角色行为准则、对话边界、使用本地语料的方式。
- `references/voice-profile.md`：角色说话风格、禁忌、场景处理。
- `references/speech-seeds.jsonl`：精选原文或仿写种子。
- `scripts/build_corpus.py`：角色别名、说话动词、过滤规则。

完成后运行：

```bash
python3 scripts/build_corpus.py
python3 -m py_compile scripts/fetch_xiyouji.py scripts/build_corpus.py scripts/search_角色名.py
```

## 8. 常见问题

### 安装后对话没有触发 skill

确认角色目录直接位于 `~/.codex/skills/` 下，并且目录里有 `SKILL.md`。

正确：

```text
~/.codex/skills/wukong/SKILL.md
```

错误：

```text
~/.codex/skills/XiYouJiSkills/wukong/SKILL.md
```

如果你把整个仓库复制进 `~/.codex/skills/`，Codex 可能不会把里面每个子目录都当成独立 skill。推荐复制或软链接每个角色目录。

### 是否每次对话都联网？

不需要。角色画像、精选语料、全文和分章材料都在本地。只有你主动运行下载脚本时才需要网络。

### 为什么同一个《西游记》全文在多个角色目录里都有一份？

这样做的好处是每个 skill 都能独立安装和离线使用。缺点是仓库体积更大。如果后续想做成更紧凑的仓库，可以把全文抽到共享目录，再让每个 skill 读取同一份公共资源。

### 可以直接商用吗？

这取决于你最终选择的开源许可证、文本来源许可，以及使用场景。发布前建议明确添加 `LICENSE`，并核对《西游记》文本来源说明。
