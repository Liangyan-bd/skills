# Source Ingestion And Manifest

Use this before interpreting any paper. The goal is to make the interpretation reproducible: readers should know exactly what source was read, whether it was complete, and which version figures/tables came from.

## Source Priority

| Priority | Source | Use when | Notes |
|-|-|-|-|
| 1 | arXiv TeX source (`/src/<id>`) | arXiv paper has source available and formulas/tables matter. | Best for section structure, equations, macros, tables, and figure references. |
| 2 | ar5iv / arXiv HTML | TeX source is unavailable or too costly to parse. | Often preserves sections, math, and tables better than raw PDF text. |
| 3 | Official PDF | Figures, captions, layout, final published version, or no HTML/source. | Use for visual anchors and page/table/figure checks. |
| 4 | DOI/publisher/official project page | Need metadata, final venue, supplement, code, dataset, or appendices. | Prefer official sources over reposts. |
| 5 | User-provided excerpt or previous summary | Only source available or user asks to edit an existing interpretation. | State partial-source limitation and avoid unsupported claims. |

## Source Manifest

Add this block near the start of section 0 or section 1.1. For Lark/wiki docs, a compact table is enough.

| Source Manifest | 内容 |
|-|-|
| source_type | arXiv TeX / arXiv HTML / PDF / DOI page / project page / user excerpt / previous summary |
| source_url | URL, local path, or document token |
| version | arXiv version, publication version, commit hash, file timestamp, or `(not visible)` |
| accessed_date | Absolute date when accessed |
| completeness | full text / abstract only / excerpt / missing appendix / figures checked from PDF / source unavailable |
| visual_source | PDF pages, extracted figures, screenshots, or `(not used)` |
| source_limitations | What this source cannot support |

## Citation Verification

Before making a document-style interpretation, verify bibliographic identity. This prevents analyzing the wrong version or overclaiming publication status.

| Citation Verification | 内容 |
|-|-|
| title_verified | yes/no plus source |
| authors_verified | yes/no plus source |
| venue_or_version_verified | venue, arXiv version, preprint status, or `(not visible)` |
| doi_or_arxiv_verified | DOI, arXiv ID, publisher URL, or `(not visible)` |
| code_data_supplement_checked | code/data/supplement/project status, or why unavailable |

Rules:
- If multiple sources are used, list the primary source first and secondary sources after it.
- If the paper has arXiv and a published version, identify which one the interpretation is based on and whether they may differ.
- If the source is partial, all evidence and claims must stay within that scope.
- If figures/tables are discussed, record whether they were read from PDF, HTML, source, or recreated from text.
- The lightweight gate script checks the first five fields: `source_type`, `source_url`, `version`, `accessed_date`, `completeness`.
- The lightweight gate script also checks Citation Verification fields for document-style outputs.
