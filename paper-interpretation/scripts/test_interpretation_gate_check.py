#!/usr/bin/env python3
import unittest

import interpretation_gate_check


VALID_DOC = """# 论文解读：Example

## 0. 导读：先把握重点与不足

| Source Manifest | 内容 |
|-|-|
| source_type | arXiv HTML + PDF |
| source_url | https://arxiv.org/abs/2606.11916 |
| version | v1 |
| accessed_date | 2026-06-30 |
| completeness | full text available; figures checked from PDF |

| Search Manifest | 内容 |
|-|-|
| database | arXiv; Semantic Scholar; OpenAlex; GitHub |
| query | "GPU LLM serving software aging"; "Qwen serving memory leak Triton" |
| date | 2026-06-30 |
| hits_seen | 24 |
| candidates_kept | 6 |
| exclusion_rule | drop unrelated CPU-only memory leak papers and non-serving papers |
| limitation | lightweight novelty check; no full systematic review |

| Citation Verification | 内容 |
|-|-|
| title_verified | yes: arXiv title page |
| authors_verified | yes: arXiv metadata |
| venue_or_version_verified | yes: arXiv v1 |
| doi_or_arxiv_verified | yes: arXiv 2606.11916 |
| code_data_supplement_checked | project/code not visible from source |

| 问题 | 回答 |
|-|-|
| 要解决什么问题 | GPU LLM serving 长时间运行后是否发生 software aging，以及短时 benchmark 为什么看不出来。 |
| 怎么解决 | 用 36h 长跑、跨 deployment stack telemetry 和趋势统计检验定位老化信号。 |
| 关键创新是什么 | 把 software aging 的受控测量协议系统迁移到 GPU LLM serving。 |
| 主要缺点是什么 | 单模型、单 GPU、合成 workload 和单次 run 限制结论外推。 |

| 导读项 | 要点结论 | 关键支撑 | 价值判断 | 阅读决策 |
|-|-|-|-|-|
| 论文问题 | 短时 benchmark 无法回答系统长时间运行后的 software aging 问题。 | Introduction 和 Methodology 使用 36h run、L40S、Qwen2.5 workload 作为依据。 | 问题压力：这影响发布验收、SRE 稳定性和容量规划，已有 peak metrics 不足。 | 做 GPU serving 平台的人应深读，只看模型算法的人可略读。 |
| 核心发现 | 用户侧延迟稳定，但 process-private memory 呈现持续增长。 | Table IV 报告 E2 约 157 KB/h，Figure 2 显示阶梯式内存增长。 | 证据增量：黑盒 SLO 稳定不代表系统没有老化，监控要看 host process。 | 结果足够支撑阅读证据章节。 |
| 关键创新 | 贡献是受控长跑测量协议和跨层 telemetry，而不是新推理算法。 | 六个 36h run、V0/V1 standalone/Triton ablation 和统计检验支撑。 | 论文动作：把泄漏怀疑转成可复现、可比较、可审计的测量框架。 | 值得为 soak test 和研究定位深读。 |
| 机制判断 | 老化更可能来自 serving runtime / hosting layer 的 host 内存路径。 | Triton+V0 增长最明显，device memory 和 client metrics 相对稳定。 | 读者收益：排查入口应从 VRAM 扩展到 process memory、runtime wrapper 和 engine version。 | 可作为复现实验和监控设计假设。 |
| 最大不足 | 单模型、单 GPU、合成 workload 和单次 run 限制外部有效性。 | 论文实验限定 Qwen2.5-7B-Instruct、NVIDIA L40S 和固定 Poisson workload。 | 边界条件：不能直接当生产容量预测，必须在真实 trace 和自家版本复测。 | 仍值得读，但采用前必须复验。 |

| Claim Ledger | claim | source_anchor | evidence_strength | uncertainty |
|-|-|-|-|-|
| 论文问题 | 长时间 serving 老化不能由短时 benchmark 判断。 | Introduction; Methodology 36h run | medium | 单模型和单硬件限制外推 |
| 核心发现 | process-private memory 呈现持续增长。 | Table IV; Figure 2 | strong | 需要更多重复 run |
| 关键创新 | 增量是 GPU LLM serving 的受控老化测量协议。 | Methodology; Experiment matrix | medium | novelty 依赖轻量 related-work search |
| 机制判断 | 老化更可能来自 host runtime path。 | Triton+V0 ablation; device memory stable | medium | 未定位具体代码 root cause |
| 最大不足 | 外部有效性有限。 | Threats to Validity | strong | 真实 trace 未覆盖 |

| Candidate Screening | relation_type | why_included | why_excluded | similarity_dimension | confidence |
|-|-|-|-|-|
| Software aging in cloud services | near neighbor | 同样研究长期运行退化 | 不是 GPU LLM serving | problem framing | medium |
| vLLM production serving benchmarks | direct baseline | 覆盖 serving performance baseline | 不覆盖 36h aging protocol | system/workload | medium |

| Mini Peer Review Panel | 主要判断 | 影响 |
|-|-|
| 方法审稿人 | 测量协议清楚但 root cause 还不够。 | 方法可复用，机制结论需降级。 |
| 实验证据审稿人 | Table IV 和 Figure 2 支撑内存增长。 | 证据足以提醒风险，不足以预测生产容量。 |
| 领域落地审稿人 | 对 GPU serving soak test 有直接启发。 | 采用前必须换真实 trace 复测。 |
| 写作审稿人 | framing 清晰，但 novelty 容易被过度表述。 | 导读应把创新限定为测量协议。 |
| Devil's Advocate | 可能只是特定 stack bug，不是普遍 aging。 | 价值判断保持中等，不上升为普遍结论。 |

## 1. 论文定位：问题、增量与背景

### 1.1 基本信息

### 1.2 问题：为什么需要这篇论文

### 1.3 一句话增量

## 2. 方法机制：Example 如何工作

### 2.1 核心机制总览

### 2.2 关键概念与对象模型

### 2.3 数学或系统框架

### 2.4 关键组件拆解

### 2.5 运行时 / 算法流程

### 2.6 设计取舍、复杂度与失败模式

## 3. 证据与评价：贡献、局限与可信度

### 3.1 证据与结果

### 3.2 真正的贡献

### 3.3 局限与问题

### 3.4 博导式评价

## 4. 工程落地与后续问题

### 4.1 对我 / 团队有什么用

### 4.2 领域视角

### 4.3 复现 / 落地清单

### 4.4 值得追问的问题

### 4.5 写作视角：这篇论文写得如何，如果我来写会怎么写

这篇论文写得如何：问题开口具体，能把系统现象拆成可测量研究问题。
如果我来写：我会更早给出 RQ 表，把贡献、结果和边界分开。

### 4.6 一句话总结
"""

