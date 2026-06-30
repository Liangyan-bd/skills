# 论文解读模板

Use this as the default structure for `deep`, `research`, `implementation`, and rich document outputs. For `triage`, use only section 0 plus the completion gate in `gate-rubric.md`. Keep exactly five top-level content sections unless the user asks for another format.

# 论文解读：<paper title>

## 0. 导读：先把握重点与不足

Purpose: let a reader understand the paper in five minutes before reading details.

Include:
- **5 分钟结论**: one concise callout covering the paper's problem, core idea, strongest contribution, and biggest weakness.
- **真正要记住 / 不要误读**: two-column bullets or a compact table.
- **四问四答**: explicitly answer `要解决什么问题 / 怎么解决 / 关键创新是什么 / 主要缺点是什么`.
- **导读必备五行决策表**: include a self-contained compact table with the required row labels `论文问题 / 核心发现 / 关键创新 / 机制判断 / 最大不足` and columns `一句话结论 / 关键证据与可信度 / 价值 / 边界 / 阅读决策`. If the reader has no time for details or excerpts only this table, it should convey the paper's main point, value, evidence strength, boundary, and whether the paper is worth reading for their goal.
- **价值链整合**: make the decision table connect the paper's problem pressure, action, evidence delta, reader value, and boundary into one coherent story.
- **价值主张**: state where the paper's value comes from: new framing, method, system capability, evidence, benchmark/dataset, theory, or engineering playbook.
- **论文主线图**: a short pipeline, Mermaid diagram, or ordered list from problem -> idea -> mechanism -> evidence -> limitation.
- **贡献与不足对照**: table with dimensions such as problem definition, method/system abstraction, technical mechanism, evidence, engineering value.
- **是否值得看 / 读者决策**: explicit recommendation: who must read it, who can skim it, and what to skip if time is limited.
- **读者路线**: which later sections to read for problem, mechanism, evidence, and adoption.

Do not bury the final judgment at the end only; front-load it here.
Do not make this section table-only. Add at least one narrative paragraph that explains the paper's core mechanism and the most important caveat in plain Chinese.

Required self-contained decision table:

| 导读项 | 一句话结论 | 关键证据与可信度 | 价值 / 边界 / 阅读决策 |
|-|-|-|-|
| 论文问题 | State the concrete problem, gap, or question the paper targets, including why prior work or common practice is insufficient. | Include source anchors plus `high/medium/low`: section, figure, table, equation, experiment, dataset, workload, baseline, metric, or source limitation. | Explain problem pressure, who should care, and who can skip it. |
| 核心发现 | State the most important finding, result, or conclusion the paper establishes, including direction and magnitude when available. | Include the strongest result/proof/measurement plus evidence strength and uncertainty. | Explain evidence delta and whether the result justifies reading the evidence section. |
| 关键创新 | State the concrete novelty or increment over prior work: new framing, method, system capability, benchmark, evidence, theory, or playbook. | Name the prior baseline/assumption and paper-specific anchor; mark novelty confidence. | Explain paper action, whether it is real novelty or packaging, and who should read deeply. |
| 机制判断 | State the shortest defensible explanation of how/why the method, system, or study works. | Anchor to architecture, algorithm, formal model, workflow, ablation, causal evidence, or author-provided mechanism; mark inference risk. | Explain reader benefit and whether the mechanism is adoptable, reproducible, comparable, or only a hypothesis. |
| 最大不足 | State the most important limitation, confounder, missing evidence, weak assumption, or non-claim. | Anchor to paper-admitted limitations, missing baselines, weak settings, external-validity gaps, or evidence-based critique; mark evidence strength. | Explain boundary condition, what not to overclaim, and whether this changes the reading priority. |

Rules:
- Treat this table as the minimum complete interpretation, not a table of contents.
- Do not fill `一句话结论` with a paper title paraphrase or broad field statement.
- Do not leave `关键证据与可信度` as "paper says so"; use concrete anchors and mark evidence strength/uncertainty.
- Do not use pointer-only cells such as "见第 2 节" or "详见实验"; the cell itself must contain the key information.
- The final decision column must make the paper's value chain explicit: `问题压力 / 论文动作 / 证据增量 / 读者收益 / 边界条件` should be covered by the five rows without adding a second value-chain table by default.
- The final decision column must make the table excerptable: after saving only this table, a reader can decide whether to deep-read, skim, use for related work, reproduce, or ignore the paper.
- Keep each cell concise, but make the row usable without reading later sections.

