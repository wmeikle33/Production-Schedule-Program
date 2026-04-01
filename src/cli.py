# src/production-schedule-program/cli.py
from __future__ import annotations

import json
from pathlib import Path

import typer
from rich import print

app = typer.Typer(add_completion=False, help="Thesis Webscraper CLI")

@app.command()
def run(
    out_dir: Path = typer.Option(Path("data/"), "--out-dir", help="Output file path"),
):

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
