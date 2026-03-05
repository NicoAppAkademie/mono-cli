import json
from pathlib import Path

import questionary
import typer

app = typer.Typer()

DATA_FILE = Path.home() / ".mono" / "links.json"


def load_links() -> list[dict]:
    if not DATA_FILE.exists():
        return []
    return json.loads(DATA_FILE.read_text())


def save_links(links: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(json.dumps(links, indent=2))


def handle_add() -> None:
    url = questionary.text("URL:").ask()
    if url is None:
        return
    note = questionary.text("Note:").ask()
    if note is None:
        return
    links = load_links()
    links.append({"url": url, "note": note})
    save_links(links)
    typer.echo(f"Saved: {url}")


@app.command()
def main() -> None:
    while True:
        choice = questionary.select(
            "mono",
            choices=["Add", "Delete", "Edit", "Exit"],
        ).ask()

        if choice == "Exit" or choice is None:
            raise typer.Exit()

        if choice == "Add":
            handle_add()
