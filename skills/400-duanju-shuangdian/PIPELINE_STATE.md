# PIPELINE_STATE.md — 流水线状态

> 蒸馏对象: 《400 个爆款短剧剧本爽点》内容总结
> 流水线: cangjie-skill (RIA-TV++)
> 最后更新: 2026-08-21

## 当前阶段

阶段 5 交付中（产物已全部生成，等待安装确认）。

## 阶段清单

- [x] **阶段 0 — 整书理解**: 产出 [BOOK_OVERVIEW.md](./BOOK_OVERVIEW.md)。用户已在任务约束中预先指定三大分类与交付物结构，骨架确认以任务约束为准。
- [x] **阶段 1 — 并行提取**: 源文本约 1100 字、单块即可覆盖，采用 5 类提取器**串行直读**（不 spawn 子代理，等价于短文本降级方案），产出见 [candidates/](./candidates/)。
- [x] **阶段 1.5 — 三重验证**: 26 个候选单元全部通过 V1/V2/V3，见 [verified.md](./verified.md)；被合并/淘汰的见 [rejected/](./rejected/)。
- [x] **阶段 2 — RIA++ 构造**: 26 个 skill（A 类 8 + B 类 7 + C 类 6 + D 类 4 + 元技能 1）全部生成 SKILL.md + test-prompts.json。
- [x] **阶段 3 — Zettelkasten 链接**: [GLOSSARY.md](./GLOSSARY.md) + [INDEX.md](./INDEX.md) + 各 SKILL.md 的 related_skills 段。
- [x] **阶段 4 — 压力测试**: 每个 skill 已写 test-prompts.json（darwin 兼容格式，含 ≥1 条同书兄弟 skill 诱饵）。独立盲测回填 test-results.md 为可选后续。
- [x] **阶段 5 — 交付**: [DIGEST.md](./DIGEST.md) 已生成。

## 各 skill 状态

| skill | 分类 | SKILL.md | test-prompts.json |
|---|---|---|---|
| a01-darenwu-fushou | A 身份反差 | ✅ | ✅ |
| a02-weifu-bei-diaonan | A 身份反差 | ✅ | ✅ |
| a03-duochong-majia | A 身份反差 | ✅ | ✅ |
| a04-muhou-dalao | A 身份反差 | ✅ | ✅ |
| a05-qinyou-buzhiqing | A 身份反差 | ✅ | ✅ |
| a06-saodiseng-shijue | A 身份反差 | ✅ | ✅ |
| a07-wujian-waimao-fancha | A 身份反差 | ✅ | ✅ |
| a08-shien-yu-guiren | A 身份反差 | ✅ | ✅ |
| b01-yueji-fansha | B 实力碾压 | ✅ | ✅ |
| b02-po-bingqi-sheng-shenbing | B 实力碾压 | ✅ | ✅ |
| b03-dazhao-wu-lengque | B 实力碾压 | ✅ | ✅ |
| b04-xuzhang-shengshi | B 实力碾压 | ✅ | ✅ |
| b05-jinzhishou-ziyuan | B 实力碾压 | ✅ | ✅ |
| b06-peijue-hongtuo | B 实力碾压 | ✅ | ✅ |
| b07-juzhong-ruoqing | B 实力碾压 | ✅ | ✅ |
| c01-jiazufan-dalian | C 打脸反转 | ✅ | ✅ |
| c02-xiaozhang-zhuan-xianmei | C 打脸反转 | ✅ | ✅ |
| c03-xuanfu-bei-nianya | C 打脸反转 | ✅ | ✅ |
| c04-jie-shizhuang-bi | C 打脸反转 | ✅ | ✅ |
| c05-wuxin-zhi-ju-re-bo | C 打脸反转 | ✅ | ✅ |
| c06-gonglao-bei-qiang | C 打脸反转 | ✅ | ✅ |
| d01-dihua-liu | D 叙事手法 | ✅ | ✅ |
| d02-puguang-liu | D 叙事手法 | ✅ | ✅ |
| d03-xinxi-cha | D 叙事手法 | ✅ | ✅ |
| d04-xitong-weizhuang | D 叙事手法 | ✅ | ✅ |
| meta-shuangdian-jiaoyan | 元技能 | ✅ | ✅ |

## 下一步

1. **安装到宿主 skills 目录**（用户确认后执行）：
   - 用户级: `~/.dsh/skills/`（DeepSeek Harness）
   - 项目级: `<项目>/.dsh/skills/` 或 `<项目>/.agents/skills/`
2. 可选: 独立 sub-agent 盲测 test-prompts.json，把通过率回填到各 skill 的 test-results.md。
3. 可选: 接入 darwin-skill 自动进化。
