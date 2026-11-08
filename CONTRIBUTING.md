# Contributing

Contributions that help readers understand or secure AI agents are welcome. Traditional Chinese is used for the main catalog in README.md, with a complete English version in README.en.md and an additional Traditional Chinese reading guide. Keep resource titles and technical terms in their original language, and update both catalog versions when adding or changing an entry.

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
7. Explain the addition or correction in your pull request and note how you verified the source.

Use the existing format:

```markdown
- [Resource name](https://original-source.example/resource) — **Paper · 2026.** A concise description of the contribution and its relevance to agent security.
```

New preprints with unverified publication status belong in the research watchlist. Clearly separate a proposed defense from a validated deployment result. Reported guarantees and attack success rates need their threat model and evaluation conditions.

## Before opening a pull request

- Check spelling, section placement, and GitHub Markdown rendering.
- Verify relative links and heading anchors after renaming or moving content.
- Open external links and check that the destination is the intended resource; a successful HTTP response alone is insufficient.
- Keep navigation consistent across both catalog versions and the Chinese guide when changing the catalog structure.
- Describe blocked or unavailable sources explicitly instead of marking them verified.

This is a documentation repository and has no application build or runtime test suite. Content review and link verification are the relevant checks.

## Attribution and license

Write original descriptions rather than copying abstracts or articles. Contributions to the curation and annotations are made under the repository's CC0 1.0 dedication. Third-party resources keep their own licenses.
