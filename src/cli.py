# src/thesis_webscraper/cli.py
from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print
from thesis_webscraper.config import SECTION_URLS
from thesis_webscraper.config import ScrapeConfig
from thesis_webscraper.scraper import scrape

app = typer.Typer(add_completion=False, help="Thesis Webscraper CLI")

@app.command()
def run(
    section: str = typer.Option(..., "--section", help="Autohome section to scrape"),
    pages: int = typer.Option(1, "--pages", min=1, help="Number of list pages to crawl"),
    out_dir: Path = typer.Option(Path("data/"), "--out-dir", help="Output file path"),
):
    cfg = ScrapeConfig(
        section=section,
        pages=pages,
        out_dir=out_dir,
    )

    result = scrape(cfg)

    print("[bold green]Done![/bold green]")
    print(f"Posts: {result.posts_count}")
    print(f"Comments: {result.comments_count}")
    print(f"Output: {out_dir.resolve()}")

    summary_path = out_dir.parent / "run_summary.json"
    summary_path.write_text(json.dumps(result.to_dict(), indent=2), encoding="utf-8")


def main():
    app()


if __name__ == "__main__":
    main()
