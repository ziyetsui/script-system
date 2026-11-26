# `/梁左` 大纲审改

在项目对话里输入 `/梁左 沿用刚才那版，保住主题，改完再评价`，或在命令后贴入当前大纲。[技能说明](SKILL.md) · [《奶奶的约会》用法示范](references/project-example.md)

| 要找的资料 | 包内位置 |
|---|---|
| 《我爱我家》001–120 集带时间码逐字稿 | [全集目录](references/transcripts/) |
| 六张原剧场面卡与作者资料 | [两个家庭现场](references/casebook.md) · [四张场面卡](references/scenes.md) · [梁左创作资料](references/author.md) |
| 编剧在《奶奶的约会》第 10 轮提出的改稿要求 | [现场演示完整对话](references/现场演示完整对话.md#L890) |
| 开发验收用的题目、答卷、评分及复测记录 | [盲测记录](validation/试跑卡-梁左审改大纲.md) |

将整个目录复制到其他位置后，在目录内运行 `python3 scripts/find_scene.py --episode 65 --at 00:04:40` 即可查询随包逐字稿。只有需要查询另一套语料时才传 `--root`。
