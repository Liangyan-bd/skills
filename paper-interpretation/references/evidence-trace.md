# Evidence Trace

Use this reference when the output must be source-grounded, published as a rich document/wiki, used for research decisions, or checked for hallucination risk.

## Evidence Trace Artifact

Create a compact trace table in the document or a separate `evidence_trace.json` when the workflow uses files.

Minimum schema:

```json
[
  {
    "claim_id": "C1",
    "claim": "Paper-specific claim in the interpretation",
    "claim_type": "problem|method|result|limitation|evaluation",
    "evidence_location": "Section/Figure/Table/Equation/Page/Appendix",
    "evidence_summary": "What the source evidence says",
    "confidence": "high|medium|low",
    "caveat": "What this evidence does not prove"
  }
]
```

Rules:
- Trace every headline claim in the 导读决策表 and every major result or limitation.
- Do not attach evidence to generic background claims unless they affect the reading decision.
- Use short evidence summaries instead of long quotes unless the user asks for direct quotation.
- If the paper source lacks page/section/figure anchors, state the limitation and use the nearest available source marker.
- A claim with no evidence must be marked as `low` confidence or removed from the interpretation.

Recommended document table:

| Claim ID | 论文解读中的主张 | 证据位置 | 证据说明 | 可信度 | 仍不能证明什么 |
|-|-|-|-|-|-|

## Section 0 Claim Ledger

For document-style single-paper interpretation, the five 导读 rows must expose claim strength. Prefer merging this into the compact 导读 table with a `关键证据与可信度` column. Use a separate ledger only for audit-heavy, research, or wiki archive outputs.

| Claim Ledger | claim | source_anchor | evidence_strength | uncertainty |
|-|-|-|-|-|
| 论文问题 | The concrete problem/gap row claim | Section/Figure/Table/experiment/source limitation | high/medium/low | Main uncertainty or scope limit |
| 核心发现 | The headline finding row claim | Strongest result/proof/measurement | high/medium/low | What remains unproven |
| 关键创新 | The novelty/increment row claim | Related-work comparison, method, benchmark, or evidence anchor | high/medium/low | Whether novelty depends on external search |
| 机制判断 | The mechanism explanation row claim | Architecture/equation/ablation/causal evidence | high/medium/low | Inference risk or missing root cause |
| 最大不足 | The primary limitation row claim | Author limitation, missing baseline, weak setting, or critique | high/medium/low | What evidence would change the judgment |

Rules:
- Keep the ledger short enough to sit near section 0, not in an appendix.
- Use the same five row labels as the 导读决策表.
- If a row has no source anchor, mark `evidence_strength = low` and downgrade the row's value/boundary/reading decision.