COMPACT_DEEP_DOC = """# 论文解读：Example

## 0. 导读：先把握重点与不足

| Source Manifest | 内容 |
|-|-|
| source_type | arXiv HTML + PDF |
| source_url | https://arxiv.org/abs/2606.11916 |
| version | v1 |
| accessed_date | 2026-06-30 |
| completeness | full text available; figures checked from PDF |

| Citation Verification | 内容 |
|-|-|
| title_verified | yes: arXiv title page |
| authors_verified | yes: arXiv metadata |
| venue_or_version_verified | yes: arXiv v1 |
| doi_or_arxiv_verified | yes: arXiv 2606.11916 |
| code_data_supplement_checked | project/code not visible from source |

| 问题 | 回答 |
|-|-|
| 要解决什么问题 | GPU LLM serving 长时间运行后是否发生 software aging，以及短时 benchmark 为什么看不出来。 |
| 怎么解决 | 用 36h 长跑、跨 deployment stack telemetry 和趋势统计检验定位老化信号。 |
| 关键创新是什么 | 把 software aging 的受控测量协议系统迁移到 GPU LLM serving。 |
| 主要缺点是什么 | 单模型、单 GPU、合成 workload 和单次 run 限制结论外推。 |

| 导读项 | 一句话结论 | 关键证据与可信度 | 价值 / 边界 / 阅读决策 |
|-|-|-|-|
| 论文问题 | 短时 benchmark 无法回答系统长时间运行后的 software aging 问题。 | high：Introduction 和 Methodology 使用 36h run、L40S、Qwen2.5 workload 作为依据。 | 问题压力：这影响发布验收、SRE 稳定性和容量规划；做 GPU serving 平台的人应深读。 |
| 核心发现 | 用户侧延迟稳定，但 process-private memory 呈现持续增长。 | high：Table IV 报告 E2 约 157 KB/h，Figure 2 显示阶梯式内存增长。 | 证据增量：黑盒 SLO 稳定不代表系统没有老化，结果足够支撑阅读证据章节。 |
| 关键创新 | 贡献是受控长跑测量协议和跨层 telemetry，而不是新推理算法。 | medium：六个 36h run、V0/V1 standalone/Triton ablation 和统计检验支撑。 | 论文动作：把泄漏怀疑转成可复现测量框架；值得为 soak test 深读。 |
| 机制判断 | 老化更可能来自 serving runtime / hosting layer 的 host 内存路径。 | medium：Triton+V0 增长最明显，device memory 和 client metrics 相对稳定。 | 读者收益：排查入口应扩展到 process memory、runtime wrapper 和 engine version。 |
| 最大不足 | 单模型、单 GPU、合成 workload 和单次 run 限制外部有效性。 | high：Threats to Validity 限定 Qwen2.5-7B-Instruct、NVIDIA L40S 和固定 Poisson workload。 | 边界条件：不能直接当生产容量预测，采用前必须复验。 |

## 1. 论文定位：问题、增量与背景

### 1.1 基本信息

### 1.2 问题：为什么需要这篇论文

### 1.3 一句话增量

## 2. 方法机制：Example 如何工作

### 2.1 核心机制总览

### 2.2 关键概念与对象模型

### 2.3 数学或系统框架

### 2.4 关键组件拆解

### 2.5 运行时 / 算法流程

### 2.6 设计取舍、复杂度与失败模式

## 3. 证据与评价：贡献、局限与可信度

### 3.1 证据与结果

### 3.2 真正的贡献

### 3.3 局限与问题

### 3.4 博导式评价

## 4. 工程落地与后续问题

### 4.1 对我 / 团队有什么用

### 4.2 领域视角

### 4.3 复现 / 落地清单

### 4.4 值得追问的问题

### 4.5 写作视角：这篇论文写得如何，如果我来写会怎么写

这篇论文写得如何：问题开口具体，能把系统现象拆成可测量研究问题。
如果我来写：我会更早给出 RQ 表，把贡献、结果和边界分开。

### 4.6 一句话总结
"""


