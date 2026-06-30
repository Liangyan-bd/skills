---
name: paper-interpretation
description: "Use when Codex is asked to read, explain, critique, summarize, or produce a structured interpretation for academic papers, arXiv/PDF links, conference papers, technical reports, survey/position papers, benchmark papers, or user-provided paper excerpts; triggers include 论文解读, 论文精读, 读论文, paper analysis, paper reading, 博导式评价, 工程视角洞察."
---

# Paper Interpretation

## Overview

Produce a rigorous Chinese paper interpretation, not a generic abstract summary. The output must let the reader decide what problem the paper solves, how it solves it, what is truly new, what evidence supports it, what it does not prove, and whether it is worth reading or using.

Default language is Chinese unless the user asks otherwise. Keep paper titles, method names, datasets, baselines, equations, and system identifiers in their original technical form when translation would reduce precision.

## Reference Routing

Read only the references needed for the current task:

| Need | Read |
|-|-|
| Source fetching, source priority, or source manifest | `references/source-ingestion.md` |
| Full document or deep-read structure | `references/interpretation-template.md` |
| Choose triage/deep/research/implementation mode | `references/reading-modes.md` |
| Evidence trace or hallucination-sensitive output | `references/evidence-trace.md` |
| Citation verification or source identity checks | `references/source-ingestion.md` |
| Innovation, novelty, related work, search manifest, or publishability judgment | `references/related-work-novelty.md` and `references/critic-mode.md` |
| Strong value claims, reliability critique, Mini Peer Review, or Devil's Advocate check | `references/critic-mode.md` |
| Reusable notes, wiki/Obsidian archive, or future retrieval | `references/knowledge-card.md` |
| Completion gate details | `references/gate-rubric.md` |

## Workflow

1. Gather the source.
   - Use `references/source-ingestion.md`.
   - Prefer arXiv TeX source when available, then arXiv/ar5iv HTML, then official PDF/DOI/project pages, then user-provided excerpts.
   - If the user provides only a title, verify the exact paper before analyzing.
   - Do not rely only on an older summary when the original paper is available.
   - If only partial text is available, state the scope limitation and avoid unsupported claims.
   - Create a `Source Manifest` for every single-paper interpretation, including `source_type`, `source_url`, `version`, `accessed_date`, and `completeness`.
   - For `deep`, `research`, `implementation`, or rich document outputs, create a `Source Depth Check` with `primary_source_used`, `full_text_status`, `fallback_reason`, and `unsupported_claims_policy`. Deep reads must use full paper text (TeX, HTML, PDF, or official full report) when available. Abstract/metadata plus older summaries are not enough for a normal deep read; if full text is unavailable or time-bounded, mark the output as partial and downgrade claims.
   - Create `Citation Verification` for document-style outputs: title, authors, venue/version, DOI/arXiv ID, and code/data/supplement status.
   - Create `Search Manifest` and `Candidate Screening` only for `research`, novelty, related-work, publishability, or "是否值得跟进" judgments. If no external search was feasible, mark the source as paper-internal related work and state the limitation.
2. Choose the output mode using `references/reading-modes.md`.
   - Use `triage` for "is it worth reading" or backlog filtering.
   - Use `deep` for normal 论文解读/精读 and rich docs.
   - Use `research` for novelty, writing lessons, or follow-up research planning.
   - Use `implementation` for reproduction or engineering adoption.
3. Classify the paper: method, system, survey/position, benchmark, empirical study, or theory.
4. Extract the reader-decision spine before drafting:
   `要解决什么问题 -> 为什么已有方法/基线不够 -> 怎么解决 -> 关键创新 -> 证据链 -> 缺点/边界 -> 读者下一步`.
5. Extract the value chain before drafting:
   `问题压力 -> 论文动作 -> 证据增量 -> 读者收益 -> 边界条件`.
   If this cannot be stated with paper-specific nouns, metrics, figures, experiments, or limitations, reread the introduction, method, results, and limitations.
6. Run preflight checks:
   - Source depth is enough for the chosen mode.
   - Source Manifest is complete enough to make the interpretation reproducible.
   - For `deep` and richer modes, full-text status is explicit in `Source Depth Check`; any missing full text has a concrete fallback reason and a visible unsupported-claims policy.
   - Citation identity is verified or explicitly marked not visible.
   - High-signal figures/tables/equations are identified for `deep` and richer outputs. Include at least one mechanism anchor and one evidence/result anchor when the paper has them; if none are available, state the source limitation.
   - Empirical/system/benchmark experiments are mapped to the claim or causal question they answer.
   - Negative space is extracted: what the paper does not prove and where not to extrapolate.
   - For `deep` and richer outputs, run Mini Peer Review and a full Critic Mode pass. For strong novelty, value, reliability, or publishability claims, also run related-work search logging and Candidate Screening; if a step is infeasible, state the concrete blocker.
