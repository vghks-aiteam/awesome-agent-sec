# Curation and source notes

[繁體中文目錄](../README.md) · [English catalog](../README.en.md) · [繁體中文導讀](../README.zh-TW.md)

## Scope and provenance

The initial catalog was curated from the supplied AgentSec research notes: principles, threat taxonomy, arXiv papers, industry reports, blogs and discussions, incidents, open versus closed models, defenses, and open problems. The supplied `agentsec-v2` HTML export was used as the source snapshot.

The snapshot contained **152 distinct external URLs**: 68 arXiv pages, 20 Hacker News threads, and 64 other references. These are counts of source URLs, not the number of independent studies or catalog entries. The arXiv references include the Gemini engineering paper outside the original numbered paper list.

The catalog provides original Traditional Chinese annotations in README.md, a complete English version in README.en.md, and an additional Traditional Chinese reading guide. The two catalog versions preserve the same resources and original titles. The repository links third-party material rather than redistributing full papers, copied abstracts, the generated website, or its bundled assets.

## Verification performed on 2026-11-08

- Checked the titles and abstracts of the 68 arXiv references against their source pages. This is metadata and abstract review, not replication or full-text validation of the results.
- Reviewed source destinations for cataloged specifications, articles, reports, and tools. Followed redirects where the intended resource remained available.
- Checked the four CVE identifiers in the supplied notes against CNA records: the CVE Services record for CVE-2025-32711 and the CVE Program's cvelistV5 records for the other three.
- Reviewed the JFrog disclosure for mcp-remote and the original researcher disclosure for GitHub Copilot. Used Cursor's vendor advisory as the canonical CurXecute link.
- Checked Markdown structure, relative file links, heading anchors, and duplicate arXiv IDs in the finished repository.

Some initial retrieval attempts were rate-limited. Their responses were not counted as successful verification; source pages were subsequently reviewed through an alternative reader or the GitHub connector. A reachable URL is not proof that the associated research claim is correct.

## Link changes and exclusions

| Source reference | Treatment |
| --- | --- |
| `NVIDIA/NeMo-Guardrails` | Updated to the redirected canonical repository, `NVIDIA-NeMo/Guardrails`. |
| Anthropic's `/engineering/claude-code-sandboxing` | Updated to the redirected `/research/claude-code-sandboxing` article. |
| Unversioned MCP security best practices | Used the resolved `2026-07-28` documentation page. The authorization entry deliberately retains the supplied `2025-06-18` specification version. |
| NVD pages for the four supplied CVEs | Automated retrieval timed out or returned an empty page. Used CVE Program records, the vendor advisory, and first-hand disclosures to verify the identifiers and descriptions. |
| Koi's postmark-mcp article | The original URL redirected to a general Palo Alto Networks product page. Omitted as a standalone catalog entry because the destination no longer supplied the cited report. |
| USENIX presentation pages | Automated retrieval returned HTTP 403. Kept the corresponding papers through verified arXiv entries, without asserting a publication venue from blocked pages. |
| Google's security blog article | Retrieval encountered an access challenge. Retained the independently accessible Gemini research paper instead. |
| Nature Medicine DOI in the original notes | Not included as a standalone entry in this agent-focused catalog; its publisher content was unavailable during review. |
| Hacker News threads | Used as discovery context rather than primary evidence. Omitted duplicate discussion links from the catalog in favor of original resources. |
| Duplicate explainers, old documentation routes, and overlapping report links | Selected one canonical entry when the extra link added no distinct contribution. |

## Evidence and wording

The original notes sometimes used absolute claims such as inevitable exfiltration, universal defense failure, or unconditional architectural guarantees. The catalog instead describes the demonstrated mechanism and points readers to the source's assumptions.

The presence of untrusted content, private data, and an outbound channel is a useful warning pattern, not a measurement of compromise probability for every possible implementation. Similarly, a formal defense guarantee depends on its specified policy, trusted components, and mediation assumptions.

Research disclosures do not establish exploitation in the wild. Controlled agentic-misalignment evaluations are kept separate from the first-party DNS incident report. Historical product findings should be read with their affected versions and remediation details.

All 2026 watchlist items are linked as arXiv preprints with publication status left explicitly unverified. No claim is made that an arXiv posting has or has not subsequently passed peer review. Older arXiv links also do not by themselves establish peer review.

## Maintenance policy

Collect broadly relevant, verifiable agent-security resources without requiring a personal recommendation or endorsement. Keep research, implementations, historical disclosures, and general-purpose infrastructure distinguishable. Fix changed destinations, remove duplicates, and preserve meaningful caveats when editing descriptions.

The coverage update adds 19 resources on identity, authorization, secrets, runtime and supply-chain security, monitoring, audit, and incident response. The catalogs now contain 137 entries; resources.json records 139 source URLs, including two additional framework papers linked within tool entries.

The [status table](../RESOURCE_STATUS.md) records publication evidence, archive flags, release snapshots, model revisions, specification versions, and check dates. Eight paper records were matched to official publication pages or official publisher search indexes. The remaining 60 arXiv records explicitly leave formal publication status unverified. Some OpenReview and USENIX pages blocked automated retrieval; absence of verification is not evidence of non-publication.

Repository and release metadata were read from GitHub's public API. The old Azure/PyRIT repository is archived and points to microsoft/PyRIT; both catalogs use the new location. The OpenTelemetry GenAI conventions page has moved to open-telemetry/semantic-conventions-genai. Generic components such as OPA, SPIFFE, Kubernetes, and OpenBao are included for their role in agent infrastructure, without implying they are complete agent-security products.

GitHub Actions now checks bilingual resource parity, metadata coverage, generated status content, and local file/heading links. It also runs the Python unit, CLI-flow, and smoke checks. External links are checked on pushes, manual runs, and a weekly schedule, with an informational report in the job summary. HTTP 403/429 and timeouts remain unresolved instead of being counted as valid links. Metadata older than 90 days prompts a review warning.

Automated checks establish document and link properties, not scientific correctness, translation equivalence, ongoing project maintenance, or the safety of any deployment. Metadata and destination changes still need human review.
