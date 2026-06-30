# Reading Modes

Choose the lightest mode that satisfies the user's goal. Do not run a deep-read template when the user only needs a relevance decision.

| Mode | Use when | Required output |
|-|-|-|
| `triage` | The user asks whether a paper is worth reading, compares a backlog, or has limited time. | Section 0 only: 5-minute conclusion, four reader questions, compact self-contained 导读决策表, worthiness verdict, and 3-5 evidence anchors. |
| `deep` | The user asks for 论文解读, 精读, detailed analysis, or document/wiki output. | Full 5-section template with source/citation audit and Source Depth Check in section 1, compact 导读决策表, mechanism, High-Signal Anchors, evidence chain, limitations, Mini Peer Review Panel, full Critic Mode, domain lens, writing lens, and completion gate. |
| `research` | The user wants research planning, paper-writing lessons, novelty judgment, reliability critique, or follow-up ideas. | Deep mode plus evidence trace, Search Manifest, Candidate Screening, executable related-work/novelty check when feasible, critic mode, Mini Peer Review, writing lens, knowledge card, and follow-up research questions. |
| `implementation` | The user wants to reproduce or implement the method/system. | Deep mode plus environment assumptions, reproduction checklist, validation metrics, risks, and minimal first experiment. |

Mode rules:
- Always classify the mode before drafting.
- If uncertain, start with `triage`; escalate to `deep` only when the paper passes the reader-decision check or the user explicitly requests depth.
- In `triage`, do not produce sections 1-4 unless needed to make the decision defensible.
- In `deep` and richer modes, the section 0 导读决策表 remains mandatory and excerptable.
- In `deep` and richer modes, keep the fixed five-section structure and core subsections; the script gate blocks missing or reordered structural headings.
- In document-style `deep` and richer modes, include `写作视角：这篇论文写得如何，如果我来写会怎么写`; it is part of the hard gate, not an optional teaching add-on.
- In every single-paper mode, include a Source Manifest so the reader can audit what source and version were used.
- In every document-style single-paper mode, include Citation Verification. Put Source Manifest and Citation Verification in section 1.1 by default, not section 0.
- In `deep` and richer modes, include Source Depth Check. Full text must be used when available; if only abstract/metadata/old notes were used, explicitly mark the interpretation partial and downgrade value, novelty, and evidence claims.
- In `deep` and richer modes, include High-Signal Anchors with at least one mechanism figure/table/equation/algorithm anchor and one evidence/result anchor when the paper provides them. If unavailable, state the source/access limitation.
- In normal `deep` mode, merge claim audit into the 导读 table with `关键证据与可信度`; use a separate Claim Ledger only for audit-heavy, research, or wiki archive outputs.
- Use Mini Peer Review Panel and full Critic Mode in `deep`, not only in research mode. The panel belongs under section 3.4 and must include 方法审稿人、实验证据审稿人、领域落地审稿人、写作审稿人、Devil's Advocate.
- Full Critic Mode in `deep` must include Problem framing attack、Method/action attack、Evidence attack、Generalization attack, and a conclusion adjustment for each attack.
- Use Search Manifest and Candidate Screening only when judging novelty, related work, publishability, or "是否值得跟进".
- Use Search Manifest and Candidate Screening for `research` mode or any strong novelty/reliability/publishability judgment.
- Report the selected mode in the final chat answer or internal completion gate.