Value-chain integration rules:
- Pick one primary value class: problem framing, method, system capability, empirical evidence, benchmark/dataset, theory, or engineering playbook.
- Do not make every row a generic restatement of "important for the field"; each row must use paper-specific entities or evidence.
- The decision table should align with sections 1-4. If they tell different stories, revise.
- Add a separate value-chain table only when the user asks for an audit trail or when the paper has multiple competing value chains that cannot fit the decision table.

Optional claim ledger for audit-heavy or research outputs:

| Claim Ledger | claim | source_anchor | evidence_strength | uncertainty |
|-|-|-|-|-|
| 论文问题 | Concrete problem/gap claim from the 导读 table | Section/Figure/Table/experiment/source limitation | high/medium/low | Main uncertainty |
| 核心发现 | Headline finding claim from the 导读 table | Strongest result/proof/measurement | high/medium/low | What remains unproven |
| 关键创新 | Novelty/increment claim from the 导读 table | Related-work, method, benchmark, or evidence anchor | high/medium/low | Novelty search limitation |
| 机制判断 | Mechanism explanation claim from the 导读 table | Architecture/equation/ablation/causal evidence | high/medium/low | Inference risk |
| 最大不足 | Primary limitation claim from the 导读 table | Author limitation, missing baseline, weak setting, or critique | high/medium/low | Evidence that would change the judgment |

Optional supplemental value table:

| 价值来源 | 论文具体体现 | 对读者意味着什么 |
|-|-|-|
| New problem/method/system/evidence/benchmark/theory/playbook | Paper-specific facts | Why this changes understanding, research, or engineering decisions |

## 1. 论文定位：问题、增量与背景

### 1.1 基本信息

Include title, authors/institution, venue/arXiv/year, paper type (method/system/survey/position/benchmark/empirical/theory), source URL/PDF/DOI, intended readers, Source Manifest, and Citation Verification.

Required source manifest:

| Source Manifest | 内容 |
|-|-|
| source_type | arXiv TeX / arXiv HTML / PDF / DOI page / project page / user excerpt / previous summary |
| source_url | URL, local path, or document token |
| version | arXiv version, publication version, commit hash, file timestamp, or `(not visible)` |
| accessed_date | Absolute date when accessed |
| completeness | full text / abstract only / excerpt / missing appendix / figures checked from PDF / source unavailable |

Required source-depth check for `deep`, `research`, `implementation`, and rich outputs:

| Source Depth Check | 内容 |
|-|-|
| primary_source_used | TeX / HTML / PDF / official report / project page / previous summary |
| full_text_status | full_text_read / partial_full_text / abstract_only / source_unavailable |
| fallback_reason | Why a lower-priority or partial source was used, or `none` |
| unsupported_claims_policy | Claims downgraded, omitted, or marked uncertain because the source was incomplete |

Rules:
- A normal deep read must use full paper text when available. `abstract_only` or `previous summary only` is not a complete deep read.
- If full text is unavailable or time-bounded, state this in Source Depth Check and downgrade evidence, novelty, and mechanism claims in the 导读 table.
- Do not hide source limitations only in the final answer; put them in the document.

Required citation verification for document-style outputs:

| Citation Verification | 内容 |
|-|-|
| title_verified | yes/no plus source |
| authors_verified | yes/no plus source |
| venue_or_version_verified | venue, arXiv version, preprint status, or `(not visible)` |
| doi_or_arxiv_verified | DOI, arXiv ID, publisher URL, or `(not visible)` |
| code_data_supplement_checked | code/data/supplement/project status, or why unavailable |

### 1.2 问题：为什么需要这篇论文

Explain:
- The real-world or research pain point.
- Why existing approaches are insufficient.
- The concrete gap the paper targets.
- What improves if the paper's claim is true.
- A concrete example or scenario that makes the pain point tangible.

For deep reads, add a visibly labeled block such as:

| 关键问题 | 论文怎么具体化 | 为什么重要 |
|-|-|-|
| What the paper must answer | Concrete variables, workloads, metrics, baselines, or settings | Why this changes research or engineering decisions |

