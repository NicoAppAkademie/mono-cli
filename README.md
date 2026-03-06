# mono-cli

A minimalist, personal CLI for browsing Reddit.

## Features

- **Personalized Feed:** Optimized for individual use and focused subreddit navigation.
- **Clean Interface:** A minimalist command-line interface designed for speed and readability.
- **Python Powered:** Built using modern Python libraries like [Typer](https://typer.tiangolo.com/) and [Questionary](https://questionary.readthedocs.io/) for a robust user experience.

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Clone the repository
git clone https://github.com/NicoAppAkademie/mono-cli.git
cd mono-cli

# Install dependencies and sync virtual environment
uv sync
```

## Usage

You can run the CLI using `uv`:

```bash
uv run mono
```

Or install it as a global command:

```bash
uv tool install .
mono --help
```

## Development

To set up a development environment:

```bash
uv venv
source .venv/bin/activate
uv sync
```

## License

[MIT](LICENSE)
