---
name: 群策
description: 编剧在选题、大纲、分场或审稿时调用 /群策，让项目里的相关故事模型、剧集、套路和导演视角并行尝试不同走法。可以只给卡点或沿用上文。
argument-hint: "[当前稿、卡点或想保住的条件，可留空沿用上文]"
disable-model-invocation: true
---

# 群策

读取[编剧 swarm 的完整分派规则](../swarm/SKILL.md)，在本轮直接按其流程执行。把 `$ARGUMENTS` 和最近的创作上下文作为输入。`/群策` 与 `/swarm` 共用这份规则，无需用户再次输入命令。