Avoid only paraphrasing the abstract.

### 1.3 一句话增量

Write exactly one sentence:
- `相对已有工作，本文首次/系统性地/更有效地...`
- Name the prior baseline or field if known.
- State the increment in capability, efficiency, quality, coverage, correctness, scale, or conceptual framing.

### 1.4 背景与基线

Cover key prior methods/systems/assumptions, what a strong baseline would look like, which part the paper changes, and domain terms needed before reading the method.

If the paper's Background/Motivation section contains high-signal evidence, add a compact subsection under section 1, such as `1.5 背景动机中的关键观察`. For each important observation or figure, explain:
- What the figure/measurement/counterexample examines.
- What the paper observes.
- What conclusion the authors draw.
- Your analysis or doubt about whether it really proves the problem.

## 2. 方法机制：<paper/method/system> 如何工作

This section must be self-contained enough that a reader can explain how the method/system works without opening the paper. Prefer paper-specific terms, variables, modules, states, equations, protocols, and runtime events over generic wording. If details are absent from the source, state the gap directly.

### 2.1 核心机制总览

Start with a short callout that answers `怎么解决` in one paragraph. For empirical, benchmark, and systems papers, explain that the "method" may be a measurement, attribution, or validation framework rather than a new algorithm.

For empirical/systems papers, prefer a problem-solving table:

| 设计动作 | 解决哪个问题 | 论文中的具体做法 |
|-|-|-|
| Experiment, component, analysis, ablation, or monitoring choice | Confounder, missing evidence, mechanism gap, attribution problem, or deployment risk | Paper-specific setup, metric, baseline, figure, or table |

Explain the main idea in 3-6 bullets:
- What the paper changes relative to the strongest prior baseline.
- Why the idea should work: the bottleneck, invariant, or causal path it attacks.
- What inputs it needs, what state it maintains, and what output/action it produces.
- What feedback loop, objective, optimization, protocol, state machine, or system policy drives it.
- What part is online/runtime behavior and what part is offline/preprocessing/training.

Add one narrative paragraph after the bullets explaining the mechanism in plain Chinese. The paragraph should use the paper's own concrete terms, not only category labels.

### 2.2 关键概念与对象模型

Define 3-7 concepts a reader must understand before reading the algorithm or architecture. For each concept, include:
- Plain-language definition.
- Role in this paper's mechanism.
- Boundary or common confusion.
- How it maps to a concrete variable, state, module, data structure, or runtime object when applicable.

Use a compact table if helpful, but add prose that explains how these concepts interact. Choose terms that are necessary for understanding this paper: abbreviations, protocols, system components, algorithms, metrics, baselines, workloads, threat models, or taxonomy axes. Do not fill the table with common words or document metadata.

### 2.3 数学或系统框架

For math-heavy papers, include:
- Variables, assumptions, objective/loss/reward, constraints, and optimization target.
- Key theorem, derivation, update rule, estimator, or scoring function.
- What the math buys: correctness, efficiency, stability, sample efficiency, calibration, etc.
- Where assumptions may fail.
- If the paper has central equations, reproduce the essential equations in LaTeX and explain every non-obvious symbol. Include only equations needed to understand the mechanism.

For system/framework papers, include:
- Architecture, data/control flow, state machine, scheduling/protocol/cache/deployment layout if relevant.
- Critical path and bottleneck.
- Resource ownership and lifecycle: allocation, migration, eviction, synchronization, rollback, or failure handling.
- Why this beats the baseline and where the analogy to OS/distributed-systems concepts stops being accurate.
- If the paper has a high-signal architecture, taxonomy, workflow, algorithm, or state-machine figure, embed a cropped figure when the output medium supports images; otherwise cite the figure/table number and describe what it shows.

If the paper has neither formal math nor concrete system design, state that explicitly and describe the closest conceptual framework.

Add a `High-Signal Anchors` block in section 2 or 3 for `deep` and richer outputs:

| High-Signal Anchors | 类型 | 为什么重要 | 解读中怎么使用 |
|-|-|-|-|
| Figure/Table/Equation/Algorithm X | 机制锚点 / 证据锚点 / 公式锚点 | What it reveals about mechanism, evidence, assumptions, or limitations | Which claim it supports or weakens |

