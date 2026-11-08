"""Validate catalog parity and metadata; render the bilingual status reference."""

import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^)\n]+)\)")
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://[^)]+)\) — (.+)$")


def without_code(text):
    return re.sub(r"^```.*?^```[^\n]*", "", text, flags=re.M | re.S)


def entries(text):
    result = []
    section = 0
    for line in without_code(text).splitlines():
        if line.startswith("## "):
            section += 1
        match = ENTRY.match(line)
        if match:
            title, url, _ = match.groups()
            links = [target for _, target in LINK.findall(line)]
            result.append((title, url, section, links))
    return result


def heading_ids(text):
    result = set()
    seen = Counter()
    for line in without_code(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+)", line)
        if not match:
            continue
        name = re.sub(r"!\[.*?\]\(.*?\)", "", match[1])
        name = LINK.sub(lambda item: item[1], name).lower()
        name = re.sub(r"[^\w\s-]", "", name).replace(" ", "-")
        result.add(name + (f"-{seen[name]}" if seen[name] else ""))
        seen[name] += 1
    return result


def metadata_errors(records):
    errors = []
    for row in records:
        url = row.get("url", "")
        if url.startswith("https://arxiv.org/abs/") and row.get("kind") != "paper":
            errors.append(f"arXiv resource must be a paper: {url}")
        if not row.get("title") or row.get("kind") not in {"paper", "tool", "model", "specification", "reference"}:
            errors.append(f"Invalid title or kind: {url}")
        try:
            checked = date.fromisoformat(row.get("checked_on", ""))
            if checked > date.today():
                errors.append(f"Future check date: {url}")
        except (TypeError, ValueError):
            errors.append(f"Invalid check date: {url}")
        evidence = row.get("evidence_urls", [])
        if not evidence or any(not source.startswith("https://") for source in evidence):
            errors.append(f"Missing HTTPS evidence: {url}")
        if row.get("kind") == "paper":
            if row.get("publication_status") not in {"published", "unverified"}:
                errors.append(f"Invalid publication status: {url}")
            if row.get("publication_status") == "published" and (not row.get("venue") or row.get("publication_url") not in evidence):
                errors.append(f"Published paper needs venue and evidence: {url}")
        if row.get("kind") == "tool":
            if row.get("maintenance_status") not in {"not_archived", "archived", "unverified"}:
                errors.append(f"Invalid maintenance status: {url}")
            if row.get("latest_release") and (not row.get("release_url") or not row.get("release_date")):
                errors.append(f"Release needs URL and date: {url}")
        if row.get("kind") == "model" and not row.get("revision"):
            errors.append(f"Model needs revision: {url}")
        if row.get("kind") == "specification" and not row.get("version"):
            errors.append(f"Specification needs version: {url}")
    return errors


def cell(value):
    return str(value).replace("|", "\\|").replace("\n", " ")