class InterpretationGateCheckTest(unittest.TestCase):
    def test_valid_doc_passes(self):
        result = interpretation_gate_check.check_text(VALID_DOC)

        self.assertTrue(result.passed, result.messages)

    def test_research_mode_valid_doc_passes(self):
        result = interpretation_gate_check.check_text(VALID_DOC, mode="research")

        self.assertTrue(result.passed, result.messages)

    def test_compact_deep_doc_passes_without_research_audit_tables(self):
        result = interpretation_gate_check.check_text(COMPACT_DEEP_DOC, mode="deep")

        self.assertTrue(result.passed, result.messages)

    def test_claim_ledger_before_intro_table_passes(self):
        claim_ledger_start = VALID_DOC.index("| Claim Ledger |")
        candidate_start = VALID_DOC.index("| Candidate Screening |")
        claim_ledger = VALID_DOC[claim_ledger_start:candidate_start]
        without_claim_ledger = VALID_DOC[:claim_ledger_start] + VALID_DOC[candidate_start:]
        intro_start = without_claim_ledger.index("| 导读项 |")
        text = without_claim_ledger[:intro_start] + claim_ledger + without_claim_ledger[intro_start:]

        result = interpretation_gate_check.check_text(text)

        self.assertTrue(result.passed, result.messages)

    def test_lark_xml_table_passes(self):
        xml = """<fragment><h1><p>0. 导读：先把握重点与不足</p></h1><table><thead><tr><th><p>Source Manifest</p></th><th><p>内容</p></th></tr></thead><tbody>
<tr><td><p>source_type</p></td><td><p>arXiv HTML + PDF</p></td></tr>
<tr><td><p>source_url</p></td><td><p>https://arxiv.org/abs/2606.11916</p></td></tr>
<tr><td><p>version</p></td><td><p>v1</p></td></tr>
<tr><td><p>accessed_date</p></td><td><p>2026-06-30</p></td></tr>
<tr><td><p>completeness</p></td><td><p>full text available; figures checked from PDF</p></td></tr>
</tbody></table><table><thead><tr><th><p>问题</p></th><th><p>回答</p></th></tr></thead><tbody>
<tr><td><p>要解决什么问题</p></td><td><p>GPU LLM serving 长时间运行后是否发生 software aging。</p></td></tr>
<tr><td><p>怎么解决</p></td><td><p>用 36h 长跑和跨 deployment stack telemetry 定位老化信号。</p></td></tr>
<tr><td><p>关键创新是什么</p></td><td><p>把 software aging 的受控测量协议迁移到 GPU LLM serving。</p></td></tr>
<tr><td><p>主要缺点是什么</p></td><td><p>单模型、单 GPU、合成 workload 和单次 run 限制外推。</p></td></tr>
</tbody></table><table><thead><tr><th><p>导读项</p></th><th><p>要点结论</p></th><th><p>关键支撑</p></th><th><p>价值判断</p></th><th><p>阅读决策</p></th></tr></thead><tbody>
<tr><td><p><b>论文问题</b></p></td><td><p>短时 benchmark 无法回答系统长时间运行后的 software aging 问题。</p></td><td><p>Introduction 和 Methodology 使用 36h run、L40S、Qwen2.5 workload 作为依据。</p></td><td><p><b>问题压力：</b>这影响发布验收、SRE 稳定性和容量规划。</p></td><td><p>做 GPU serving 平台的人应深读。</p></td></tr>
<tr><td><p><b>核心发现</b></p></td><td><p>用户侧延迟稳定，但 process-private memory 呈现持续增长。</p></td><td><p>Table IV 报告 E2 约 157 KB/h，Figure 2 显示阶梯式内存增长。</p></td><td><p><b>证据增量：</b>黑盒 SLO 稳定不代表系统没有老化。</p></td><td><p>结果足够支撑阅读证据章节。</p></td></tr>
<tr><td><p><b>关键创新</b></p></td><td><p>贡献是受控长跑测量协议和跨层 telemetry。</p></td><td><p>六个 36h run、V0/V1 standalone/Triton ablation 和统计检验支撑。</p></td><td><p><b>论文动作：</b>把泄漏怀疑转成可复现测量框架。</p></td><td><p>值得为 soak test 和研究定位深读。</p></td></tr>
<tr><td><p><b>机制判断</b></p></td><td><p>老化更可能来自 serving runtime / hosting layer 的 host 内存路径。</p></td><td><p>Triton+V0 增长最明显，device memory 和 client metrics 相对稳定。</p></td><td><p><b>读者收益：</b>排查入口应扩展到 process memory 和 runtime wrapper。</p></td><td><p>可作为复现实验和监控设计假设。</p></td></tr>
<tr><td><p><b>最大不足</b></p></td><td><p>单模型、单 GPU、合成 workload 和单次 run 限制外部有效性。</p></td><td><p>Threats to Validity 限定 Qwen2.5-7B-Instruct、NVIDIA L40S 和固定 Poisson workload。</p></td><td><p><b>边界条件：</b>不能直接当生产容量预测。</p></td><td><p>上线采用前必须复验真实 trace。</p></td></tr>
</tbody></table><table><thead><tr><th><p>Search Manifest</p></th><th><p>内容</p></th></tr></thead><tbody>
<tr><td><p>database</p></td><td><p>arXiv; Semantic Scholar; OpenAlex; GitHub</p></td></tr>
<tr><td><p>query</p></td><td><p>GPU LLM serving software aging</p></td></tr>
<tr><td><p>date</p></td><td><p>2026-06-30</p></td></tr>
<tr><td><p>hits_seen</p></td><td><p>24</p></td></tr>
<tr><td><p>candidates_kept</p></td><td><p>6</p></td></tr>
<tr><td><p>exclusion_rule</p></td><td><p>drop unrelated papers</p></td></tr>
<tr><td><p>limitation</p></td><td><p>lightweight novelty check</p></td></tr>
</tbody></table><table><thead><tr><th><p>Citation Verification</p></th><th><p>内容</p></th></tr></thead><tbody>
<tr><td><p>title_verified</p></td><td><p>yes</p></td></tr>
<tr><td><p>authors_verified</p></td><td><p>yes</p></td></tr>
<tr><td><p>venue_or_version_verified</p></td><td><p>yes</p></td></tr>
<tr><td><p>doi_or_arxiv_verified</p></td><td><p>yes</p></td></tr>
<tr><td><p>code_data_supplement_checked</p></td><td><p>not visible</p></td></tr>
</tbody></table><table><thead><tr><th><p>Claim Ledger</p></th><th><p>claim</p></th><th><p>source_anchor</p></th><th><p>evidence_strength</p></th><th><p>uncertainty</p></th></tr></thead><tbody>
<tr><td><p>论文问题</p></td><td><p>long benchmark gap</p></td><td><p>Introduction</p></td><td><p>medium</p></td><td><p>limited stack</p></td></tr>
<tr><td><p>核心发现</p></td><td><p>memory growth</p></td><td><p>Table IV</p></td><td><p>strong</p></td><td><p>more runs needed</p></td></tr>
</tbody></table><table><thead><tr><th><p>Candidate Screening</p></th><th><p>relation_type</p></th><th><p>why_included</p></th><th><p>why_excluded</p></th><th><p>similarity_dimension</p></th><th><p>confidence</p></th></tr></thead><tbody>
<tr><td><p>Software aging in cloud services</p></td><td><p>near neighbor</p></td><td><p>same problem framing</p></td><td><p>not LLM serving</p></td><td><p>problem framing</p></td><td><p>medium</p></td></tr>
</tbody></table><table><thead><tr><th><p>Mini Peer Review Panel</p></th><th><p>主要判断</p></th><th><p>影响</p></th></tr></thead><tbody>
<tr><td><p>方法审稿人</p></td><td><p>protocol clear</p></td><td><p>root cause downgraded</p></td></tr>
<tr><td><p>实验证据审稿人</p></td><td><p>Table IV supports growth</p></td><td><p>capacity prediction limited</p></td></tr>
<tr><td><p>领域落地审稿人</p></td><td><p>soak test useful</p></td><td><p>need real traces</p></td></tr>
<tr><td><p>写作审稿人</p></td><td><p>framing clear</p></td><td><p>avoid overclaiming</p></td></tr>
<tr><td><p>Devil's Advocate</p></td><td><p>could be stack-specific bug</p></td><td><p>value stays medium</p></td></tr>
</tbody></table><h1><p>1. 论文定位：问题、增量与背景</p></h1><h2><p>1.1 基本信息</p></h2><h2><p>1.2 问题：为什么需要这篇论文</p></h2><h2><p>1.3 一句话增量</p></h2><h1><p>2. 方法机制：Example 如何工作</p></h1><h2><p>2.1 核心机制总览</p></h2><h2><p>2.2 关键概念与对象模型</p></h2><h2><p>2.3 数学或系统框架</p></h2><h2><p>2.4 关键组件拆解</p></h2><h2><p>2.5 运行时 / 算法流程</p></h2><h2><p>2.6 设计取舍、复杂度与失败模式</p></h2><h1><p>3. 证据与评价：贡献、局限与可信度</p></h1><h2><p>3.1 证据与结果</p></h2><h2><p>3.2 真正的贡献</p></h2><h2><p>3.3 局限与问题</p></h2><h2><p>3.4 博导式评价</p></h2><h1><p>4. 工程落地与后续问题</p></h1><h2><p>4.1 对我 / 团队有什么用</p></h2><h2><p>4.2 领域视角</p></h2><h2><p>4.3 复现 / 落地清单</p></h2><h2><p>4.4 值得追问的问题</p></h2><h2><p>4.5 写作视角：这篇论文写得如何，如果我来写会怎么写</p></h2><p>这篇论文写得如何：问题开口具体，能把系统现象拆成可测量研究问题。</p><p>如果我来写：我会更早给出 RQ 表，把贡献、结果和边界分开。</p><h2><p>4.6 一句话总结</p></h2></fragment>"""

        result = interpretation_gate_check.check_text(xml)

        self.assertTrue(result.passed, result.messages)

    def test_missing_value_column_fails(self):
        text = VALID_DOC.replace("价值判断 |", "读者结论 |")

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("价值判断" in msg for msg in result.messages))

    def test_pointer_only_cell_fails(self):
        text = VALID_DOC.replace(
            "Introduction 和 Methodology 使用 36h run、L40S、Qwen2.5 workload 作为依据。",
            "详见实验。",
        )

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("pointer-only" in msg for msg in result.messages))

    def test_missing_reader_questions_fails(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("要解决什么问题", "怎么解决", "关键创新是什么", "主要缺点是什么"))
        )

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("reader question" in msg for msg in result.messages))

    def test_missing_source_manifest_fails(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Source Manifest", "source_type", "source_url", "version", "accessed_date", "completeness"))
        )

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("source manifest" in msg for msg in result.messages))

    def test_missing_search_manifest_allowed_in_deep_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Search Manifest", "database", "query", "hits_seen", "candidates_kept", "exclusion_rule"))
        )

        result = interpretation_gate_check.check_text(text, mode="deep")

        self.assertTrue(result.passed, result.messages)

    def test_missing_search_manifest_fails_in_research_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Search Manifest", "database", "query", "hits_seen", "candidates_kept", "exclusion_rule"))
        )

        result = interpretation_gate_check.check_text(text, mode="research")

        self.assertFalse(result.passed)
        self.assertTrue(any("search manifest" in msg for msg in result.messages))

    def test_missing_citation_verification_fails(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Citation Verification", "title_verified", "authors_verified", "doi_or_arxiv_verified"))
        )

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("citation verification" in msg for msg in result.messages))

    def test_missing_writing_lens_fails_in_deep_mode(self):
        start = COMPACT_DEEP_DOC.index("## 4. 工程落地与后续问题")
        text = COMPACT_DEEP_DOC[:start]

        result = interpretation_gate_check.check_text(text, mode="deep")

        self.assertFalse(result.passed)
        self.assertTrue(any("writing lens" in msg for msg in result.messages))

    def test_missing_deep_structure_fails_in_deep_mode(self):
        text = COMPACT_DEEP_DOC.replace("## 2. 方法机制：Example 如何工作\n", "")

        result = interpretation_gate_check.check_text(text, mode="deep")

        self.assertFalse(result.passed)
        self.assertTrue(any("deep structure" in msg for msg in result.messages))

    def test_missing_claim_ledger_fails_when_no_compact_confidence_column(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Claim Ledger", "source_anchor", "evidence_strength", "uncertainty"))
        )

        result = interpretation_gate_check.check_text(text)

        self.assertFalse(result.passed)
        self.assertTrue(any("claim ledger" in msg for msg in result.messages))

    def test_missing_candidate_screening_allowed_in_deep_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Candidate Screening", "relation_type", "why_included", "why_excluded", "similarity_dimension", "confidence"))
        )

        result = interpretation_gate_check.check_text(text, mode="deep")

        self.assertTrue(result.passed, result.messages)

    def test_missing_candidate_screening_fails_in_research_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Candidate Screening", "relation_type", "why_included", "why_excluded", "similarity_dimension", "confidence"))
        )

        result = interpretation_gate_check.check_text(text, mode="research")

        self.assertFalse(result.passed)
        self.assertTrue(any("candidate screening" in msg for msg in result.messages))

    def test_missing_mini_peer_review_panel_allowed_in_deep_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Mini Peer Review Panel", "方法审稿人", "实验证据审稿人", "领域落地审稿人", "写作审稿人", "Devil's Advocate"))
        )

        result = interpretation_gate_check.check_text(text, mode="deep")

        self.assertTrue(result.passed, result.messages)

    def test_missing_mini_peer_review_panel_fails_in_research_mode(self):
        text = "\n".join(
            line
            for line in VALID_DOC.splitlines()
            if not any(label in line for label in ("Mini Peer Review Panel", "方法审稿人", "实验证据审稿人", "领域落地审稿人", "写作审稿人", "Devil's Advocate"))
        )

        result = interpretation_gate_check.check_text(text, mode="research")

        self.assertFalse(result.passed)
        self.assertTrue(any("mini peer review" in msg for msg in result.messages))


if __name__ == "__main__":
    unittest.main()
