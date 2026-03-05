import questionary
import typer

app = typer.Typer()


@app.command()
def main() -> None:
    while True:
        choice = questionary.select(
            "mono",
            choices=["Add", "Delete", "Edit", "Exit"],
        ).ask()

        if choice == "Exit" or choice is None:
            raise typer.Exit()
