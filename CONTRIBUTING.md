# Contributing

Contributions that help readers understand or secure AI agents are welcome. This is a broad resource index: inclusion indicates topical relevance, not endorsement. Traditional Chinese is used for the main catalog in README.md, with a complete English version in README.en.md and an additional Traditional Chinese reading guide. Keep resource titles and technical terms in their original language, and update both catalog versions when adding or changing an entry.

## What belongs here

- Original research on agent attacks, defenses, evaluation, or trust boundaries.
- Official specifications and actionable security guidance.
- Implementations with a clear purpose and usable documentation.
- First-hand vulnerability disclosures and incident reports.
- Explanations that make an existing research topic substantially easier to understand.

General AI news, promotional landing pages, unsourced performance claims, and duplicate summaries of an already listed resource usually do not add enough value.

## Adding a resource

1. Search the README for the title, URL, arXiv ID, or CVE to avoid duplicates.
2. Choose the closest existing section. Link the original source using HTTPS.
3. Add one concise sentence explaining the contribution or use case.
4. Identify the resource type and, where relevant, its year of first publication or disclosure.
5. For papers, confirm that the linked ID matches the title. Add a venue only when confirmed by the publisher or conference.
6. For disclosures, distinguish a research demonstration from observed exploitation. Avoid claiming a historical vulnerability affects current releases without evidence.
7. Add the resource URL and evidence to resources.json. Include secondary paper links attached to tool entries as separate records.
8. Regenerate RESOURCE_STATUS.md and explain the addition or correction in your pull request, including how you verified the source.

Use the existing format:

```markdown
- [Resource name](https://original-source.example/resource) — **Paper · 2026.** A concise description of the contribution and its relevance to agent security.
```

New preprints with unverified publication status belong in the research watchlist. Clearly separate a proposed defense from a validated deployment result. Reported guarantees and attack success rates need their threat model and evaluation conditions.

## Recording status and versions

- Papers use `publication_status: published` only with a venue and an official publisher or conference evidence URL. Record whether the evidence came from the page or its official search index. Otherwise use `unverified`; an arXiv page alone is not proof of peer review.
- Tools record the repository's archive flag and the release returned by GitHub's `releases/latest` endpoint at the check date. `not_archived` does not mean actively maintained. If the endpoint returns no release, retain that uncertainty instead of inventing a version.
- Models record an immutable revision. Specifications record a pinned version or explicitly identify rolling documentation.
- Set `checked_on` to the date the metadata was actually checked, and keep supporting URLs in `evidence_urls`. A link check does not automatically refresh a publication or maintenance check date.
- When a source moves, update both catalogs and keep its earlier URL and migration evidence in the metadata. Archived resources can remain relevant historical references when clearly labeled.

Use Python 3.12 or newer; the checker uses only the standard library:

```sh
python3 check_catalog.py --write-status
python3 check_catalog.py
python3 -m unittest -v
```

The checker compares resource titles, order, section placement, and secondary links across both languages; verifies metadata coverage and local links; and detects a stale generated status table. It does not assess whether translations have equivalent meaning or whether a paper's results reproduce. Metadata older than 90 days produces a review warning.

## Before opening a pull request

- Check spelling, section placement, and GitHub Markdown rendering.
- Verify relative links and heading anchors after renaming or moving content.
- Open external links and check that the destination is the intended resource; a successful HTTP response alone is insufficient.
- Keep navigation consistent across both catalog versions and the Chinese guide when changing the catalog structure.
- Describe blocked or unavailable sources explicitly instead of marking them verified.

The repository has no application build. Changes to the checker should include relevant unit tests; the suite also exercises the CLI generation/checking flow and a repository smoke check.

## Automated checks and maintenance

GitHub Actions runs the deterministic catalog checks on pushes and pull requests. Pushes, manual runs, and a weekly Monday 02:17 UTC schedule also produce a lychee external-link report in the job summary.

External network results are informational so that access challenges and rate limits do not block unrelated content changes. HTTP 403, 429, timeouts, and other failures remain unresolved in the report; they are not accepted as valid links. Review the report to distinguish a removed resource from a site rejecting automated access. A successful HTTP response still needs a human check when its destination changes.

Review unresolved link reports regularly and recheck publication, release, and archive metadata at least quarterly. The workflow reports drift; it does not silently rewrite publication status or tool versions.

## Attribution and license

Write original descriptions rather than copying abstracts or articles. Contributions to the curation and annotations are made under the repository's CC0 1.0 dedication. Third-party resources keep their own licenses.
