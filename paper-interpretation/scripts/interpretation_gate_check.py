#!/usr/bin/env python3
"""Lightweight gate checker for paper interpretation drafts.

This script catches structural failures in Markdown/text/Lark XML. It does not
replace the human/agent judgment required by the SKILL.md quality gate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


REQUIRED_ROWS = ["论文问题", "核心发现", "关键创新", "机制判断", "最大不足"]
LEGACY_REQUIRED_COLUMNS = ["导读项", "要点结论", "关键支撑", "价值判断", "阅读决策"]
COMPACT_REQUIRED_COLUMNS = ["导读项", "一句话结论", "关键证据与可信度", "价值 / 边界 / 阅读决策"]
VALUE_CHAIN_TERMS = ["问题压力", "论文动作", "证据增量", "读者收益", "边界条件"]
READER_QUESTIONS = ["要解决什么问题", "怎么解决", "关键创新是什么", "主要缺点是什么"]
SOURCE_MANIFEST_TERMS = ["Source Manifest", "source_type", "source_url", "version", "accessed_date", "completeness"]
SOURCE_DEPTH_CHECK_TERMS = [
    "Source Depth Check",
    "primary_source_used",
    "full_text_status",
    "fallback_reason",
    "unsupported_claims_policy",
]
SEARCH_MANIFEST_TERMS = ["Search Manifest", "database", "query", "date", "hits_seen", "candidates_kept", "exclusion_rule", "limitation"]
CITATION_VERIFICATION_TERMS = [
    "Citation Verification",
    "title_verified",
    "authors_verified",
    "venue_or_version_verified",
    "doi_or_arxiv_verified",
    "code_data_supplement_checked",
]
CLAIM_LEDGER_TERMS = ["Claim Ledger", "source_anchor", "evidence_strength", "uncertainty"]
CANDIDATE_SCREENING_TERMS = [
    "Candidate Screening",
    "relation_type",
    "why_included",
    "why_excluded",
    "similarity_dimension",
    "confidence",
]
MINI_PEER_REVIEW_TERMS = [
    "Mini Peer Review Panel",
    "方法审稿人",
    "实验证据审稿人",
    "领域落地审稿人",
    "写作审稿人",
    "Devil's Advocate",
]
CRITIC_MODE_TERMS = [
    "Critic Mode",
    "Problem framing attack",
    "Method/action attack",
    "Evidence attack",
    "Generalization attack",
    "结论调整",
]
HIGH_SIGNAL_ANCHOR_TERMS = [
    "High-Signal Anchors",
    "机制锚点",
    "证据锚点",
]
WRITING_LENS_TERMS = ["写作视角", "这篇论文写得如何", "如果我来写"]
DEEP_TOP_LEVEL_PREFIXES = [
    "0. 导读：先把握重点与不足",
    "1. 论文定位：问题、增量与背景",
    "2. 方法机制：",
    "3. 证据与评价：贡献、局限与可信度",
    "4. 工程落地与后续问题",
]
DEEP_SUBSECTION_PREFIXES = [
    "1.1 基本信息",
    "1.2 问题：为什么需要这篇论文",
    "1.3 一句话增量",
    "2.1 核心机制总览",
    "2.2 关键概念与对象模型",
    "2.3 ",
    "2.4 关键组件拆解",
    "2.5 ",
    "2.6 ",
    "3.1 证据与结果",
    "3.2 真正的贡献",
    "3.3 局限与问题",
    "3.4 博导式评价",
    "4.1 ",
    "4.2 ",
    "4.3 复现 / 落地清单",
    "4.4 值得追问的问题",
    "4.5 写作视角",
    "4.6 一句话总结",
]
SUPPORTED_MODES = {"triage", "deep", "research", "implementation"}
POINTER_ONLY = re.compile(r"^\s*(见|详见|参考|参见|see)\s*(第?\s*\d+|section|figure|fig\.|table|表|图|实验|后文|下文).{0,12}$", re.I)
EVIDENCE_HINTS = re.compile(
    r"(section|figure|fig\.|table|equation|eq\.|appendix|introduction|methodology|"
    r"图\s*\d+|表\s*\d+|第\s*\d+\s*节|实验|消融|ablation|baseline|benchmark|"
    r"dataset|workload|metric|模型|GPU|CPU|L40S|A100|H100|36h|KB/h|ms|%)",
    re.I,
)


@dataclass
class GateResult:
    passed: bool
    messages: list[str]


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def _is_separator(line: str) -> bool:
    cells = _split_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{2,}:?", cell.strip()) for cell in cells)


def _extract_tables(text: str) -> list[list[list[str]]]:
    tables: list[list[list[str]]] = []
    current: list[list[str]] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("|") and line.endswith("|"):
            if not _is_separator(line):
                current.append(_split_row(line))
            continue
        if current:
            tables.append(current)
            current = []

    if current:
        tables.append(current)

    return tables


def _element_text(element: ET.Element) -> str:
    return "".join(element.itertext()).strip()


def _extract_xml_tables(text: str) -> list[list[list[str]]]:
    if "<table" not in text:
        return []

    try:
        root = ET.fromstring(f"<root>{text}</root>")
    except ET.ParseError:
        return []

    tables: list[list[list[str]]] = []
    for table in root.iter("table"):
        rows: list[list[str]] = []
        for tr in table.iter("tr"):
            cells = [_element_text(cell) for cell in list(tr) if cell.tag in {"th", "td"}]
            if cells:
                rows.append(cells)
        if rows:
            tables.append(rows)
    return tables


def _extract_headings(text: str) -> list[tuple[int, str]]:
    headings: list[tuple[int, str]] = []

    for raw_line in text.splitlines():
        match = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$", raw_line)
        if match:
            headings.append((len(match.group(1)), re.sub(r"<[^>]+>", "", match.group(2)).strip()))

    if "<h" not in text:
        return headings

    try:
        root = ET.fromstring(f"<root>{text}</root>")
    except ET.ParseError:
        return headings

    for element in root.iter():
        if re.fullmatch(r"h[1-6]", element.tag):
            headings.append((int(element.tag[1]), _element_text(element)))
    return headings


def _matches_prefix(text: str, prefix: str) -> bool:
    return text.startswith(prefix)


def _check_deep_structure(text: str) -> list[str]:
    headings = _extract_headings(text)
    heading_texts = [heading for _, heading in headings]
    messages: list[str] = []

    top_level = [heading for heading in heading_texts if re.match(r"^[0-4]\.\s", heading)]
    matched_top: list[str] = []
    cursor = 0
    for prefix in DEEP_TOP_LEVEL_PREFIXES:
        for idx in range(cursor, len(top_level)):
            if _matches_prefix(top_level[idx], prefix):
                matched_top.append(top_level[idx])
                cursor = idx + 1
                break
        else:
            messages.append(f"missing deep structure heading: {prefix}")

    if len(top_level) != len(DEEP_TOP_LEVEL_PREFIXES):
        messages.append(f"deep structure top-level heading count should be 5, got {len(top_level)}")

    cursor = 0
    for prefix in DEEP_SUBSECTION_PREFIXES:
        for idx in range(cursor, len(heading_texts)):
            if _matches_prefix(heading_texts[idx], prefix):
                cursor = idx + 1
                break
        else:
            messages.append(f"missing deep structure subsection: {prefix}")

    return messages


def _is_intro_header(header: list[str]) -> bool:
    return all(col in header for col in LEGACY_REQUIRED_COLUMNS) or all(col in header for col in COMPACT_REQUIRED_COLUMNS)


def _required_columns_for(header: list[str]) -> list[str]:
    if all(col in header for col in COMPACT_REQUIRED_COLUMNS):
        return COMPACT_REQUIRED_COLUMNS
    return LEGACY_REQUIRED_COLUMNS


def _find_intro_table(tables: list[list[list[str]]]) -> list[list[str]] | None:
    for table in tables:
        flat = "\n".join(" ".join(row) for row in table)
        header = table[0] if table else []
        if all(label in flat for label in REQUIRED_ROWS) and _is_intro_header(header):
            return table
    return None


def _find_intro_row_table(tables: list[list[list[str]]]) -> list[list[str]] | None:
    for table in tables:
        flat = "\n".join(" ".join(row) for row in table)
        header = table[0] if table else []
        if all(label in flat for label in REQUIRED_ROWS) and any(col in header for col in LEGACY_REQUIRED_COLUMNS + COMPACT_REQUIRED_COLUMNS):
            return table
    return None


def _row_map(table: list[list[str]]) -> tuple[list[str], dict[str, list[str]]]:
    header = table[0]
    rows: dict[str, list[str]] = {}
    for row in table[1:]:
        if not row:
            continue
        label = row[0].strip()
        if label in REQUIRED_ROWS:
            rows[label] = row
    return header, rows


def _cell(row: list[str], header: list[str], name: str) -> str:
    try:
        idx = header.index(name)
    except ValueError:
        return ""
    if idx >= len(row):
        return ""
    return row[idx].strip()


def _has_claim_ledger_or_compact_confidence(text: str, header: list[str]) -> bool:
    has_ledger = all(term in text for term in CLAIM_LEDGER_TERMS)
    has_compact_confidence = "关键证据与可信度" in header
    return has_ledger or has_compact_confidence


def check_text(text: str, mode: str = "deep") -> GateResult:
    if mode not in SUPPORTED_MODES:
        return GateResult(False, [f"unsupported mode: {mode}"])

    messages: list[str] = []
    tables = _extract_tables(text) + _extract_xml_tables(text)
    table = _find_intro_table(tables) or _find_intro_row_table(tables)

    for question in READER_QUESTIONS:
        if question not in text:
            messages.append(f"missing reader question answer: {question}")

    for term in SOURCE_MANIFEST_TERMS:
        if term not in text:
            messages.append(f"missing source manifest field: {term}")

    if mode in {"deep", "research", "implementation"}:
        messages.extend(_check_deep_structure(text))
        for term in SOURCE_DEPTH_CHECK_TERMS:
            if term not in text:
                messages.append(f"missing source depth check field: {term}")
        if re.search(r"full_text_status\s*[:：]\s*(abstract_only|source_unavailable|previous_summary_only)", text, re.I):
            messages.append("deep source depth insufficient: full_text_status cannot be abstract_only/source_unavailable/previous_summary_only")
        for term in CITATION_VERIFICATION_TERMS:
            if term not in text:
                messages.append(f"missing citation verification field: {term}")
        for term in HIGH_SIGNAL_ANCHOR_TERMS:
            if term not in text:
                messages.append(f"missing high-signal anchor field: {term}")
        for term in MINI_PEER_REVIEW_TERMS:
            if term not in text:
                messages.append(f"missing mini peer review field: {term}")
        for term in CRITIC_MODE_TERMS:
            if term not in text:
                messages.append(f"missing critic mode field: {term}")
        for term in WRITING_LENS_TERMS:
            if term not in text:
                messages.append(f"missing writing lens field: {term}")

    if mode == "research":
        for term in SEARCH_MANIFEST_TERMS:
            if term not in text:
                messages.append(f"missing search manifest field: {term}")

        for term in CANDIDATE_SCREENING_TERMS:
            if term not in text:
                messages.append(f"missing candidate screening field: {term}")

    if table is None:
        messages.append("missing intro decision table with required five rows")
        return GateResult(False, messages)

    header, rows = _row_map(table)
    required_columns = _required_columns_for(header)
    for col in required_columns:
        if col not in header:
            messages.append(f"missing required column: {col}")

    for label in REQUIRED_ROWS:
        if label not in rows:
            messages.append(f"missing required row: {label}")

    if messages:
        return GateResult(False, messages)

    if mode in {"deep", "research", "implementation"} and not _has_claim_ledger_or_compact_confidence(text, header):
        messages.append("missing claim ledger or compact evidence/confidence column")

    table_text = "\n".join(" | ".join(row) for row in table)
    for term in VALUE_CHAIN_TERMS:
        if term not in table_text:
            messages.append(f"missing value-chain term in intro table: {term}")

    for label, row in rows.items():
        for col in required_columns[1:]:
            content = _cell(row, header, col)
            if len(content) < 12:
                messages.append(f"cell too thin: {label}/{col}")
            if POINTER_ONLY.search(content):
                messages.append(f"pointer-only cell: {label}/{col}")

        evidence = _cell(row, header, "关键支撑") or _cell(row, header, "关键证据与可信度")
        if not EVIDENCE_HINTS.search(evidence):
            messages.append(f"missing concrete evidence anchor: {label}/关键支撑")

    return GateResult(not messages, messages)


def _read_input(path: str | None) -> str:
    if path and path != "-":
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check paper interpretation quality-gate basics.")
    parser.add_argument("path", nargs="?", default="-", help="Markdown/text/Lark XML file path, or stdin when omitted")
    parser.add_argument("--mode", choices=sorted(SUPPORTED_MODES), default="deep", help="Output mode to check")
    parser.add_argument("--json", action="store_true", help="Emit JSON result")
    args = parser.parse_args(argv)

    result = check_text(_read_input(args.path), mode=args.mode)
    if args.json:
        print(json.dumps({"passed": result.passed, "messages": result.messages}, ensure_ascii=False, indent=2))
    elif result.passed:
        print("门禁检查结果：PASS")
    else:
        print("门禁检查结果：BLOCKED")
        for message in result.messages:
            print(f"- {message}")
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