def render_status(records):
    papers = [row for row in records if row["kind"] == "paper"]
    tools = [row for row in records if row["kind"] in {"tool", "model"}]
    specs = [row for row in records if row["kind"] == "specification"]
    published = sum(row["publication_status"] == "published" for row in papers)
    lines = [
        "# 資源狀態與版本 / Resource status and versions", "",
        "[繁體中文目錄](README.md) · [English catalog](README.en.md) · [來源紀錄](docs/curation.md)", "",
        "本表由 `resources.json` 產生。更新資料後執行 `python3 check_catalog.py --write-status`。 / Generated from `resources.json`.", "",
        f"收錄 {len(records)} 個來源 URL；其中 {len(papers)} 篇 arXiv 論文有 {published} 篇已找到正式出版紀錄，其餘明列未確認。 / {published} of {len(papers)} papers have verified publication records.", "",
        "- 「未確認 / Unverified」表示未獨立確認正式出版狀態，不代表已被拒絕或沒有通過 peer review。",
        "- Publisher index 表示核對官方搜尋索引中的出版 metadata；當時直接讀取頁面可能遇到 403 或 timeout。未進行論文結果重現。",
        "- 未封存 / Not archived 不等於積極維護；release 為查核當日 GitHub `releases/latest` 的回傳值，並非部署建議。",
        "- Living document 的內容會變更；導入前應另外 pin 實際採用的版本或 revision。",
        "- Dates describe metadata checks, not continuous monitoring. Publication, release, and archive status can change.", "",
        "## 論文出版狀態 / Publication status", "",
        "| 論文 / Paper | 狀態 / Status | Venue | 證據 / Evidence | 查核日期 / Checked |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in papers:
        status = "已出版 / Published" if row["publication_status"] == "published" else "未確認 / Unverified"
        evidence = f"[Publisher]({row['publication_url']})" if row.get("publication_url") else f"[arXiv]({row['url']})"
        if row.get("evidence_access") == "publisher_index":
            evidence += " (index)"
        lines.append(f"| [{cell(row['title'])}]({row['url']}) | {status} | {cell(row.get('venue', '—'))} | {evidence} | {row['checked_on']} |")
    lines += ["", "## 工具與模型 / Tools and models", "", "| 資源 / Resource | 狀態 / Status | Release / revision | 發布或修改日期 / Date | 查核日期 / Checked |", "| --- | --- | --- | --- | --- |"]
    labels = {"not_archived": "未封存 / Not archived", "archived": "已封存 / Archived", "unverified": "未確認 / Unverified"}
    for row in tools:
        if row["kind"] == "model":
            state = "模型 revision / Model revision"
            version = f"`{row['revision']}`"
            released = row.get("last_modified", "—")
        else:
            state = labels[row["maintenance_status"]]
            version = f"[{cell(row['latest_release'])}]({row['release_url']})" if row.get("latest_release") else "latest release 未取得 / Not available"
            released = row.get("release_date") or "—"
        lines.append(f"| [{cell(row['title'])}]({row['url']}) | {state} | {version} | {released[:10]} | {row['checked_on']} |")
    migrations = [row for row in records if row.get("previous_urls")]
    if migrations:
        lines += ["", "### 來源搬遷 / Source migrations", ""]
        for row in migrations:
            for previous in row["previous_urls"]:
                lines.append(f"- [{cell(row['title'])}]({previous}) → [目前來源 / Current source]({row['url']})。搬遷證據見 `resources.json`。")
    lines += ["", "## 規格版本 / Specification versions", "", "| 資源 / Resource | 版本 / Version | 查核日期 / Checked |", "| --- | --- | --- |"]
    for row in specs:
        lines.append(f"| [{cell(row['title'])}]({row['url']}) | {cell(row['version'])} | {row['checked_on']} |")
    lines += ["", "本表不包含所有文章的 metadata；完整來源清單與證據 URL 請查 `resources.json`。 / The JSON registry also includes the remaining references and evidence URLs.", ""]
    return "\n".join(lines)


def validate(root):
    errors = []
    try:
        zh = entries((root / "README.md").read_text())
        en = entries((root / "README.en.md").read_text())
        data = json.loads((root / "resources.json").read_text())
        records = data["resources"]
    except (OSError, ValueError, KeyError) as error:
        return [f"Cannot read catalog: {error}"]
    if not zh or zh != en:
        errors.append("Catalogs differ in titles, order, section placement, or linked resources")
    if data.get("schema_version") != 1:
        errors.append("Unsupported metadata schema")
    primary = [row[1] for row in zh]
    if len(primary) != len(set(primary)):
        errors.append("Duplicate catalog entries")
    urls = {url for row in zh for url in row[3]}
    registered = [row.get("url") for row in records]
    if len(registered) != len(set(registered)):
        errors.append("Duplicate metadata URLs")
    if urls != set(registered):
        errors.append(f"Metadata coverage mismatch: missing={sorted(urls - set(registered))}, extra={sorted(set(registered) - urls)}")
    lookup = {row.get("url"): row for row in records}
    for title, url, _, _ in zh:
        if url in lookup and title != lookup[url].get("title"):
            errors.append(f"Metadata title differs from catalog: {url}")
    errors += metadata_errors(records)
    for file in root.rglob("*.md"):
        if ".git" in file.parts or file.name == "link-report.md":
            continue
        for _, target in LINK.findall(without_code(file.read_text())):
            if urlsplit(target).scheme:
                continue
            path, _, fragment = target.partition("#")
            destination = (file.parent / unquote(path)).resolve() if path else file.resolve()
            if not destination.is_relative_to(root.resolve()) or not destination.is_file():
                errors.append(f"Missing local link in {file.name}: {target}")
            elif fragment and unquote(fragment) not in heading_ids(destination.read_text()):
                errors.append(f"Missing heading in {file.name}: {target}")
    status_file = root / "RESOURCE_STATUS.md"
    if errors:
        return errors
    if not status_file.exists() or status_file.read_text() != render_status(records):
        errors.append("RESOURCE_STATUS.md is stale; run python3 check_catalog.py --write-status")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--write-status", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    if args.write_status:
        data = json.loads((root / "resources.json").read_text())
        errors = metadata_errors(data["resources"])
        if errors:
            print("\n".join(errors))
            return 1
        (root / "RESOURCE_STATUS.md").write_text(render_status(data["resources"]))
    errors = validate(root)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        records = json.loads((root / "resources.json").read_text())["resources"]
        stale = sum((date.today() - date.fromisoformat(row["checked_on"])).days > 90 for row in records)
        if stale:
            print(f"WARNING: {stale} resource metadata records are older than 90 days; review their status")
        print(f"PASS: bilingual catalog, {len(records)} metadata records, status report, and local links")
    return bool(errors)


if __name__ == "__main__":
    raise SystemExit(main())
