# 从已选热点到单集大纲

编剧选一次热点，Agent 自行试两条创作路线、比较结构和梗、试写关键戏，交约 500 字的《北京一家人》推荐大纲。编剧可以直接给局部修改意见，直到明确认可这一版。

## 现在使用

从包含 `剧本系统/` 的目录打开 Claude Code 或 Cursor Agent。在当前对话的热点列表下直接回复：

> 招财童子，选第 3 条

Claude Code 通过项目的 `UserPromptSubmit` 钩子识别独立选择句；Cursor Agent 通过项目规则读取同一个任务入口。首次在已打开的 Claude Code 会话中加载新钩子，可打开 `/hooks` 或重启会话。

同一会话接着说「保留开头，中段换一种喜剧机制」即可改稿。新会话附上上一版大纲和运行记录。也可以直接提供选定热点的标题、事件摘要及已有来源。

## 接入 Cursor Automations

参照 pstack 的 Benny 包，将本包、`剧本系统/skills/` 和所需 `docs/` 放进运行端可读的同一仓库。用 [运行提示词](templates/automation-prompt.md) 创建 automation 草稿，选择实际支持的手动或事件触发入口。启动方把**选中的热点内容**传给任务；「第 3 条」只有在任务也收到原列表时才可解析。修改任务同时传上版及反馈。目录本身是 automation 源材料，线上启用需在目标运行端完成。

[任务入口](FOR_AGENTS.md) · [创作与返工步骤](skills/develop-outline/SKILL.md)