7. Draft with the relevant template and mode.
8. Run the completion gate in `references/gate-rubric.md`. If Markdown/text/Lark XML is available, also run:
   ```bash
   scripts/interpretation_gate_check.py --mode <triage|deep|research|implementation> <draft-or-export>
   ```

## Mandatory Section 0 Requirements

Every single-paper interpretation in `triage`, `deep`, `research`, `implementation`, or rich document mode must make section `0. 导读` excerptable.

It must include:
- Four explicit reader questions: `要解决什么问题 / 怎么解决 / 关键创新是什么 / 主要缺点是什么`.
- A self-contained `导读决策表` with exactly these row labels: `论文问题`, `核心发现`, `关键创新`, `机制判断`, `最大不足`.
- Prefer the compact table columns `一句话结论`, `关键证据与可信度`, `价值 / 边界 / 阅读决策`. The legacy columns `要点结论`, `关键支撑`, `价值判断`, `阅读决策` are still accepted for existing documents.
- The value chain integrated into the table through the final decision column: `问题压力 / 论文动作 / 证据增量 / 读者收益 / 边界条件`.
- Paper-specific evidence anchors in each row, such as section, figure, table, equation, experiment, dataset, workload, baseline, metric, or explicit source limitation.
- Evidence strength and uncertainty must be visible either in `关键证据与可信度` or in a separate `Claim Ledger`. Prefer the compact column for normal deep reads; use a separate Claim Ledger only for audit-heavy or research outputs.

Do not use pointer-only cells such as "见第 2 节" or "详见实验". A reader who saves only this table must still understand the paper's problem, solution logic, value, evidence strength, biggest caveat, and reading decision.

## Writing Rules

- Start with `# 论文解读：<paper title>` for document-style output.
- For deep single-paper reads, use exactly five top-level content sections:
  - `0. 导读：先把握重点与不足`
  - `1. 论文定位：问题、增量与背景`
  - `2. 方法机制：<paper/method/system> 如何工作`
  - `3. 证据与评价：贡献、局限与可信度`
  - `4. 工程落地与后续问题`
- The script gate enforces this five-section structure for `deep`, `research`, and `implementation` outputs, including the core subsections under sections 1-4.
- Put 基本信息、问题、背景、机制、证据、贡献、局限、复现、写作视角 under those five sections, not as extra top-level chapters.
- Keep `一句话增量` to one concrete delta over prior work, not a title paraphrase.
- Separate paper claims, evidence-supported conclusions, and your evaluation with wording such as "论文声称", "证据显示", and "我的判断是".
- Do not let tables replace explanation. Every major section needs at least one paper-specific prose paragraph.
- Make the mechanism inspectable with paper-specific objects, variables, modules, equations, workflows, state transitions, or experiments.
- For empirical, benchmark, and systems papers, organize key evidence as a claim/evidence/value or evidence-chain table.
- For `deep`, `research`, `implementation`, and rich docs, include `High-Signal Anchors`: 2-4 high-signal figures/tables/equations/algorithms when available, including at least one mechanism anchor and one evidence/result anchor. If source access prevents this, say so explicitly.
- For document-style `deep`, `research`, `implementation`, or rich wiki outputs, include `Mini Peer Review Panel` under section 3.4 with 方法审稿人、实验证据审稿人、领域落地审稿人、写作审稿人、Devil's Advocate.
- For document-style `deep`, `research`, `implementation`, or rich wiki outputs, include `Critic Mode` under section 3.4 with Problem framing attack、Method/action attack、Evidence attack、Generalization attack, and downgrade conclusions when the attack is not answered by evidence.
- For systems, memory, scheduler, OS, AI infra, serving, performance, or reliability papers, include a concrete engineering/domain lens under section 4.
- For document-style `deep`, `research`, `implementation`, or rich wiki outputs, include `写作视角：这篇论文写得如何，如果我来写会怎么写` under section 4. The script gate blocks deep/richer outputs that omit it.

## Optional Enhancements By User Goal

- **Evidence trace:** For research, rich docs, or high-stakes interpretation, add the artifact from `references/evidence-trace.md`.
- **Critic mode:** For `deep` and richer outputs, run `references/critic-mode.md`, include Mini Peer Review and the full four-attack Critic Mode table, and downgrade claims that cannot survive the attack.
- **Related-work/novelty check:** When judging innovation or publishability, use the executable workflow in `references/related-work-novelty.md`, include Search Manifest and Candidate Screening, and do not treat the paper's own "first" claim as proven.
- **Knowledge card:** For wiki/archive workflows, add the compact card from `references/knowledge-card.md`.
- **Implementation notes:** For reproduction/adoption, include required code/data/model/config/hardware, minimal reproduction steps, expected outputs, risks, and validation metrics.

## Failure Handling

- If a hard gate fails and can be fixed with available sources/tools, revise before answering or publishing.
- If a gate cannot be satisfied, include `门禁未满足说明：<gate> - <concrete blocker>`.
- Never claim "已完成", "完整解读", "已生成", or equivalent while any fixable hard gate remains unmet.
