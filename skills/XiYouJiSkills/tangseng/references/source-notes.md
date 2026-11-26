# 本地语料来源说明

## 推荐来源

完整章回文本优先从 Project Gutenberg 下载：

- 作品：`Xi You Ji / 西遊記`
- 编号：`23962`
- 页面：`https://www.gutenberg.org/ebooks/23962`
- 纯文本候选地址：
  - `https://www.gutenberg.org/files/23962/23962-0.txt`
  - `https://www.gutenberg.org/cache/epub/23962/pg23962.txt`
  - `https://www.gutenberg.org/ebooks/23962.txt.utf-8`

备用来源：

- 维基文库《西游记》：`https://zh.wikisource.org/zh-hans/西游记`

## 使用原则

- 本 skill 的核心语气画像是本地蒸馏资料，可直接离线使用。
- 完整原文由 `scripts/fetch_xiyouji.py` 下载到本地，不在对话时联网搜索。
- 下载后运行 `scripts/build_corpus.py`，生成分章文本、章回索引和唐僧发言候选。
- 引用原文时保留章回信息；不要把风格化句子说成原文。

## 许可提醒

《西游记》原著为公版古典小说。Project Gutenberg 和维基文库页面各自带有使用条款或授权说明；如果把下载后的全文随 skill 再分发，应保留来源说明和相应许可信息。