Rules:
- Include at least one mechanism anchor and one evidence/result anchor when the paper provides them.
- If figures cannot be embedded, describe them precisely with figure/table/equation numbers and the takeaway.
- If only abstract/metadata were accessible, write `High-Signal Anchors unavailable because...` and downgrade the output as partial.

### 2.4 关键组件拆解

Make the method inspectable. Choose the representation that fits:
- Architecture table: component/module, responsibility, input, output, internal state, side effects.
- Data structure table: field/state, meaning, producer, consumer, lifecycle.
- Protocol table: actor, message/event, precondition, transition, result.
- Pipeline table: stage, operation, decision, cost, failure mode.

After the table, explain:
- Why each key component exists.
- Which baseline or naive alternative it avoids.
- Which component is on the critical path.
- Which component dominates memory, compute, communication, latency, or implementation complexity.

For survey/position papers, map the taxonomy or conceptual framework instead of inventing an algorithm. Still explain what the axes mean and why they are useful.

### 2.5 运行时 / 算法流程

Write the actual execution path. Use an ordered list, pseudocode, state-transition table, or Mermaid sequence/flow diagram. Cover:
- Initialization/preprocessing.
- Per-request/per-sample/per-iteration behavior.
- Decision points and thresholds.
- Update, feedback, or learning step.
- Stopping condition or output.
- Fallback/error path when the core assumption breaks.

For system papers, name the runtime event that triggers work, such as request arrival, cache miss, allocator failure, scheduler tick, timeout, retry, or backpressure. For algorithm papers, name the loop variable, scoring function, selection step, and update rule.

### 2.6 设计取舍、复杂度与失败模式

Explain:
- Why the design is better than obvious alternatives.
- What it pays in extra compute, memory, communication, latency, annotation cost, or implementation complexity.
- What failure mode remains even if the paper's main claim is true.
- Which ablation or sensitivity result should prove this mechanism is responsible for the gain.
- What would have to change for production or open-source implementation.

Do not let this section become generic. Tie each trade-off to a paper-specific mechanism, experiment, or assumption.

### Optional visual or pseudocode block

Include a diagram/pseudocode when the mechanism has multiple actors, state transitions, or nontrivial loops. A small accurate diagram is better than a decorative one. If you use a table/diagram, still include prose.

When using source figures or equation screenshots:
- Prefer 1-3 high-signal items from the paper: architecture diagrams, taxonomy figures, algorithm boxes, central equations, or result tables that explain why the method works.
- Put them in section 2 near the explanation they support, not as a detached appendix.
- Add a caption in Chinese explaining the figure's role in the mechanism and the key takeaway.
- If cropping or image insertion is unavailable, write `图/公式摘取说明：` and cite the figure/table/equation number with a precise textual reconstruction.
- Do not include decorative overview figures or screenshots whose text would be unreadable in the final document.

## 3. 证据与评价：贡献、局限与可信度

### 3.1 证据与结果

Extract evidence, not just conclusions:
- Evaluation setting: datasets, benchmarks, workloads, models, systems, hardware, or subjects.
- Metrics: accuracy, latency, throughput, cost, coverage, bug count, win rate, memory, energy, etc.
- Baselines: strongest compared methods and why they are fair or weak.
- Main results: concrete numbers when available, including baseline, denominator/scope, direction, and CI/variance if available.
- Ablation/sensitivity: what proves the mechanism, not just the final score.
- Failure cases: where the method does not work.

When the paper's value depends on attribution, confounder elimination, or causal interpretation, use an evidence-chain table:

| 证据链问题 | 论文结果 | 说明了什么 |
|-|-|-|
| The claim or doubt being tested | Concrete number, trend, CI, figure/table, or qualitative result | What this supports, what it rules out, and what remains unproven |

Add a Claim-Evidence-Value table when the paper's value might otherwise be implicit:

| 论文主张 | 支撑证据 | 价值判断 |
|-|-|-|
| Claim the paper needs readers to believe | Dataset/workload/baseline/metric/result/figure/table | Why this evidence matters and what it changes for research or engineering |

For `research` mode or hallucination-sensitive rich documents, add an evidence trace table using `evidence-trace.md`:

