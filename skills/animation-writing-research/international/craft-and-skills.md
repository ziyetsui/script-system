# 从制作资料到可执行的写作练习

核对日期为 2026-11-26。前半部分是动画主创、制作方及博物馆教学资料。后半部分是独立开发者的通用分镜方法，已核对仓库、正文、固定提交和许可；运行效果未测试。各节的「试做」均为本库原创改编。

## 先决定观众站在谁那边

《Peppa Pig》制片人 Phil Davies 回忆，团队把 Peppa 设为四岁，从她的视角讲系列故事。对照《Muddy Puddles》，「今天下雨」是客观情况，「现在出不去玩」才是孩子此刻关心的问题。[The Guardian，How we made Peppa Pig，Phil Davies 段](https://www.theguardian.com/tv-and-radio/2018/feb/19/how-we-made-peppa-pig)

**试做**　同一句「公共汽车开走了」，给孩子和站务员各写一个紧接着的动作。选择更能启动本集目标的一版。

## 把剧本读一遍，再决定第一张图

《Bluey》分镜师 Jasmine Moody 描述的流程是，先和 Joe Brumm 围读剧本，画第一版分镜，依据反馈修改。她把剧本和导演意图转成一组具体镜头，供后续工种沿用。她谈的是自己的工作流程，未在该访谈中将这套步骤绑定到《Rain》的某一镜。[Bluey 官网，Jasmine Moody，工作流程问答](https://www.bluey.tv/blog/jasmine-moody-storyboard-artist/)

**试做**　先读一遍包含「她改变了主意」的场景，两人各画一格转折。若一个画了角色皱眉，另一个画了她放下手中物品去帮忙，问哪一格同时解释了下一个人的反应。

## 用身体和时间表达意图

《Shaun the Sheep Movie》编导区分了无对白、偶的视觉表演和配音表情。《Mr Bean》2001 年制作报道记下动画师参考 Atkinson 真人表演的做法。TUBA 营销负责人在 2012 年介绍《Larva》早期规格时，谈到把篇幅压到约一分半，以及为触达更广年龄层而选用无对白的肢体喜剧。这是制作方当时对早期节目的说法。[Skwigly 编导访谈](https://www.skwigly.co.uk/shaun-sheep-movie-interview-directors-richard-starzak-mark-burton/) · [The Guardian 制作报道](https://www.theguardian.com/media/2001/feb/06/broadcasting2) · [News2day 访 TUBA，最小制作成本及肢体喜剧两节](https://www.news2day.co.kr/3996?site_preference=normal)

**试做**　同写一个人想拿回错递的帽子。第一版只许写身体动作；第二版给对方加一声轻咳；第三版删去一个来回。逐版找出观众第一次知道「递错了」的时刻。

## 用六格检查因果

Young V&A 教师指南第 6 页把想法、剧本、分镜、动态分镜串成制作步骤；第 21 页给出六格模板，要求选取开头、中段和结尾的关键时刻。Cartoon Museum 的《The Wrong Trousers》教学包第 34 页起是分镜活动。第 38 页先让学生在不知道教师答案的情况下解读六格，再让各人画同样的文字说明；第 42 页建议互换原创说明，看别人的图是否传达了作者的意思。活动中用到的早期未采用剧本与成片示例分列。[Young V&A 离线原版，第 6、21 页](documents/va-aardman-pdf/source.pdf) · [Cartoon Museum 离线文字，第 34–42 页](documents/cartoon-museum/source.txt)

**试做**　甲画六格后遮掉注释。乙逐格回答「谁让什么发生了变化」。把两人第一次读出不同因果的那一格圈起来，只改它的视点或动作，再请乙读一次。

## 三份可核对的公共 Skill

以下借用范围限于文本编剧与分镜评阅。离线原文统一为 `.txt`，可直接阅读。文件中出现的工具调用和安装说明属于作者文档。每个仓库的许可证随原文归档。

| 英文名与离线正文 | 原文解决的问题 | 可迁移的步骤与边界 |
|---|---|---|
| [animation](documents/animation/skill/source.txt) | 把知识说明拆成镜头表，再制作 HTML 动画 | 取「一镜一个信息点」和持续物体的位置连续性。改编为冰钓戏时，先画鱼、鱼堆与两个冰孔的相对位置。原文面向知识动画。 |
| [take-one](documents/take-one/skill/source.txt) | 为短片提出方案、画分镜并评阅成片 | 配套的 [Page or picture](documents/take-one/page-or-picture/source.txt) 要求盖住文字，分辨镜头只展示状态还是发生了事件。可用来查「一排孩子很着急」前后有没有动作和结果。 |
| [shot-specifier](documents/shot-specifier/skill/source.txt) | 已有场景清单后，逐镜规定人物位置、动作、摄影机、时长和切点 | 编剧可只取走位、动作与切点三栏，核对主角何时越过柜台、何时被误认成店员。完整工作流还依赖素材、图像或视频生成工具。 |

固定版本及许可分别为 [dimayip/animation-skill 原文](https://github.com/dimayip/animation-skill/blob/2bd612982642062084f62640e3c6ce7b1d5e2c62/SKILL.md) · [MIT](documents/animation/license/source.txt)，[talsiach/take-one 原文](https://github.com/talsiach/take-one/blob/38eb9030c88d14c12360889cd8317f8ffb81e9ab/SKILL.md) · [配套评阅页](https://github.com/talsiach/take-one/blob/38eb9030c88d14c12360889cd8317f8ffb81e9ab/references/page-or-picture.md) · [MIT](documents/take-one/license/source.txt)，[leynos/visual-storytelling-skills 原文](https://github.com/leynos/visual-storytelling-skills/blob/aae6386bb3cb383acf27dc6c86c0b56699cf64cb/skills/shot-specifier/SKILL.md) · [ISC](documents/shot-specifier/license/source.txt)。

## 下载原件与缺口

| 文档 | 离线保存形式 | 来源与核验 |
|---|---|---|
| Young V&A，Inside Aardman: Wallace & Gromit and Friends | [21 页 PDF，9,295,763 字节](documents/va-aardman-pdf/source.pdf) | [展览教师指南原件](https://vanda-production-assets.s3.amazonaws.com/2026/03/20/09/53/49/e33ef239-18d5-41d4-9341-7d9725bf1b5b/260316_0290_Aardman_Resource_A4_AW_R01%20%281%29.pdf)。文件头与 PDF 页数已核对，扫描未发现 JavaScript、表单或嵌入附件。原件 SHA-256 为 `49abe6b5701637a332d588afa84eb8dd40c8c64f12d86b68f026236adb833ab5`。 |
| Cartoon Museum，Wallace & Gromit School Activity Sheets | [保留分页的纯文字](documents/cartoon-museum/source.txt) | [52 页教学包原件](https://static1.squarespace.com/static/636d0f1190ba4247110f5c4a/t/656f0fb8ccce0c695ff21c63/1701777430055/WallaceGromit_School%2BActivity%2BSheets%2B%282%29.pdf)。解析器未报告活动脚本或附件；字节扫描命中了可能的脚本标记，因此本地只留文字，画格图像需看原件。下载原件 SHA-256 为 `b8e659078e0f0230cb081a6aa2c448cd7f0d7e26ff5fb7ea084c52fd229733bf`。 |

补检的 [Larva 展会资料 PDF](https://k-contentpavilion.id/wp-content/uploads/2022/10/Larva-IP-Introduction_EN_larva-S1-3-Isand-in-Mars.pdf) 在 TLS 连接阶段失败，未用于取证。《Larva》两集由制作方供稿的韩文梗概核定。[EBS 2017 综合目录](https://about.ebs.co.kr/files/about/files/global/2017_EBS_Preschoolers_Children_Catalogue.pdf) 的响应头报 57,819,018 字节；本次选用更直接的 ICONIX 节目规格与分集文本，未保存整本目录。网页主张均以中文卡片离线保留；镜头时间码、对白逐字稿和未见于梗概的结尾仍待看片核对。
