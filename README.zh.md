<div align="center">

<img src="assets/hero.svg" alt="canva-slides — 用于 Canva 演示文稿的智能体技能" width="100%">

### 做出经得起 Canva 真实限制考验的幻灯片

**规划 · 构建 · 校验 · 发布** —— 忠于来源、完全可编辑、链接永不改变。

[![License: MIT](https://img.shields.io/badge/license-MIT-1F5FA8)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.1.0-1F5FA8)](skills/canva-slides/SKILL.md)
[![Skill](https://img.shields.io/badge/skills-1-1F5FA8)](#仓库结构)
[![Canva MCP + CLI](https://img.shields.io/badge/Canva-MCP%20%2B%20CLI-1F5FA8)](skills/canva-slides/references/00-preflight-and-environment.md)
[![Checked against live API](https://img.shields.io/badge/verified-live%20API-7BE0C3)](skills/canva-slides/SOURCES.md)

[English](README.md) · **中文** · [Tiếng Việt](README.vi.md) · [Русский](README.ru.md) · [Français](README.fr.md) · [Español](README.es.md)

</div>

---

## 为什么需要它

大多数"帮我做一套幻灯片"的技能都建立在两个经常不成立的假设上：

1. **AI 生成调用一定成功。** 并非如此：当月 AI 额度用尽后，`create-design` 会立即返回 `quota_exceeded`，重试毫无意义。
2. **生成后的幻灯片还能修。** 结构上修不了：没有任何 Canva 编辑操作能新增文本框，而编辑服务本身可能连续数小时返回 `503`。

这个技能记录的是实测中真正站得住的做法：先过规划校验，再逐条比对文字与来源，**逐页看渲染结果**，并准备一条完全不依赖 Canva AI 的退路——本地生成原生可编辑的 PPTX，再用 Canva 官方 REST 导入。

## 能力

- **先做设计访谈** —— 动工前先问清主题、密度、视觉语言、图片、引用与特殊页；问题按主题生成，答案写入 plan，缺失时 linter 阻止开工。
- **先规划后动笔** —— 主线、模式（演讲者 / 讲授 / 文档）、每页行动式标题、字数上限、案例覆盖；生成前由 linter 拦截错误结构。
- **忠于来源** —— 教科书 / PDF 场景附"幻灯片 ↔ 页码"对照表；来源之外的例子会在页面上标明。
- **视觉系统而非感觉** —— 1920×1080 的 px 字号阶梯、单一强调色、统一网格与边距、明确的"反 AI 味"禁用清单、原生图示。
- **给证据不给承诺** —— 文字 diff、逐页渲染、联系表、可测量的版式审计（错位、溢出、重叠、安全区）。
- **链接永不变** —— 通过 `POST /v1/merges` 做页面级替换；设计 id、链接与公开分享设置在更新后保持不变。
- **原生可编辑** —— Canva 中是真实文本框与矢量图形，绝不是整页图片。
- **按能力降级** —— MCP → CLI/REST → 本地 PPTX，取决于当前哪条路可用。
- **越南语优先** —— 完整声调符号、换行预测、教室字号、课程 / 答辩剧本。

## 安装

```bash
# omp managed skills
cp -R skills/canva-slides ~/.omp/agent/managed-skills/canva-slides

# 任何读取 SKILL.md 的智能体（Claude Code、Codex 等）
git clone https://github.com/thomas-nguyen-seamless/ai-skills-canva
cp -R ai-skills-canva/skills/canva-slides <你的技能目录>/
```

随后让技能准备环境：

```bash
skills/canva-slides/scripts/bootstrap.sh # 缺什么问一次
skills/canva-slides/scripts/bootstrap.sh --check # 只报告，不安装
```

`bootstrap.sh` **只安装缺失项** —— 已存在的显示 `[ok] … (already installed, skipped)`，绝不重装。之后它会检查两件无法代劳的事：Canva CLI 登录、MCP 挂载。

| 检查项 | 已存在时 | 缺失时 |
|---|---|---|
| `uv`、`python3`、`git`、`node ≥ 22`、`npx` | 报告，不动 | 用 Homebrew 安装（`uv` 可用官方脚本） |
| Canva CLI | 报告，不重新下载 | 经 `npx` 拉取一次（缓存，不全局安装） |
| Python 库（`pillow`、`numpy`、`scipy`、`python-pptx`、`lxml`、`pymupdf`、`pypdf`） | import 通过即跳过 | 预热到 uv 缓存 |
| Canva CLI 登录 | 打印账号名 | `canva login`，**需你在浏览器批准** |
| MCP `canva` | 确认 `mcp.json` 中存在 | 打印片段；**绝不覆盖**配置 |

## 快速开始

**新建演示文稿**

```text
/skill:canva-slides 依据 @triethocmaclenin.pdf 做 20 页"否定之否定规律"，
15 分钟，越南语，教室大字号
```

**修改现有演示文稿，链接不变**

```bash
scripts/update_canva_deck.sh DAHaPZNNOhs deck.pptx "tmp import" --pages "5,9"
```

**只评审，不改动**

```text
/skill:canva-slides 评审这个 Canva 稿件：https://canva.link/… —— 打分并列出缺陷
```

## 一套稿子怎么建成

<div align="center"><img src="assets/workflow.svg" alt="规划、构建、校验、发布、导出" width="100%"></div>

| # | 阶段 | 推进门槛 |
|---|---|---|
| 1 | **规划** —— 需求、来源对照表、术语、逐页记录、案例 | `plan_check.py --ghost` 报告 **0 错误** |
| 2 | **构建** —— Canva AI（`create-design`）*或* 原生 PPTX（Arial，实测文字高度） | 页数与计划一致 |
| 3 | **校验** —— 文字 diff、逐页渲染、版式审计、对比度 | 计划中的每条文字都在，无遗留硬伤 |
| 4 | **发布** —— 导入一次，之后在同一设计上做页面级更新 | 页数一致，链接与分享设置完好 |
| 5 | **导出** —— PDF/PPTX，核对页数，备注单独成文件 | 完成度清单全部勾选 |

## 更新共享的演示文稿

默认**按页**替换，因为稿件通常由多人共同编辑：

```bash
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --pages "5,7,12-14" # 只改这些页
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" --all # 全部（仅限单人稿件）
scripts/update_canva_deck.sh <ID> deck.pptx "tmp" # 拒绝执行
```

每页两次 merge 任务（插入 + 删除），总页数保持不变，页码不会中途错位。已在 20 页稿件上验证：替换第 5 页只改变**第 5 页**（1,266 像素），其余 19 页逐像素一致，设计 id、短链接与 `Can view` 权限均不变。

> 被替换的页来自本地构建，因此**该页上**的手工修改会丢失；其他页完全不受影响。

## 脚本

| 脚本 | 用途 |
|---|---|
| `bootstrap.sh` | 安装缺失依赖；检查登录与 MCP 挂载 |
| `intake_prompt.py` | 依主题生成开工前的设计问卷 |
| `plan_check.py` | 计划 lint：字数、标题、重复、节奏、目录、案例、ghost-deck |
| `text_diff.py` | 计划文字与实际文字比对 |
| `deck_audit.py` | 可测量版式审计：标题错位、安全区、溢出、重叠、AI 味痕迹 |
| `fit_check.py` | 改字前预测越南语换行与高度 |
| `contrast.py` | 投影用的 WCAG 对比度 |
| `diagrams.py` | 8 种图示，按最终页尺寸渲染 |
| `contact_sheet.py` | 所有页面合成一张带标注的图 |
| `post_upload.sh` | 一次性素材上传 |
| `update_canva_deck.sh` | 把 PPTX 推入现有设计，保留 id、链接与分享权限 |
| `templates/pptx-fallback/` | 原生构建器、铜版画素材处理、PowerPoint 渲染、渲染文字校验 |

## 仓库结构

```text
ai-skills-canva/
├── assets/ 封面与流程图
├── README.md 六语 README（EN · VI · ZH · RU · FR · ES）
└── skills/canva-slides/ 一个技能，但很深入
 ├── SKILL.md 路由：规则、阶段、快捷指令、工具、脚本
 ├── SOURCES.md 来源、取舍决策、按日期的验证日志
 ├── references/00…12 每个阶段一个文件
 ├── scripts/ 上述 10 个脚本
 ├── templates/ plan.json、brief-vi、deck-rules、speaker-notes、
 │ mcp-canva.snippet.json、pptx-fallback/
 └── research/ 调研笔记（标注来源）
```

## 技能内置的现实限制

| 现实 | 技能的做法 |
|---|---|
| `create-design` / `generate-image` 消耗**月度 AI 额度**（`quota_exceeded`，同步返回） | 立即停止，转无额度路径，告知重置日期 |
| `start-editing-transaction` 可能连续 `503` 数小时 | 降级为读取 + 导出 + 页面级 merge；未 commit 绝不说已改 |
| Canva 的 PPTX 导入会丢失形状内边距、段间距、freeform 描边 | 每段独立文本框、纯形状 + 独立文字、曲线用填充多边形 |
| 没有任何 API 能公开分享或删除设计 | 写明 UI 操作，不虚构命令 |
| 生成的稿件会改写措辞、可能替换术语 | 与计划做 diff；就地修改，绝不靠重新生成改字 |

完整证据、日期与来源：[`skills/canva-slides/SOURCES.md`](skills/canva-slides/SOURCES.md)。

## 许可证

MIT —— 见 [LICENSE](LICENSE)；第三方署名见 [NOTICE.md](NOTICE.md)。Canva 是 Canva Pty Ltd 的商标，本项目与 Canva 无隶属或背书关系。