| Claim ID | 论文解读中的主张 | 证据位置 | 证据说明 | 可信度 | 仍不能证明什么 |
|-|-|-|-|-|-|

For each important experiment or measurement, prefer a structured block or table with:
- 测试目的: what claim this experiment is supposed to validate.
- 测试方案: dataset/workload/model/system/hardware/baseline setup.
- 测试结果: concrete number, trend, or qualitative finding.
- 数据解读: what the result supports, what it does not prove, and remaining doubts.

If evidence is weak, say exactly why: missing baseline, small dataset, unrealistic workload, leakage risk, no ablation, no statistical test, unreleased code, unclear implementation detail, no end-to-end task, no cost/latency report, or no red-team evaluation.
If a paper reports both synthetic and realistic workloads, separate the headline upper-bound from the more realistic central estimate and explain which one should guide engineering decisions.

### 3.2 真正的贡献

Separate contribution types:
- Conceptual contribution: new framing, taxonomy, problem definition.
- Technical contribution: new algorithm, model, protocol, data structure, or optimization.
- System contribution: implementation, integration, tooling, production constraints.
- Empirical contribution: new benchmark, measurement, dataset, or surprising result.
- Engineering playbook: reusable workflow or operational insight.

Then give a concise judgment of which contribution is strongest.

If the paper's contribution is easy to confuse with its result, prefer this table:

| 创新点 | 具体是什么 | 为什么算贡献 |
|-|-|-|
| Problem framing, method, system, empirical result, or playbook | Paper-specific detail | Why prior work did not already provide this |

When judging novelty or publishability, run `related-work-novelty.md` and include:

| Search Manifest | 内容 |
|-|-|
| database | arXiv/ar5iv, Semantic Scholar, OpenAlex, OpenReview, CrossRef/DBLP, GitHub/project page, or paper-internal related work |
| query | Exact search strings or title/citation-network seeds used |
| date | Absolute search date |
| hits_seen | Approximate number of hits inspected |
| candidates_kept | Number of candidates compared |
| exclusion_rule | What was excluded and why |
| limitation | What this search cannot establish |

| Candidate Screening | relation_type | why_included | why_excluded | similarity_dimension | confidence |
|-|-|-|-|-|-|

| 对比对象 / 既有做法 | relation_type | 已有工作覆盖了什么 | 本文真正新增 | 新颖性判断 | 证据缺口 |
|-|-|-|-|-|-|

If external related-work search was skipped, explicitly state that novelty is based only on paper-internal related work.

### 3.3 局限与问题

Include author-admitted limitations, inferred limitations, hidden assumptions, scalability/cost/robustness/correctness/security/privacy/maintainability risks, and what evidence would remove each concern.

For deep reads, turn limitations into a follow-up roadmap:

| 缺点 / 威胁 | 具体影响 | 后续应该补什么 |
|-|-|-|
| Limitation or confounder | What conclusion it weakens or blocks | Replication, ablation, dataset, workload, profiling, proof, or deployment validation needed |

Add a short `反误读 / 负空间` note:
- What the paper did not prove.
- Where the result should not be extrapolated.
- Which production/research decisions still require more evidence.
- Which author claims are plausible but not fully established by the experiments or proof.

### 3.4 博导式评价

Use direct, grounded judgment:
- 选题眼光
- 方法成熟度
- 实验证据
- 论文表达与可复现性
- 最终判决: Strong Accept / Accept / Weak Accept / Borderline / Weak Reject / Reject, with one-sentence reason.

Do not use conference-style verdicts if the user asks for a neutral business or engineering review.

For `deep`, `research`, `implementation`, and rich document outputs, run `critic-mode.md` and include both a Mini Peer Review Panel and full Critic Mode block:

| Mini Peer Review Panel | 主要判断 | 影响 |
|-|-|-|
| 方法审稿人 | Method/protocol/proof/system design judgment | What to keep, narrow, or drop. |
| 实验证据审稿人 | Baseline, metric, ablation, and result-strength judgment | What evidence is strong, weak, or missing. |
| 领域落地审稿人 | Engineering/research adoption judgment | What to adopt, reproduce, monitor, or ignore. |
| 写作审稿人 | Problem framing, contribution framing, evidence ordering, and limitation-writing judgment | Writing lesson and rewrite priority. |
| Devil's Advocate | Strongest alternative explanation or overclaim risk | How to downgrade value and reading decision. |

