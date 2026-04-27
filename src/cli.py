from __future__ import annotations

import typer
from rich import print

from .config import ProgramConfig
from .pipeline import pipeline

app = typer.Typer(add_completion=False, help="Production Scheduling Program CLI")


@app.command()
def run(
    value_list: list[str] = typer.Option(
        ..., "--value-list", help="Values for Production Program"
    ),
    date: str = typer.Option(
        ..., "--date", help="Production date"
    ),
    new_values: list[str] = typer.Option(
        ..., "--new-values", help="New values for Production Program"
    ),
    market: str = typer.Option(
        ..., "--market", help="Market"
    ),
):
    config = ProgramConfig(
        value_list=value_list,
        date=date,
        new_values=new_values,
        market=market,
    )

    result = pipeline(config)

    print("[bold green]Done![/bold green]")
    print(result)


def main():
    app()


if __name__ == "__main__":
