# Critic Mode And Devil's Advocate Gate

Use this for every `deep`, `research`, `implementation`, or rich document interpretation. It is also required when the user asks whether the paper is strong, novel, publishable, reliable, worth following, or when the interpretation makes a strong value claim.

## Critic Mode

Run critique after the normal reader-decision spine, not before understanding the paper.

| Stage | Question | Output |
|-|-|-|
| Correctness | Are there internal contradictions, unsupported claims, math/logic/data inconsistencies, or missing definitions? | `correct / questionable / unsupported` with evidence anchors. |
| Evidence quality | Are baselines competitive, ablations meaningful, metrics appropriate, and sample sizes/repetitions adequate? | Evidence strength and weakest link. |
| Novelty | Is the contribution new relative to prior work or mainly packaging/framing? | Use `related-work-novelty.md` when external search is needed. |
| Significance | If the claim is true, what changes for researchers or engineers? | Practical/research value and who should care. |
| Boundary | What should not be inferred from this paper? | Non-claims, external-validity limits, and follow-up evidence. |

## Devil's Advocate Gate

Before reporting `PASS` for `deep`, `research`, or `implementation` outputs, attack the interpretation's own main value claim.

| 反方攻击 | 最强质疑 | 需要什么证据反驳 | 当前证据是否足够 | 结论调整 |
|-|-|-|-|-|
| Problem framing attack | Maybe the problem is already solved or not important. | Prior work, benchmark gaps, real-world failure/cost. | enough / partial / weak | Keep, narrow, or drop value claim. |
| Method/action attack | Maybe the paper's method/action is routine. | Mechanism delta, comparison to baselines, ablation. | enough / partial / weak | Keep, narrow, or drop innovation claim. |
| Evidence attack | Maybe the headline result does not support the claim. | Metrics, setup, variance, controls, confounder checks. | enough / partial / weak | Keep, narrow, or downgrade. |
| Generalization attack | Maybe the result only holds in a narrow setting. | External validity, workload/model/hardware/data diversity. | enough / partial / weak | State boundary clearly. |

Rules:
- Do not soften the critique just because the paper is interesting.
- If the devil's advocate attack cannot be answered with concrete evidence, downgrade the `价值判断` in the 导读决策表.
- In chat outputs, summarize the gate in 2-4 bullets. In rich docs, use the table when the critique materially changes the reading decision.

## Mini Peer Review Panel

Use this for `deep`, `research`, `implementation`, publishability, reliability, strong novelty, or rich wiki outputs. It is a compact multi-perspective review, not a substitute for the main interpretation.

| Mini Peer Review Panel | 主要判断 | 影响 |
|-|-|-|
| 方法审稿人 | Is the method, protocol, proof, or system design technically sound? | What method/mechanism claim should be kept, narrowed, or dropped. |
| 实验证据审稿人 | Do experiments, baselines, metrics, and ablations support the headline claims? | What evidence is strong, weak, or missing. |
| 领域落地审稿人 | Does the result change engineering/research decisions in the target domain? | What should be adopted, reproduced, monitored, or ignored. |
| 写作审稿人 | Does the paper frame the problem, contribution, evidence order, and limitations well? | What readers can learn about writing and what should be rewritten. |
| Devil's Advocate | What is the strongest alternative explanation or overclaim risk? | How the 导读 `价值判断` and reading decision should be downgraded. |

Rules:
- Each panel row should be 1-2 dense sentences, not a generic review paragraph.
- If two reviewers disagree, preserve the disagreement and reflect it in the final reading decision.
- Do not use the panel to add new unsupported claims; every critique must point to source evidence, missing evidence, or related-work uncertainty.