| Critic Mode | 最强质疑 | 需要什么证据反驳 | 当前证据是否足够 | 结论调整 |
|-|-|-|-|-|
| Problem framing attack | Maybe the problem is already solved, too narrow, or not important. | Prior work, benchmark gap, real-world failure/cost. | enough / partial / weak | Keep, narrow, or drop the problem value claim. |
| Method/action attack | Maybe the proposed method is routine packaging. | Mechanism delta, comparison to baselines, ablation. | enough / partial / weak | Keep, narrow, or drop the innovation claim. |
| Evidence attack | Maybe the headline result does not support the claim. | Metrics, setup, variance, controls, confounder checks. | enough / partial / weak | Keep, narrow, or downgrade evidence confidence. |
| Generalization attack | Maybe the result only holds in a narrow setting. | Workload/model/hardware/data diversity and external validation. | enough / partial / weak | State boundary and reading decision downgrade. |

Rules:
- The Mini Peer Review Panel is a compact review, not a generic praise/critique section.
- The Critic Mode block must attack the interpretation's own main value thesis, not only repeat author limitations.
- If an attack cannot be answered with concrete paper evidence, downgrade the section 0 reading decision and state the non-claim.

## 4. 工程落地与后续问题

### 4.1 对我 / 团队有什么用

Translate the paper into action:
- Which workflow/system/research direction it may change.
- What can be copied immediately.
- What should be tested before adoption.
- What is not worth copying.
- Possible internal experiments or prototypes.
- Whether the paper is "must read", "skim", or "archive for later" for the likely reader, with one concrete reason.

### 4.2 领域视角

Adapt to the user context:
- Linux kernel engineer: subsystem fit, syzkaller/perf/debugging implications, upstreamability, config/build/test cost.
- AI infra engineer: serving cost, GPU utilization, KV cache, batching, scheduler, eval reliability, observability.
- Security engineer: threat model, exploitability, fuzzing/static analysis integration, false positive handling.
- Backend/system engineer: latency, consistency, storage, rollout, failure modes, SLO impact.
- Researcher: open questions, missing ablations, publishable extensions.

If context is unknown, write "通用工程视角". If the paper is a systems, memory, scheduler, OS, serving, reliability, or performance paper and the working context suggests kernel/performance/AI infra work, include both an `AI infra 视角` paragraph and a `Linux 内核工程师视角` subsection. The Linux subsection should contain 2-4 concrete analogies or contrasts, such as page fault vs allocation failure, mmap/VMA vs virtual handle space, THP/huge pages vs heterogeneous page sizes, slab/page allocator vs model cache pools, reclaim/compaction vs migration, NUMA vs multi-GPU pool coordination, cgroup pressure vs tenant/SLO accounting.

### 4.3 复现 / 落地清单

Use when implementation or follow-up work matters:
- Required code, data, model, config, hardware, and dependencies.
- Minimal reproduction steps.
- Expected outputs and sanity checks.
- Likely blockers.
- Metrics to track during reproduction.
- A small first experiment that can validate value quickly.

### 4.4 值得追问的问题

List 3-8 sharp questions for authors, reviewers, engineering adoption, or follow-up research.

For `research` mode, include at least one question about novelty/related work and one question about what evidence would change the current judgment.

### 4.5 写作视角：这篇论文写得如何，如果我来写会怎么写

Required for document-style `deep`, `research`, `implementation`, and rich wiki outputs. Keep the analysis grounded in this paper rather than generic writing advice, so the reader can learn how the paper was written and how it could be rewritten.

Cover:
- What the paper does well as writing: problem opening, difference from prior work, contribution framing, method-to-question mapping, evidence ordering, threat-to-validity honesty.
- What could be improved: whether research questions are explicit, whether contributions are separated from results, whether the result section has a roadmap, whether root-cause or scope boundaries are front-loaded enough.
- Reusable writing techniques: how to turn an engineering observation into a research question, how each experiment should carry one causal role, how to write negative results and limitations without weakening the paper.

Recommended tables:

| 写得好的地方 | 具体做法 | 可学习技巧 |
|-|-|-|

