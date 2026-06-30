# Completion Gate Rubric

Run this after drafting and after any document/wiki/slides update. Passing means the interpretation is useful without reopening the paper.

## Procedure

1. Classify output mode: `triage`, `deep`, `research`, `implementation`, `rich document/wiki/slides`, or `paper collection`.
2. Check required gates against the actual output, not intent.
3. Fix all fixable failures before finalizing.
4. If a required gate cannot be satisfied, include `门禁未满足说明：<gate> - <concrete blocker>`.
5. Report `门禁检查结果：PASS` or `BLOCKED` with 3-5 concrete anchors.

## Required Gates

| Gate | Pass condition |
|-|-|
| Source depth | Original PDF/HTML/full text was used when available. Deep/research/implementation outputs include `Source Depth Check` with `primary_source_used / full_text_status / fallback_reason / unsupported_claims_policy`; abstract/metadata-only reads are marked partial and claims are downgraded. |
| Source manifest | Output records `Source Manifest` with `source_type / source_url / version / accessed_date / completeness`. |
| Citation verification | Deep/research/implementation outputs record `Citation Verification` with title, authors, venue/version, DOI/arXiv, and code/data/supplement status. |
| Deep structure | Deep/research/implementation outputs use the fixed five-section structure: `0. 导读`, `1. 论文定位`, `2. 方法机制`, `3. 证据与评价`, `4. 工程落地与后续问题`, with core subsections under sections 1-4. |
| Four questions | Section 0 explicitly answers `要解决什么问题 / 怎么解决 / 关键创新是什么 / 主要缺点是什么`. |
| Intro decision table | Section 0 contains the five mandatory rows. Prefer compact columns `一句话结论 / 关键证据与可信度 / 价值 / 边界 / 阅读决策`; legacy columns remain accepted. |
| Claim evidence strength | The five 导读 rows expose source anchor, evidence strength, and uncertainty either via `关键证据与可信度` or a separate Claim Ledger. |
| Problem clarity | The output explains the problem and why existing work, benchmarks, or practice are insufficient. |
| Mechanism/solution | The method/system/study is inspectable with paper-specific objects, workflow, equations, modules, or experiments. |
| Evidence chain | Key results are connected to the causal question or claim each supports. |
| Value thesis | The interpretation states why the paper matters to the likely reader. |
| Value chain | The 导读决策表 connects `问题压力 / 论文动作 / 证据增量 / 读者收益 / 边界条件`. |
| Claim evidence | Major claims have evidence anchors or an explicit uncertainty label. |
| Innovation | Conceptual, technical/system, empirical, benchmark, and engineering contributions are separated. |
| Search manifest | Research/novelty/publishability outputs record database/query/date/hits/candidates/exclusion/limitation, or explicitly state paper-internal-only search. |
| Candidate screening | Research/novelty/publishability outputs include candidate relevance and exclusion reasoning, not only final comparison. |
| Critic / Devil's Advocate | Deep/research/implementation outputs include full `Critic Mode` with Problem framing attack, Method/action attack, Evidence attack, Generalization attack, and conclusion adjustment. Strong value, novelty, reliability, or publishability claims are downgraded if the attack is not answered. |
| Mini peer review | Deep/research/implementation outputs include `Mini Peer Review Panel` with method, evidence, domain, writing, and Devil's Advocate perspectives. |
| Limitations | Author-admitted and inferred limitations include their impact and needed follow-up evidence. |
| Non-claim | The output states at least one important thing the paper does not prove. |
| Visual/formal anchors | Deep/research/implementation/rich outputs include `High-Signal Anchors`: at least one mechanism anchor and one evidence/result anchor when the paper provides figures/tables/equations/algorithms; otherwise the source limitation is explicit. |
| Domain usefulness | Section 4 translates the paper into concrete reader actions or follow-up questions. |
| Writing lens | Deep/research/implementation document outputs include `写作视角：这篇论文写得如何，如果我来写会怎么写` under section 4 with paper-specific writing strengths and rewrite advice. |
| No placeholders | No major section is filled with generic labels unsupported by paper details. |

## Mode-Specific Gates

- `triage`: source depth, source manifest, four questions, compact intro decision table, value thesis, largest limitation, and reading decision are mandatory.
- `deep`: all required gates apply except Search Manifest and Candidate Screening unless the output makes strong novelty/publishability claims; Source Depth Check, High-Signal Anchors, Mini Peer Review Panel, full Critic Mode, and writing lens are mandatory for document-style outputs.
- `research`: all deep gates plus evidence trace, Search Manifest, Candidate Screening, executable novelty check when feasible, critic mode, Mini Peer Review, writing lens, and knowledge card.
- `implementation`: all deep gates plus reproduction inputs, environment assumptions, validation metrics, and engineering risks.
- `paper collection`: apply a compact version per paper and add cross-paper comparison.

## Script Gate

When Markdown, text, or Lark XML is available, run:

```bash
scripts/interpretation_gate_check.py <draft-or-export>
```

The script supports `--mode triage|deep|research|implementation`. It always checks Source Manifest, the section 0 decision table, four reader questions, value-chain terms, evidence anchors, and pointer-only cells. In `deep` and richer modes it checks the fixed five-section structure, core subsections, Source Depth Check, Citation Verification, High-Signal Anchors, Mini Peer Review Panel, full Critic Mode, writing lens, and claim evidence strength. In `research` mode it also checks Search Manifest and Candidate Screening. It does not replace human judgment about whether the source was actually read deeply enough or whether the critique is substantively correct.
