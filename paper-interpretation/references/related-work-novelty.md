# Executable Related Work And Novelty Check

Use this when the user asks about innovation, novelty, publishability, related work, paper ranking, or whether the paper is worth following. Do not treat the paper's own "we are first" claim as proven.

## Workflow

1. Extract the paper's novelty claim.
   - Claimed baseline or prior assumption.
   - Claimed delta: problem framing, method, system, evidence, benchmark/data, or theory.
   - Keywords: method names, dataset/benchmark, task, core mechanism, author terms, and competing systems.
2. Run a lightweight external search when feasible.
   - arXiv/ar5iv: exact title, method keywords, benchmark names, and "survey" query.
   - Semantic Scholar or OpenAlex: title match, top cited related works, recent 2-3 year papers.
   - OpenReview: use when venue reviews are relevant or the paper is ML conference work.
   - CrossRef/DBLP/DOI page: use for exact metadata, final venue, and bibliographic disambiguation.
   - GitHub/project page: use when the claim depends on implementation, benchmark, or system adoption.
   - Record a `Search Manifest` so the novelty judgment can be reproduced.
3. Build a candidate list.
   - Keep 5-12 candidates for normal novelty checks.
   - Deduplicate by DOI/arXiv ID/lowercased title.
   - Prefer surveys, strong baselines, highly cited predecessors, and closest recent papers.
4. Screen candidates.
   - Compare only against the specific novelty claim, not the whole field.
   - Mark each candidate as `direct baseline`, `near neighbor`, `background`, or `not comparable`.
   - Keep why each candidate was included or excluded; this prevents cherry-picking.
5. Produce the novelty table and adjust the interpretation.
   - If novelty is weaker than the paper claims, downgrade `关键创新` and `价值判断` in section 0.
   - If no external search was done, explicitly state that novelty is based only on paper-internal related work.

## Search Manifest

Include this table when making novelty, related-work, or publishability judgments.

| Search Manifest | 内容 |
|-|-|
| database | arXiv/ar5iv, Semantic Scholar, OpenAlex, OpenReview, CrossRef/DBLP, GitHub/project page, or paper-internal related work |
| query | Exact search strings or title/citation-network seeds used |
| date | Absolute search date |
| hits_seen | Approximate number of hits inspected, not just returned |
| candidates_kept | Number of candidates compared in the novelty table |
| exclusion_rule | What was excluded and why |
| limitation | What this search cannot establish |

## Candidate Fields

| Field | Meaning |
|-|-|
| title | Candidate paper/system title |
| year | Publication/preprint year |
| venue_or_source | Venue, arXiv, OpenReview, project page, or repository |
| relation_type | direct baseline / near neighbor / background / not comparable |
| why_included | Why this candidate is relevant enough to compare |
| why_excluded | Why it does not fully subsume or disprove the target paper's novelty |
| similarity_dimension | problem framing / mechanism / system / benchmark / evidence / theory / deployment |
| confidence | high / medium / low novelty-screening confidence |
| covered_claim | Which part of the target paper's claim it already covers |
| missing_vs_target | What it does not cover compared with the target paper |
| evidence_anchor | Candidate section, abstract claim, figure, table, or source URL |

## Candidate Screening Table

Use this compact table before the final novelty table when the paper's value depends on novelty.

| Candidate Screening | relation_type | why_included | why_excluded | similarity_dimension | confidence |
|-|-|-|-|-|-|

## Output Table

| 对比对象 / 既有做法 | relation_type | 已有工作覆盖了什么 | 本文真正新增 | 新颖性判断 | 证据缺口 |
|-|-|-|-|-|-|

Novelty labels:
- `new problem framing`
- `new mechanism`
- `new system integration`
- `new evidence/measurement`
- `new benchmark/dataset`
- `incremental packaging`
- `unclear without broader related-work search`

Rules:
- Do not over-search for normal paper interpretation; stop when the novelty decision is stable enough for the user's goal.
- For conference-style evaluation, include baseline competitiveness, ablation quality, evidence sufficiency, and honest limitations.
- If the novelty depends on a benchmark or measurement, judge whether the task/workload/metric is externally valid and hard to game.
- If related-work search was skipped, write: `新颖性判断基于论文自述和文内相关工作，未做外部系统检索`.
- If no external search was feasible, still include a Search Manifest with `database = paper-internal related work` and an explicit limitation.