| 写作上可改进 | 当前问题 | 如果我来写 |
|-|-|-|

| 给读者的写论文技巧 | 可复用模板 |
|-|-|

### 4.6 一句话总结

End with one sentence that preserves the technical core and practical implication. It can be vivid, but must not overclaim.

Optional knowledge card for wiki/archive workflows:

| 卡片项 | 内容 |
|-|-|
| 可复用概念 | Paper-specific concepts worth remembering. |
| 可复用方法 | Measurement, algorithm, proof, system, or evaluation pattern. |
| 可复用写法 | Problem framing, contribution framing, evidence ordering, or limitation writing technique. |
| 可追踪关键词 | Search terms, systems, datasets, benchmarks, authors, or subfields to monitor. |
| 会修正的旧认知 | Prior belief this paper should update or weaken. |
| 下次遇到类似论文先看什么 | Figures, tables, metrics, sections, or failure modes to inspect first. |

# Completion Gate

After drafting the interpretation, run the completion gate in `SKILL.md` before returning or publishing.

Do not add the full gate checklist as a top-level document section unless the user asks for an audit trail. In chat, report a compact verdict:

- `门禁检查结果：PASS` plus 3-5 concrete anchors that prove the read is complete enough.
- `门禁检查结果：BLOCKED` plus `gate / missing evidence / next fix` if any required gate remains unsatisfied.

For rich documents, add a short `门禁未满足说明` callout only when a required gate cannot be satisfied with available source/tools.

Reader-usability check before PASS:
- Can the reader answer `要解决什么问题 / 怎么解决 / 关键创新是什么 / 主要缺点是什么` from section 0 directly?
- If the reader only reads or excerpts the required five-row 导读 table, can they understand the paper's main problem, solution logic, value, evidence strength, biggest caveat, and whether it is worth reading for their goal?
- Can the reader state the paper's primary value chain: problem pressure, paper action, evidence delta, reader benefit, and boundary condition?
- Can the reader answer the core four questions in five minutes?
- Can the reader explain the mechanism without opening the PDF?
- Can the reader say why the paper is valuable and what it does not prove?
- Can the reader decide whether to read, adopt, reproduce, or follow up?

When Markdown/text/Lark XML is available, run `scripts/interpretation_gate_check.py --mode <triage|deep|research|implementation> <draft-or-export>` before reporting PASS.

# Variant Rules

## Method Paper

Emphasize:
- Problem formulation and assumptions.
- Algorithmic mechanism, objective, update rule, or decision policy.
- Why the mechanism should beat the strongest baseline.
- Main ablation/sensitivity that proves the mechanism matters.
- Failure conditions and where assumptions break.

## Survey / Position Paper

Emphasize:
- Taxonomy quality.
- Whether the framing aligns scattered work.
- Missing categories or biased selection.
- Whether the future agenda is actionable.

De-emphasize exact numerical results if the paper is not claiming a new method.

## System Paper

Emphasize:
- Architecture, integration constraints, operational failure modes.
- Cost model and bottlenecks.
- Deployment assumptions.
- Comparison with production-grade baselines.
- Design rationale in prose, not only component tables.
- OS/distributed-systems analogy when useful, plus where the analogy stops being accurate.
- Production readiness gap: what must be integrated, instrumented, benchmarked, or hardened before deployment.
Keep all of these under section 2 and section 3, not as extra top-level sections.

## Empirical Study

Emphasize:
- Measurement question and why it matters.
- Study design, workload/data/source selection, controls, and statistical validity.
- Surprising or belief-changing findings.
- Confounders, external validity, and what the evidence does not prove.
- What research or engineering practice should change because of the measurement.

## Benchmark Paper

Emphasize:
- Task design, data quality, leakage risk, metric validity.
- Whether the benchmark measures the intended capability.
- How hard it is to game the benchmark.
- Whether the benchmark will remain useful over time.
Put data quality, leakage risk, and metric validity in section 3.1/3.3.

## Theory Paper

Emphasize:
- Formal assumptions.
- Meaning of theorem statements.
- Which assumptions are realistic.
- Whether the theory explains a practical phenomenon or only a narrow case.
Put formal assumptions and theorem meaning in section 2.3, and realism concerns in section 3.3.
